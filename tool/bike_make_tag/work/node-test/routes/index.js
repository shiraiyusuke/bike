/* どのURLnいリクエスト(GET or POST)が来たら何をするか(関数)を定義する場所。*/
var express = require('express');
var router = express.Router();
var moment = require('moment');
var connection = require('../mysqlConnection'); // 追加

/* GET home page. */
router.get('/', function(req, res, next) {
    var query = 'SELECT * FROM bike_result WHERE processed =0 LIMIT 4';
    connection.query(query, function(err, rows) {
        res.render('index', {
            title: 'バイク正解データ収集', /* ここでindex.ejsに渡す値をセット*/
            imageList: rows
        });
    });
});

router.post('/', function(req, res, next) {
    var table_id1 = req.body.table_img_id1;
    console.log(table_id1);
    var x_l_t1 = req.body.name_x_l_t1;
    var y_l_t1 = req.body.name_y_l_t1;
    var x_r_t1 = req.body.name_x_r_t1;
    var y_r_t1 = req.body.name_y_r_t1;
    var x_l_m1 = req.body.name_x_l_m1;
    var y_l_m1 = req.body.name_y_l_m1;
    var x_r_m1 = req.body.name_x_r_m1;
    var y_r_m1 = req.body.name_y_r_m1;
    var x_l_b1 = req.body.name_x_l_b1;
    var y_l_b1 = req.body.name_y_l_b1;
    var x_r_b1 = req.body.name_x_r_b1;
    var y_r_b1 = req.body.name_y_r_b1;
    var table_id2 = req.body.table_img_id2;
    var x_l_t2 = req.body.name_x_l_t2;
    var y_l_t2 = req.body.name_y_l_t2;
    var x_r_t2 = req.body.name_x_r_t2;
    var y_r_t2 = req.body.name_y_r_t2;
    var x_l_m2 = req.body.name_x_l_m2;
    var y_l_m2 = req.body.name_y_l_m2;
    var x_r_m2 = req.body.name_x_r_m2;
    var y_r_m2 = req.body.name_y_r_m2;
    var x_l_b2 = req.body.name_x_l_b2;
    var y_l_b2 = req.body.name_y_l_b2;
    var x_r_b2 = req.body.name_x_r_b2;
    var y_r_b2 = req.body.name_y_r_b2;
    var table_id3 = req.body.table_img_id3;
    var x_l_t3 = req.body.name_x_l_t3;
    var y_l_t3 = req.body.name_y_l_t3;
    var x_r_t3 = req.body.name_x_r_t3;
    var y_r_t3 = req.body.name_y_r_t3;
    var x_l_m3 = req.body.name_x_l_m3;
    var y_l_m3 = req.body.name_y_l_m3;
    var x_r_m3 = req.body.name_x_r_m3;
    var y_r_m3 = req.body.name_y_r_m3;
    var x_l_b3 = req.body.name_x_l_b3;
    var y_l_b3 = req.body.name_y_l_b3;
    var x_r_b3 = req.body.name_x_r_b3;
    var y_r_b3 = req.body.name_y_r_b3;
    var table_id4 = req.body.table_img_id4;
    var x_l_t4 = req.body.name_x_l_t4;
    var y_l_t4 = req.body.name_y_l_t4;
    var x_r_t4 = req.body.name_x_r_t4;
    var y_r_t4 = req.body.name_y_r_t4;
    var x_l_m4 = req.body.name_x_l_m4;
    var y_l_m4 = req.body.name_y_l_m4;
    var x_r_m4 = req.body.name_x_r_m4;
    var y_r_m4 = req.body.name_y_r_m4;
    var x_l_b4 = req.body.name_x_l_b4;
    var y_l_b4 = req.body.name_y_l_b4;
    var x_r_b4 = req.body.name_x_r_b4;
    var y_r_b4 = req.body.name_y_r_b4;
    var createdAt = moment().format('YYYY-MM-DD HH:mm:ss');

    var up1_flg = 1;
    var up2_flg = 1;
    var up3_flg = 1;
    var up4_flg = 1;

    if (y_l_t1 == 0 || x_r_t1 == 0 || y_r_t1 == 0 || x_l_m1 == 0 || y_l_m1 == 0 || x_r_m1 == 0 || y_r_m1 == 0 ||
        x_l_b1 == 0 || y_l_b1 == 0 || x_r_b1 == 0 || y_r_b1 == 0){
        up1_flg = 0;
    }
    if (y_l_t2 == 0 || x_r_t2 == 0 || y_r_t2 == 0 || x_l_m2 == 0 || y_l_m2 == 0 || x_r_m2 == 0 || y_r_m2 == 0 ||
        x_l_b2 == 0 || y_l_b2 == 0 || x_r_b2 == 0 || y_r_b2 == 0){
        up2_flg = 0;
    }
    if (y_l_t3 == 0 || x_r_t3 == 0 || y_r_t3 == 0 || x_l_m3 == 0 || y_l_m3 == 0 || x_r_m3 == 0 || y_r_m3 == 0 ||
        x_l_b3 == 0 || y_l_b3 == 0 || x_r_b3 == 0 || y_r_b3 == 0){
        up3_flg = 0;
    }
    if (y_l_t4 == 0 || x_r_t4 == 0 || y_r_t4 == 0 || x_l_m4 == 0 || y_l_m4 == 0 || x_r_m4 == 0 || y_r_m4 == 0 ||
        x_l_b4 == 0 || y_l_b4 == 0 || x_r_b4 == 0 || y_r_b4 == 0){
        up4_flg = 0;
    }

    console.log(up1_flg)
    console.log(up2_flg)
    console.log(up3_flg)
    console.log(up4_flg)

    var processed1 = 0;
    var processed2 = 0;
    var processed3 = 0;
    var processed4 = 0;

    if (up1_flg == 1) {
        processed1 = 1;
    }
    if (up2_flg == 1) {
        processed2 = 1;
    }
    if (up3_flg == 1) {
        processed3 = 1;
    }
    if (up4_flg == 1) {
        processed4 = 1;
    }

    var query1 = 'UPDATE bike_result SET processed = ' + processed1 +
        ',left_top_x =' + x_l_t1 +
        ',left_top_y =' + y_l_t1 +
        ',right_top_x =' + x_r_t1 +
        ',right_top_y =' + y_r_t1 +
        ',left_middle_x =' + x_l_m1 +
        ',left_middle_y =' + y_l_m1 +
        ',right_middle_x =' + x_r_m1 +
        ',right_middle_y =' + y_r_m1 +
        ',left_bottom_x =' + x_l_b1 +
        ',left_bottom_y =' + y_l_b1 +
        ',right_bottom_x =' + x_r_b1 +
        ',right_bottom_y =' + y_r_b1 +
        ',update_at ="' + createdAt + '"' +
        ' WHERE image_id = ' +table_id1;

    var query2 = 'UPDATE bike_result SET processed = ' + processed2 +
        ',left_top_x =' + x_l_t2 +
        ',left_top_y =' + y_l_t2 +
        ',right_top_x =' + x_r_t2 +
        ',right_top_y =' + y_r_t2 +
        ',left_middle_x =' + x_l_m2 +
        ',left_middle_y =' + y_l_m2 +
        ',right_middle_x =' + x_r_m2 +
        ',right_middle_y =' + y_r_m2 +
        ',left_bottom_x =' + x_l_b2 +
        ',left_bottom_y =' + y_l_b2 +
        ',right_bottom_x =' + x_r_b2 +
        ',right_bottom_y =' + y_r_b2 +
        ',update_at ="' + createdAt + '"' +
        ' WHERE image_id = ' + table_id2;

    var query3 = 'UPDATE bike_result SET processed = ' + processed3 +
            ',left_top_x =' + x_l_t3 +
            ',left_top_y =' + y_l_t3 +
            ',right_top_x =' + x_r_t3 +
            ',right_top_y =' + y_r_t3 +
            ',left_middle_x =' + x_l_m3 +
            ',left_middle_y =' + y_l_m3 +
            ',right_middle_x =' + x_r_m3 +
            ',right_middle_y =' + y_r_m3 +
            ',left_bottom_x =' + x_l_b3 +
            ',left_bottom_y =' + y_l_b3 +
            ',right_bottom_x =' + x_r_b3 +
            ',right_bottom_y =' + y_r_b3 +
            ',update_at ="' + createdAt + '"' +
            ' WHERE image_id = ' + table_id3;

    var query4 = 'UPDATE bike_result SET processed = ' + processed4 +
        ',left_top_x =' + x_l_t4 +
        ',left_top_y =' + y_l_t4 +
        ',right_top_x =' + x_r_t4 +
        ',right_top_y =' + y_r_t4 +
        ',left_middle_x =' + x_l_m4 +
        ',left_middle_y =' + y_l_m4 +
        ',right_middle_x =' + x_r_m4 +
        ',right_middle_y =' + y_r_m4 +
        ',left_bottom_x =' + x_l_b4 +
        ',left_bottom_y =' + y_l_b4 +
        ',right_bottom_x =' + x_r_b4 +
        ',right_bottom_y =' + y_r_b4 +
        ',update_at ="' + createdAt + '"' +
        ' WHERE image_id = ' + table_id4;


    console.log(query1);
    console.log(query2);
    console.log(query3);
    console.log(query4);

    connection.query(query1, function(err, rows) {
        console.log(err);
        connection.query(query2, function(err, rows) {
            console.log(err);
            connection.query(query3, function(err, rows) {
                console.log(err);
                connection.query(query4, function(err, rows) {
                    console.log(err);
                    res.redirect('/');
                });
            });
        });
    });

    /*
    var query = 'UPDATE bike_result SET processed = 1' +
        ',left_top_x =' + x_l_t1 +
        ',left_top_y =' + y_l_t1 +
        ',right_top_x =' + x_r_t1 +
        ',right_top_y =' + y_r_t1 +
        ',left_middle_x =' + x_l_m1 +
        ',left_middle_y =' + y_l_m1 +
        ',right_middle_x =' + x_r_m1 +
        ',right_middle_y =' + y_r_m1 +
        ',left_bottom_x =' + x_l_b1 +
        ',left_bottom_y =' + y_l_b1 +
        ',right_bottom_x =' + x_r_b1 +
        ',right_bottom_y =' + y_r_b1 +
        ',update_at ="' + createdAt + '"' +
        ' WHERE image_id = ' + table_id;
    connection.query(query, function(err, rows) {
        console.log(err);
        console.log(query);
        res.redirect('/');
    });
    */
});


router.get('/aa', function(req, res, next) {
    var query = 'SELECT count(*) FROM bike_result WHERE processed = 0';
    connection.query(query, function(err, count) {
        res.render('disp_count', {
            tag_count: count
        });
    });
});

module.exports = router;
