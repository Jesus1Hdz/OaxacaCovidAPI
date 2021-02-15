const csvToJson = require("csvtojson");
const jsonToCSV = require("json2csv");
const fs = require("fs");

csvToJson().fromFile("covidFiltradoOaxaca.csv").then(source =>{
       
    var filtroOaxaca = source.filter(item =>{
        return item.ENTIDAD_RES === '20';
    });

    filtroOaxacaStr = JSON.stringify(filtroOaxaca);
    fs.writeFile("covidOaxaca.json", filtroOaxacaStr, function(err){
        if (err) {
        return console.log(err);
        }
        console.log("Archivo guardado");
    });
    console.log(filtroOaxaca);
});

