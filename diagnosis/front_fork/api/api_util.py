# -*- coding: utf-8 -*-
"""
api_util:API共通処理モジュール
"""
import os
import tornado
import tornado.wsgi
import tornado.ioloop
import tornado.httpserver
import log
import string
import tempfile
from datetime import datetime
import hashlib
from werkzeug.utils import secure_filename
import random
import time
from flask import Response
import json


def start_tornado(app, port, proc):
    """    指定されたポート番号、プロセス数でアプリケーションサーバーを起動する
    :param app: Flask アプリケーションオブジェクト
    :param port: 起動するポート番号
    :param proc: 起動するプロセス数
    :return:
    """
    http_server = tornado.httpserver.HTTPServer(tornado.wsgi.WSGIContainer(app))
    http_server.bind(port)
    http_server.start(proc)
    print('Tornado server starting on port {}'.format(port))
    tornado.ioloop.IOLoop.instance().start()


def start_from_terminal(app, port=5000, proc=1, debug=False):
    """   アプリケーションを Flask または tornadoで起動する
    :param app: Flaskアプリケーションオブジェクト
    :param port: 起動するポート番号
    :param proc: 起動するプロセス数
    :param debug: デバッグフラグ
    :return:
    """
    if os.path.dirname(__file__) == '':
        os.chdir('./')
    else:
        os.chdir(os.path.dirname(__file__))

    if debug:
        app.run(debug=debug, host='0.0.0.0', port=port)
    else:
        start_tornado(app, port, proc)


