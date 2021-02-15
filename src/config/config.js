const express = require('express');
const path = require('path');
const rutas = require('./rutas');

module.exports = app => {

    var app = express();
    app.set('port', process.env.PORT || 5700);
    app.set('views', path.join(__dirname, '../views'));
    app.set('view engine', 'pug');

    // Archivos estáticos
    app.use('/public',express.static(path.join(__dirname, '../public')));

    // rutas
    rutas(app);

    return app;
}