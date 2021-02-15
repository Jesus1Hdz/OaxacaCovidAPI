const express = require('express');
const config = require('./src/config/config');

const app = config(express());

app.listen(app.get('port'), function(){
    console.log('Server running in port ', app.get('port'));
});