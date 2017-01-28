# -*- coding: utf-8 -*-
import flask
import os
import argparse
from log import get_logger

WORK_DIR = '/usr/local/wk/git_local/bike/'
MODEL_DIR = WORK_DIR + 'analysis/front_fork/model/'
ARCHITECT_FILE = MODEL_DIR + '/bike_conv_model_architecture_arg.json'
WEIGHT_FILE = MODEL_DIR + '/bike_conv_model_weights_arg.h5'

def parse_args():
    """    引数をパースして返却    """
    parser = argparse.ArgumentParser(description='bike front fork API')

    parser.add_argument('-d', '--debug', action='store_true', default=False, help='デバッグモード')
    parser.add_argument('--port', type=int, dest='port', default=5001, help='ポート番号')
    parser.add_argument('--proc', type=int, dest='proc', default=1, help='サーバープロセス数')
    parser.add_argument('--log-file', type=str, dest='log_file', default='./log/bike_result.log', help='ログファイル')
    parser.add_argument('--log-level', type=str, dest='log_level', default='info', help='ログレベル')

    return parser.parse_args()

def logging_args(logger, args):
    """    指定されたロガーに引数の項目名と値を出力(ログレベル:info)
    :param logger: logging.Loggerオブジェクト
    :param args: argparse.ArgumentParserオブジェクト
    :return:
    """
    for arg in vars(args):
        val = getattr(args, arg) # argsの中のargを取得

        if type(val) == list and len(val) > 0:
            if type(val[0]) == unicode:
                val = ', '.join(val).encode('utf-8')
            else:
                val = ', '.join(val)

        logger.info('arguments %s = %s' % (arg, val))

if __name__ == '__main__':
    args = parse_args()
    print args

    logger = get_logger(__name__, args.log_level, args.log_file, args.log_level)
    logging_args(logger, args)