class BaseApi(object):
    """    API共通処理クラス    """
    # 許可される画像拡張子
    allowed_image_extensions = {'png', 'bmp', 'jpg', 'jpe', 'jpeg', 'gif'}

    # エラー番号・メッセージ対応表
    error_map = {
        101: 'INCORRECT_API_KEY',
        102: 'INVALID_PARAMETER',
        103: 'BAD_UPLOAD_FILE',
        104: 'FILE_SIZE_TOO_LEARGE',
        201: 'IMAGE_FILE_UPLOAD_FAILED',
        202: 'IMAGE_KEY_DOES_NOT_SPECIFIED',
        203: 'IMAGE_FILE_DOES_NOT_EXIST',
        999: 'OTHER_EXCEPTION'
    }

    def __init__(self, logger=None):
        """    API共通処理クラスの初期化処理
        :param logger: ロガーオブジェクト
        :return:
        """
        if logger:
            self.logger = logger
        else:
            self.logger = log.get_logger(__name__)

    def check_value(self, value, length=80, has_alphabet=True, has_number=True, has_symbol=True):
        """    単体パラメータチェック処置
        :param value: パラメータ値
        :param length: 値の最大文字列数(None または 0 を指定した時は無制限)
        :param has_alphabet: 英字を含むことの許可フラグ
        :param has_number: 数字を含むことの許可フラグ
        :param has_symbol: 記号を含むことの許可フラグ
        :return: True or False
        """
        if length and 0 < length < len(value):
            self.logger.error('Parameter value length error: {} longer than {}'
                              .format(len(value), length))
            return False

        allowed_string = ''

        if has_alphabet:
            allowed_string += string.ascii_letters
        if has_number:
            allowed_string += string.digits
        if has_symbol:
            allowed_string += '%$&()<>[]{}!?/*+=-.,:;^~_'

        allowed_string_set = set(allowed_string)

        if allowed_string_set:
            for char in set(value):
                if char not in allowed_string_set:
                    self.logger.error(
                        'Parameter value string error: {} include no allowed charactor {}'.format(
                            value.encode('utf-8', char.encode('utf-8'))))
                    return False
        return True

    def allowed_file(self, filename):
        """   指定したファイル名の拡張子チェック
        :param filename: ファイル名
        :return: True or False
        """
        checked = ('.' in os.path.basename(filename) and
                   filename.rsplit('.', 1)[1].lower() in BaseApi.allowed_image_extensions)

        if not checked:
            self.logger.error('Check file extension {} is not allowed.'.format(filename))

        return checked

    def get_tempdir(self, base_dir, imagekey='imagekey', prefix='temp'):
        """   指定されたディレクトリいかに一時ディレクトリを作成してファイルパスを返却します
        :param base_dir: 保存先ディレクトリ
        :param imagekey: 画像キー
        :param prefix: 接頭語
        :return: 一時ディレクトリパス
        """
        try:
            output_dir = tempfile.mkdtemp(
                prefix='-'.join([
                    prefix,
                    imagekey,
                    str(datetime.now().strftime('%s')).replace(' ', '_')
                ]) + '-',
                dir=base_dir)
            os.chmod(output_dir, 0755)
            self.logger.info('Create output directory {} success.'.format(output_dir))
            return output_dir

        except IOError as e:
            self.logger.error('Catch exception: {}'.format(e))
            return None

    def get_imagekey(self, image_data):
        """    指定された画像の画像キーを返却
        :param image_data: 画像データ
        :return: 画像キー or None
        """
        try:
            md5 = hashlib.md5()
            md5.update('_'.join([
                str(datetime.now().strftime('%s')),
                secure_filename(image_data.filename),
                str(random.random())]))
            imagekey = md5.hexdigest()
            return imagekey

        except IOError as e:
            self.logger.error('Catch exception: {}'.format(e))
            return None

    def save_image(self, image, base_dir):
        """    指定された画像を保存先ディレクトリに保存して画像キーを返却
        :param image: 画像データ
        :param base_dir: 保存先ディレクトリ
        :return: 画像キー or None
        """
        try:
            md5 = hashlib.md5()
            md5.update('_'.join([
                str(datetime.now().strftime("%s")),
                secure_filename(image.filename),
                str(random.random())]))

            imagekey = md5.hexdigest()
            filename = os.path.join(base_dir, imagekey)
            image.save(filename)

            self.logger.info('Save image file {} success.'.format(filename))
            return imagekey

        except IOError as e:
            self.logger.error('Catch exception: {}'.format(e))
            return None

    def check_image(self, imagekey, base_dir):
        """    指定された画像キーのファイルが保存先ディレクトリに存在するか確認して画像ファイルパスを返却
        :param imagekey: 画像キー
        :param base_dir: 保存先ディレクトリ
        :return: 画像ファイルパス or None
        """
        try:
            filename = os.path.join(base_dir, imagekey)
            if os.path.exists(filename):
                self.logger.info('Check image file {} success.'.format(filename))
                return filename
            else:
                self.logger.error('Check image file {} failed.'.format(filename))
                return None

        except IOError as e:
            self.logger.error('Catch exception: {}'.format(e))
            return None

    def make_dir(self, dirpath):
        """    指定されたディレクトリが存在しない、作成してパスを返却
        :param dirpath: ディレクトリパス
        :return: ディレクトリパス
        """
        try:
            if os.path.exists(dirpath):
                self.logger.error('{} already exists.'.format(dirpath))
            else:
                os.mkdir(dirpath)

                if os.path.isdir(dirpath):
                    return dirpath
                else:
                    self.logger.error('{} directory create failed'.format(dirpath))
                    return None

        except IOError as e:
            self.logger.error('Catch exception: {}'.format(e))
            return None

    def json_success(self, result, imagekey, start_time=None):
        """    処理成功時のjson返却
        :param result: 結果データ
        :param imagekey: 画像キー
        :param start_time: 開始時間
        :return: jsonフォーマットデータ
        """
        try:
            if start_time:
                elapsed_time = float('%.3f' % (time.time() - start_time))
            else:
                elapsed_time = None

            return Response(json.dumps({
                'status': 0,
                'result': result,
                'imagekey': imagekey,
                'time': elapsed_time
            }, sort_keys=False), content_type='application/json; charset=utf-8')

        except Exception as e:
            self.logger.error('Catch exception: {}'.format(e))
            return None

    def json_fail(self, err_no, err=None, start_time=None):
        """    処理失敗時のjson文字列を返却
        :param err_no: エラー番号
        :param err: エラーオブジェクト
        :param start_time: 開始時間
        :return: jsonフォーマットデータ
        """
        try:
            self.logger.error('{}: {}'.format(self.error_map[err_no], err))

            if start_time:
                elapsed_time = float('%.3f' % (time.time() - start_time))
            else:
                elapsed_time = None

            return Response(json.dumps({
                'status': err_no,
                'massage': BaseApi.error_map[err_no],
                time: elapsed_time
            }, sort_keys=False), content_type='application/json; charset=utf-8')

        except Exception as e:
            self.logger.error('Catch exception: {}'.format(e))
            return None

    def check_apikey(self, request_key, correct_key):
        """    指定されたAPIキーが一致しているかどうかを返却
        :param request_key: リクエストAPIキー
        :param correct_key: 正しい APIキー
        :return: True or False
        """
        if correct_key is None:
            return True

        if request_key == correct_key:
            return True
        else:
            self.logger.error('Incorrect api key. request_key={}, correct_key={}'.format(request_key, correct_key))
            return False

    def elapsed_time(self, exec_method, return_time=False):
        """    指定されたメソッドの実行時間を計測して返却
        :param exec_method:
        :param return_time:
        :return:
        """
        start_time = time.time()
        try:
            if return_time:
                return exec_method, time.time() - start_time
            else:
                return exec_method

        finally:
            self.logger.info('method {} execute elapsed time: {} sec.'
                             .format(exec_method.__name__, time.time() - start_time))
