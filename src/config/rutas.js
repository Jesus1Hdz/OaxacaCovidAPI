const express = require('express');
const rutas = express.Router();

module.exports = app => {
    app.get('/', (req, res) => res.render('home'));

    app.use(rutas);
}