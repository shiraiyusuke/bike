/**
 * Created by shirai on 2016/12/25.
 */
var mysql = require('mysql');

var dbConfig = {
    host: '127.0.0.1',
    user: 'root',
    password: '',
    database: 'bike'
};

var connection = mysql.createConnection(dbConfig);

module.exports = connection;
