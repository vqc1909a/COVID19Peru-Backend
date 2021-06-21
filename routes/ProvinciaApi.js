const express = require('express');
const Router = express.Router();
const obtenerDepartamentos  = require('../helpers/obtenerDepartamentos');


Router.get("/provincias/:provincia", async (req, res, next) => {
  
  const prov = req.params.provincia.toLowerCase().trim();
  const [loreto, amazonas, tumbes, piura, lambayeque, cajamarca, libertad, ancash, sanmartin, huanuco, ucayali, pasco, lima, junin, huancavelica, ica, ayacucho, apurimac, cusco, madrededios, puno, arequipa, moquegua, tacna, callao] = await obtenerDepartamentos(["provincias"]);

  const provincias = [...loreto[0].provincias, ...amazonas[0].provincias, ...tumbes[0].provincias, ...piura[0].provincias, ...lambayeque[0].provincias, ...cajamarca[0].provincias, ...libertad[0].provincias, ...ancash[0].provincias, ...sanmartin[0].provincias, ...huanuco[0].provincias, ...ucayali[0].provincias, ...pasco[0].provincias, ...lima[0].provincias, ...junin[0].provincias, ...huancavelica[0].provincias, ...ica[0].provincias, ...ayacucho[0].provincias, ...apurimac[0].provincias, ...cusco[0].provincias, ...madrededios[0].provincias, ...puno[0].provincias, ...arequipa[0].provincias, ...moquegua[0].provincias, ...tacna[0].provincias, ...callao[0].provincias]

  const provincia = provincias.find(provi => provi.name.toLowerCase().trim() === prov);
  if(!provincia){
   return next();
  }
  return res.status(200).json(provincia);

})


Router.get("/provincias/random", async (req, res, next) => {
  const [loreto, amazonas, tumbes, piura, lambayeque, cajamarca, libertad, ancash, sanmartin, huanuco, ucayali, pasco, lima, junin, huancavelica, ica, ayacucho, apurimac, cusco, madrededios, puno, arequipa, moquegua, tacna, callao] = await obtenerDepartamentos(["provincias"]);

  const provincias = [...loreto[0].provincias, ...amazonas[0].provincias, ...tumbes[0].provincias, ...piura[0].provincias, ...lambayeque[0].provincias, ...cajamarca[0].provincias, ...libertad[0].provincias, ...ancash[0].provincias, ...sanmartin[0].provincias, ...huanuco[0].provincias, ...ucayali[0].provincias, ...pasco[0].provincias, ...lima[0].provincias, ...junin[0].provincias, ...huancavelica[0].provincias, ...ica[0].provincias, ...ayacucho[0].provincias, ...apurimac[0].provincias, ...cusco[0].provincias, ...madrededios[0].provincias, ...puno[0].provincias, ...arequipa[0].provincias, ...moquegua[0].provincias, ...tacna[0].provincias, ...callao[0].provincias]

  const numero_aleatorio = Math.floor(Math.random() * 193);

  const provincia = provincias[numero_aleatorio];
  if(!provincia){
   return next();
  }
  return res.status(200).json(provincia);

})

module.exports = Router;
