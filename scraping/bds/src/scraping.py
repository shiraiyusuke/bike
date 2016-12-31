# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
import sys


class article():
    def __init__(self):
        pass


def get_data(driver, date):
    out_str_list = []

    # 基本情報= ''
    try: chassis_num     = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[1]/table/tbody/tr[1]/td').text
    except: chassis_num    = '' # 台車番号
    try: engine_form     = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[1]/table/tbody/tr[2]/td').text
    except: engine_form    = '' # エンジン型式
    try: kilometers      = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[1]/table/tbody/tr[3]/td').text
    except: kilometers     = '' # 走行距離
    try: kilometers_doc  = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[1]/table/tbody/tr[4]/td').text
    except: kilometers_doc = '' # 書類距離
    try: kilometers_past = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[1]/table/tbody/tr[5]/td').text
    except: kilometers_past= '' # 過去距離
    try: color           = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[1]/table/tbody/tr[6]/td').text
    except: color          = '' # 色
    try: displacement    = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[1]/table/tbody/tr[7]/td').text
    except: displacement   = '' # 排気量
    try: firsr_year      = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td').text
    except: firsr_year     = '' # 初年度
    try: inspection      = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td').text
    except: inspection     ='' # 車検・保険
    if driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/th').text.encode('utf-8') == 'パーツ有無':
        try: parts           = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td').text
        except: parts        = ''# パーツ有無
        try: enroll_num      = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td').text
        except: enroll_num   = ''# 登録番号
        try: start_price     = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td').text
        except: start_price  = ''# スタート価格
        try: sold_price      = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td').text
        except: sold_price   = ''# 売切価格
        try: bid             = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[7]/td/p/span[1]').text
        except: bid          = ''# 落札
        try: finish_price    = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[7]/td/p/span[2]').text
        except: finish_price = ''# 価格
    else:
        try: parts           = ''
        except: parts        = ''# パーツ有無
        try: enroll_num      = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td').text
        except: enroll_num   = ''# 登録番号
        try: start_price     = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td').text
        except: start_price  = ''# スタート価格
        try: sold_price      = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[5]/td').text
        except: sold_price   = ''# 売切価格
        try: bid             = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td/p/span[1]').text
        except: bid          = ''# 落札
        try: finish_price    = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[1]/div[2]/table/tbody/tr[6]/td/p/span[2]').text
        except: finish_price = ''# 価格

    # コメント
    try: bds_report      = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[1]/p').text
    except: bds_report   = ''# BDS報告
    try: bid_report      = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[2]/div[2]/div/p').text
    except: bid_report   = ''# 落札価格情報
    try: store_report    = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/p').text
    except: store_report = ''# 出品店申告

    # 点数= ''
    try: total_score     = driver.find_element(By.XPATH, '//*[@id="rank"]/tbody/tr[2]/td[1]').text
    except: total_score   = ''# 総合点数
    try: engine_score    = driver.find_element(By.XPATH, '//*[@id="rank"]/tbody/tr[2]/td[2]').text
    except: engine_score  = ''# エンジン点数
    try: ftire_score     = driver.find_element(By.XPATH, '//*[@id="rank"]/tbody/tr[2]/td[3]').text
    except: ftire_score   = ''# フロント足回り点数
    try: exterior_score  = driver.find_element(By.XPATH, '//*[@id="rank"]/tbody/tr[2]/td[4]').text
    except: exterior_score= ''# 外装点数
    try: rtire_score     = driver.find_element(By.XPATH, '//*[@id="rank"]/tbody/tr[2]/td[5]').text
    except: rtire_score   = ''# リア足回り点数
    try: denho_score     = driver.find_element(By.XPATH, '//*[@id="rank"]/tbody/tr[2]/td[6]').text
    except: denho_score   = ''# 電/保点数
    try: chassis_score   = driver.find_element(By.XPATH, '//*[@id="rank"]/tbody/tr[2]/td[7]').text
    except: chassis_score = ''# 車台点数

    try: engine_engine     = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[1]/table/tbody/tr[1]/td').text
    except: engine_engine     = ''# エンジン
    try: engine_cover      = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[1]/table/tbody/tr[2]/td').text
    except: engine_cover      = ''# カバー
    try: engine_oil        = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[1]/table/tbody/tr[3]/td').text
    except: engine_oil        = ''# オイル漏れ
    try: engine_radiator   = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[1]/table/tbody/tr[4]/td').text
    except: engine_radiator   = ''# ラジエター
    try: engine_cab        = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[1]/table/tbody/tr[5]/td').text
    except: engine_cab        = ''# キャブ
    try: engine_cratch     = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[1]/table/tbody/tr[6]/td').text
    except: engine_cratch     = ''# クラッチ
    try: engine_cell       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[1]/table/tbody/tr[7]/td').text
    except: engine_cell       = ''# セル
    try: ftire_outer       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[2]/table/tbody/tr[1]/td').text
    except: ftire_outer       = ''# アウター
    try: ftire_inner       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[2]/table/tbody/tr[2]/td').text
    except: ftire_inner       = ''# インナー
    try: ftire_stem        = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[2]/table/tbody/tr[3]/td').text
    except: ftire_stem        = ''# ステム
    try: ftire_handle      = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[2]/table/tbody/tr[4]/td').text
    except: ftire_handle      = ''# ハンドル
    try: ftire_wheel       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[2]/table/tbody/tr[5]/td').text
    except: ftire_wheel       = ''# ホイル
    try: ftire_brake       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[2]/table/tbody/tr[6]/td').text
    except: ftire_brake       = ''# ブレーキ
    try: ftire_tire        = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[1]/div[2]/table/tbody/tr[7]/td').text
    except: ftire_tire        = ''# タイヤ
    try: outer_upper       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[1]/table/tbody/tr[1]/td').text
    except: outer_upper       = ''# アッパー
    try: outer_center      = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[1]/table/tbody/tr[2]/td').text
    except: outer_center      = ''# センター
    try: outer_under       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[1]/table/tbody/tr[3]/td').text
    except: outer_under       = ''# アンダー
    try: outer_side        = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[1]/table/tbody/tr[4]/td').text
    except: outer_side        = ''# サイド
    try: outer_tank        = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[1]/table/tbody/tr[5]/td').text
    except: outer_tank        = ''# タンク
    try: outer_sheet       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[1]/table/tbody/tr[6]/td').text
    except: outer_sheet       = ''# シート
    try: outer_tail        = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[1]/table/tbody/tr[7]/td').text
    except: outer_tail        = ''# テール
    try: outer_ffender     = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[1]/table/tbody/tr[8]/td').text
    except: outer_ffender     = ''# 前フェンダー
    try: outer_bfender     = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[1]/table/tbody/tr[9]/td').text
    except: outer_bfender     = ''# 後フェンダー
    try: outer_screen      = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[1]/table/tbody/tr[10]/td').text
    except: outer_screen      = '' # スクリーン
    try: rtire_shock       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[2]/table/tbody/tr[1]/td').text
    except: rtire_shock       = ''# ショック
    try: rtire_swingarm    = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[2]/table/tbody/tr[2]/td').text
    except: rtire_swingarm    = ''# スイングアーム
    try: rtire_chain       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[2]/table/tbody/tr[3]/td').text
    except: rtire_chain       = ''# チェーン
    try: rtire_sprocket    = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[2]/table/tbody/tr[4]/td').text
    except: rtire_sprocket    = ''# スプロケ
    try: rtire_wheel       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[2]/table/tbody/tr[5]/td').text
    except: rtire_wheel       = ''# ホイル
    try: rtire_brake       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[2]/table/tbody/tr[6]/td').text
    except: rtire_brake       = ''# ブレーキ
    try: rtire_tire        = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[3]/div[2]/table/tbody/tr[7]/td').text
    except: rtire_tire        = ''# タイヤ
    try: denho_key         = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[1]/table/tbody/tr[1]/td').text
    except: denho_key         = ''# キー
    try: denho_meter       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[1]/table/tbody/tr[2]/td').text
    except: denho_meter       = ''# メーター
    try: denho_blinker     = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[1]/table/tbody/tr[3]/td').text
    except: denho_blinker     = ''# ウインカー
    try: denho_right       = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[1]/table/tbody/tr[4]/td').text
    except: denho_right       = ''# ライト
    try: denho_battery     = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[1]/table/tbody/tr[5]/td').text
    except: denho_battery     = ''# バッテリー
    try: denho_horn        = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[1]/table/tbody/tr[6]/td').text
    except: denho_horn        = ''# ホーン
    try: denho_brakelamp   = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[1]/table/tbody/tr[7]/td').text
    except: denho_brakelamp   = ''# ブレーキランプ
    try: outer_mirror      = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[1]/table/tbody/tr[8]/td').text
    except: outer_mirror      = ''# ミラー
    try: outer_muffler     = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[1]/table/tbody/tr[9]/td').text
    except: outer_muffler     = ''# マフラー
    try: outer_exhaustpipe = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[1]/table/tbody/tr[10]/td').text
    except: outer_exhaustpipe = '' # エキパイ
    try: chassis_mainframe = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[2]/table/tbody/tr[1]/td').text
    except: chassis_mainframe = ''# メインフレーム
    try: chassis_downtube  = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[2]/table/tbody/tr[2]/td').text
    except: chassis_downtube  = ''# ダウンチューブ
    try: chassis_stopper   = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[2]/table/tbody/tr[3]/td').text
    except: chassis_stopper   = ''# ストッパー
    try: chassis_sheetrail = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[2]/table/tbody/tr[4]/td').text
    except: chassis_sheetrail = ''# シートレール
    try: chassis_step      = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[2]/table/tbody/tr[5]/td').text
    except: chassis_step      = ''# ステップ
    try: chassis_stand     = driver.find_element(By.XPATH, '//*[@id="kensa"]/div[4]/div[2]/table/tbody/tr[6]/td').text
    except: chassis_stand     = ''# スタンド
    try: bike_no           = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[3]/form/div[1]/div[3]/div[1]/span[2]').text.strip()
    except: bike_no           = ''


    # url作成
    front_url = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_cube_high/' + bike_no + date + '_f.jpg'
    back_url = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_cube_high/' + bike_no + date + '_b.jpg'
    right_url = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_cube_high/' + bike_no + date + '_r.jpg'
    left_url = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_cube_high/' + bike_no + date + '_l.jpg'
    top_url = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_cube_high/' + bike_no + date + '_t.jpg'
    bottom_url = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_cube_high/' + bike_no + date + '_u.jpg'

    engin_url1 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_010_01.jpg'
    engin_url2 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_010_02.jpg'
    engin_url3 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_010_03.jpg'
    engin_url4 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_010_04.jpg'

    ftire_url1 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_020_01.jpg'
    ftire_url2 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_020_02.jpg'
    ftire_url3 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_020_03.jpg'
    ftire_url4 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_020_04.jpg'

    outer_url1 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_030_01.jpg'
    outer_url2 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_030_02.jpg'
    outer_url3 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_030_03.jpg'
    outer_url4 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_030_04.jpg'

    rtire_url1 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_040_01.jpg'
    rtire_url2 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_040_02.jpg'
    rtire_url3 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_040_03.jpg'
    rtire_url4 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_040_04.jpg'

    denho_url1 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_050_01.jpg'
    denho_url2 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_050_02.jpg'
    denho_url3 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_050_03.jpg'
    denho_url4 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_050_04.jpg'

    chassis_url1 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_060_01.jpg'
    chassis_url2 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_060_02.jpg'
    chassis_url3 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_060_03.jpg'
    chassis_url4 = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/image_item_high/' + bike_no + date + '_060_04.jpg'

    movie_l = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/movie_engine/' + bike_no + date +'_l.mp4'
    movie_r = 'http://jadb2.jupiter.ac/auctiondata/bds/disp/bds/' + date + '/movie_engine/' + bike_no + date +'_r.mp4'

    out_str_list.append(str(chassis_num.encode('utf-8')))
    out_str_list.append(str(engine_form.encode('utf-8')))
    out_str_list.append(str(kilometers.encode('utf-8')))
    out_str_list.append(str(kilometers_doc.encode('utf-8')))
    out_str_list.append(str(kilometers_past.encode('utf-8')))
    out_str_list.append(str(color.encode('utf-8')))
    out_str_list.append(str(displacement.encode('utf-8')))
    out_str_list.append(str(firsr_year.encode('utf-8')))
    out_str_list.append(str(inspection.encode('utf-8')))
    out_str_list.append(str(parts.encode('utf-8')))
    out_str_list.append(str(enroll_num.encode('utf-8')))
    out_str_list.append(str(start_price.encode('utf-8')))
    out_str_list.append(str(sold_price.encode('utf-8')))
    out_str_list.append(str(bid.encode('utf-8')))
    out_str_list.append(str(finish_price.encode('utf-8')))
    out_str_list.append(str(bds_report.encode('utf-8')))
    out_str_list.append(str(bid_report.encode('utf-8')))
    out_str_list.append(str(store_report.encode('utf-8')))
    out_str_list.append(str(total_score.encode('utf-8')))
    out_str_list.append(str(engine_score.encode('utf-8')))
    out_str_list.append(str(ftire_score.encode('utf-8')))
    out_str_list.append(str(exterior_score.encode('utf-8')))
    out_str_list.append(str(rtire_score.encode('utf-8')))
    out_str_list.append(str(denho_score.encode('utf-8')))
    out_str_list.append(str(chassis_score.encode('utf-8')))
    out_str_list.append(str(engine_engine.encode('utf-8')))
    out_str_list.append(str(engine_cover.encode('utf-8')))
    out_str_list.append(str(engine_oil.encode('utf-8')))
    out_str_list.append(str(engine_radiator.encode('utf-8')))
    out_str_list.append(str(engine_cab.encode('utf-8')))
    out_str_list.append(str(engine_cratch.encode('utf-8')))
    out_str_list.append(str(engine_cell.encode('utf-8')))
    out_str_list.append(str(ftire_outer.encode('utf-8')))
    out_str_list.append(str(ftire_inner.encode('utf-8')))
    out_str_list.append(str(ftire_stem.encode('utf-8')))
    out_str_list.append(str(ftire_handle.encode('utf-8')))
    out_str_list.append(str(ftire_wheel.encode('utf-8')))
    out_str_list.append(str(ftire_brake.encode('utf-8')))
    out_str_list.append(str(ftire_tire.encode('utf-8')))
    out_str_list.append(str(outer_upper.encode('utf-8')))
    out_str_list.append(str(outer_center.encode('utf-8')))
    out_str_list.append(str(outer_under.encode('utf-8')))
    out_str_list.append(str(outer_side.encode('utf-8')))
    out_str_list.append(str(outer_tank.encode('utf-8')))
    out_str_list.append(str(outer_sheet.encode('utf-8')))
    out_str_list.append(str(outer_tail.encode('utf-8')))
    out_str_list.append(str(outer_ffender.encode('utf-8')))
    out_str_list.append(str(outer_bfender.encode('utf-8')))
    out_str_list.append(str(outer_screen.encode('utf-8')))
    out_str_list.append(str(rtire_shock.encode('utf-8')))
    out_str_list.append(str(rtire_swingarm.encode('utf-8')))
    out_str_list.append(str(rtire_chain.encode('utf-8')))
    out_str_list.append(str(rtire_sprocket.encode('utf-8')))
    out_str_list.append(str(rtire_wheel.encode('utf-8')))
    out_str_list.append(str(rtire_brake.encode('utf-8')))
    out_str_list.append(str(rtire_tire.encode('utf-8')))
    out_str_list.append(str(denho_key.encode('utf-8')))
    out_str_list.append(str(denho_meter.encode('utf-8')))
    out_str_list.append(str(denho_blinker.encode('utf-8')))
    out_str_list.append(str(denho_right.encode('utf-8')))
    out_str_list.append(str(denho_battery.encode('utf-8')))
    out_str_list.append(str(denho_horn.encode('utf-8')))
    out_str_list.append(str(denho_brakelamp.encode('utf-8')))
    out_str_list.append(str(outer_mirror.encode('utf-8')))
    out_str_list.append(str(outer_muffler.encode('utf-8')))
    out_str_list.append(str(outer_exhaustpipe.encode('utf-8')))
    out_str_list.append(str(chassis_mainframe.encode('utf-8')))
    out_str_list.append(str(chassis_downtube.encode('utf-8')))
    out_str_list.append(str(chassis_stopper.encode('utf-8')))
    out_str_list.append(str(chassis_sheetrail.encode('utf-8')))
    out_str_list.append(str(chassis_step.encode('utf-8')))
    out_str_list.append(str(chassis_stand.encode('utf-8')))
    out_str_list.append(str(bike_no.encode('utf-8')))
    out_str_list.append(str(front_url.encode('utf-8')))
    out_str_list.append(str(back_url.encode('utf-8')))
    out_str_list.append(str(right_url.encode('utf-8')))
    out_str_list.append(str(left_url.encode('utf-8')))
    out_str_list.append(str(top_url.encode('utf-8')))
    out_str_list.append(str(bottom_url.encode('utf-8')))
    out_str_list.append(str(engin_url1.encode('utf-8')))
    out_str_list.append(str(engin_url2.encode('utf-8')))
    out_str_list.append(str(engin_url3.encode('utf-8')))
    out_str_list.append(str(engin_url4.encode('utf-8')))
    out_str_list.append(str(ftire_url1.encode('utf-8')))
    out_str_list.append(str(ftire_url2.encode('utf-8')))
    out_str_list.append(str(ftire_url3.encode('utf-8')))
    out_str_list.append(str(ftire_url4.encode('utf-8')))
    out_str_list.append(str(outer_url1.encode('utf-8')))
    out_str_list.append(str(outer_url2.encode('utf-8')))
    out_str_list.append(str(outer_url3.encode('utf-8')))
    out_str_list.append(str(outer_url4.encode('utf-8')))
    out_str_list.append(str(rtire_url1.encode('utf-8')))
    out_str_list.append(str(rtire_url2.encode('utf-8')))
    out_str_list.append(str(rtire_url3.encode('utf-8')))
    out_str_list.append(str(rtire_url4.encode('utf-8')))
    out_str_list.append(str(denho_url1.encode('utf-8')))
    out_str_list.append(str(denho_url2.encode('utf-8')))
    out_str_list.append(str(denho_url3.encode('utf-8')))
    out_str_list.append(str(denho_url4.encode('utf-8')))
    out_str_list.append(str(chassis_url1.encode('utf-8')))
    out_str_list.append(str(chassis_url2.encode('utf-8')))
    out_str_list.append(str(chassis_url3.encode('utf-8')))
    out_str_list.append(str(chassis_url4.encode('utf-8')))
    out_str_list.append(str(movie_l.encode('utf-8')))
    out_str_list.append(str(movie_r.encode('utf-8')))

    print bike_no.encode('utf-8') + '完了'

    return '"",""'.join(out_str_list)

