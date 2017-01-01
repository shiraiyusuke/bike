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
    var table_id = req.body.img_table_id;
    var x_l_t = req.body.name_x_l_t1;
    var y_l_t = req.body.name_y_l_t1;
    var x_r_t = req.body.name_x_r_t1;
    var y_r_t = req.body.name_y_r_t1;
    var x_l_m = req.body.name_x_l_m1;
    var y_l_m = req.body.name_y_l_m1;
    var x_r_m = req.body.name_x_r_m1;
    var y_r_m = req.body.name_y_r_m1;
    var x_l_b = req.body.name_x_l_b1;
    var y_l_b = req.body.name_y_l_b1;
    var x_r_b = req.body.name_x_r_b1;
    var y_r_b = req.body.name_y_r_b1;
    var createdAt = moment().format('YYYY-MM-DD HH:mm:ss');

    var query = 'UPDATE bike_result SET processed = 1' +
        ',left_top_x =' + x_l_t +
        ',left_top_y =' + y_l_t +
        ',right_top_x =' + x_r_t +
        ',right_top_y =' + y_r_t +
        ',left_middle_x =' + x_l_m +
        ',left_middle_y =' + y_l_m +
        ',right_middle_x =' + x_r_m +
        ',right_middle_y =' + y_r_m +
        ',left_bottom_x =' + x_l_b +
        ',left_bottom_y =' + y_l_b +
        ',right_bottom_x =' + x_r_b +
        ',right_bottom_y =' + y_r_b +
        ',update_at ="' + createdAt + '"' +
        ' WHERE image_id = ' +table_id;

/*    var query = 'UPDATE bike_result SET ' +
        'processed = 1' +
        ',left_top_x =' + x_l_t +
        ',left_top_y =' + y_l_t +
        ',right_top_x =' + x_r_t +
        ',right_top_y =' + y_r_t +
        ',left_middle_x =' + x_l_m +
        ',left_middle_y =' + y_l_m +
        ',right_middle_x =' + x_r_m +
        ',right_middle_y =' + y_r_m +
        ',left_bottom_x =' + x_l_b +
        ',left_bottom_y =' + y_l_b +
        ',right_bottom_x =' + x_r_b +
        ',right_bottom_y =' + y_r_b +
        ',update_at ="' + createdAt+ '"'
        ' WHERE id = '+ parseInt(id);*/
    //var query = 'INSERT INTO boards (title, created_at) VALUES ("' + title + '", ' + '"' + createdAt + '")';
    connection.query(query, function(err, rows) {
        res.redirect('/');
    });
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
