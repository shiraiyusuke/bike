# -*- coding: utf-8 -*-
import logging


def get_logger(name, level_stream='info', logfile=None, level_file=None, rotate_when='D', rotate_count=7):
    """    指定されたログレベル・ファイルを定義したロガーの返却
    :param name: モジュール名[str]
    :param level_stream: ストリームログレベル[str]
    :param log_file: ログファイル[str]
    :param level_file: ログレベル[str]
    :param rotate_when: ローテートのタイミング[str]
    :param rotate_count: ローテート世代数[int]
    :return: 定義済みのロガー[logging.:Logger]
    """
    log_level = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    # サポートのないログレベルが指定されたら、infoを指定
    if not level_stream or not log_level[level_stream]:
        level_stream = 'info'

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # ログフォーマットの定義
    formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineng)s - %(funcName)s - %(message)s')

    # ストリームハンドラ定義
    sh = logging.StreamHandler()
    sh.setLevel(log_level[level_stream])
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    # ログファイルが指定されている場合
    if logfile:
        if not level_file or not log_level[level_file]:
            level_file = level_stream

        # ファイルハンドラを定義
        fh = logging.FileHandler(logfile)
        fh.setLevel(log_level[level_file])
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger

if __name__ == '__main__':
    get_logger()