def chrome(file_no):
    try:
        driver = webdriver.Chrome(executable_path='/usr/local/git_local/python_study/scraping/bike/etc/chromedriver')
        driver.get('http://bds.jupiter.ac/')
        driver.find_element_by_id('UserName').send_keys('81589')
        driver.find_element_by_id('Password').send_keys('ibao2002')
        driver.find_element_by_class_name('icon-hand-right').click()
        driver.find_element_by_class_name('icon-ok').click()

        # driver.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody/tr[2]/td/div[4]').click()
        # driver.find_element(By.XPATH, '//*[@id="wrap"]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody/tr[2]/td/div[4]/ul/li[1]').click()

        CB_file = '../data/url/CB1300/url_list.txt'
        with open(CB_file, 'r') as in_file:
            for line in in_file:
                values = line.rstrip().split(',')
                date = values[0]
                url = values[2]
                driver.get(url)
                try:bike_published_info = driver.find_element(By.XPATH, '//*[@id="_form"]/div/div[2]/div/table[1]/tbody/tr[1]/td[2]').text
                except: bike_published_info = ' 0 '
                bike_num = bike_published_info.split(' ')[1]

                with open('../data/output/CB1300_' + date + '.csv', 'w') as out_f:
                    out_str = ''
                    for i in range(int(bike_num)):
                        # 一覧から、物件詳細ページ遷移
                        driver.find_element(By.XPATH, '//*[@id="_form"]/div/div[2]/div/div/table/tbody/tr[' + str(i + 1) + ']/td[4]').click()
                        bike_str = get_data(driver, date)
                        str_del_brank = bike_str.replace('\n','')
                        out_str = out_str + str_del_brank + '\n'
                        driver.back()
                    out_f.write(out_str)
                print str(date) + '完了'

        """
        sum = 0
        result_dict = {}

        if file_no == '1':
            start = 2
            end = 31
            for i, hiddenId in enumerate(driver.find_elements(By.XPATH, "//input[@id='hiddenAccountId']")):
                # print i + 1, hiddenId.get_attribute('value')
                result_dict[i + 1] = hiddenId.get_attribute('value')
            for i, LikeCount in enumerate(driver.find_elements(By.XPATH, "//span[@class='recentLikeCount']")):
                # print i + 1, LikeCount.text
                result_dict[i + 1] = result_dict[i + 1] + '\t' + LikeCount.text
            for i, image in enumerate(driver.find_elements(By.XPATH, '//*[@id="main"]//*[@class="otherSexDetails"]/p/img')):
                # print i + 1, image.get_attribute('src')
                result_dict[i + 1] = result_dict[i + 1] + '\t' + image.get_attribute('src')
            sum = i + 1
        else :
            start = (int(file_no) -1) * 30
            end = int(file_no) * 30 + 1

        for page_no in range(start, end):
            time.sleep(3)
            driver.get('https://zexy-koimusubi.net/searchConditionList/paging?sort=NEW&count=30&page=' + str(page_no))
            for i, hiddenId in enumerate(driver.find_elements(By.XPATH, "//input[@id='hiddenAccountId']")):
                # print sum + i + 1, hiddenId.get_attribute('value')
                result_dict[sum + i + 1] = hiddenId.get_attribute('value')
            for i, LikeCount in enumerate(driver.find_elements(By.XPATH, "//span[@class='recentLikeCount']")):
                # print i + 1, LikeCount.text
                result_dict[sum + i + 1] = result_dict[sum + i + 1] + '\t' + LikeCount.text
            for i, image in enumerate(driver.find_elements(By.XPATH, '//*[@id="main"]//*[@class="otherSexDetails"]/p/img')):
                # print sum + i + 1, image.get_attribute('src')
                result_dict[sum + i + 1] = result_dict[sum + i + 1] + '\t' + image.get_attribute('src')
            sum = sum + i + 1

        with open('../data/result_' + file_no + '.tsv', 'w') as result:
            lines = []
            for key in result_dict.keys():
                value = result_dict[key].split('\t')
                accountid = value[0]
                like_count = value[1]
                image_url = value[2]
                lines.append(accountid + '\t' + like_count + '\t' + image_url)
                print accountid + '::' + like_count + '::' + image_url
            result.write('\n'.join(lines))
        """

    except Exception as e:
        print e
    finally:
        driver.close()

if __name__ == '__main__':
    start = time.time()
    print 'start :', start
    file_no = '1'
    # file_no = sys.argv[1]
    chrome(file_no)
    elapsed_time = time.time() - start
    print 'end :', time.time()
    print 'elapsed :', elapsed_time


