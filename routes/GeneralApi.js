const express = require('express');
const Router = express.Router();
const obtenerDepartamentos  = require('../helpers/obtenerDepartamentos');
const Peru = require('../models/PeruModel');


Router.get("/", async (req, res) => {
  return res.status(200).json({
    "nacional": `${req.protocol}://${req.headers.host}/api/pais`,
    "departamentos": `${req.protocol}://${req.headers.host}/api/departamentos`,
    "provincias": `${req.protocol}://${req.headers.host}/api/provincias`
  })
})

Router.get("/departamentos", async (req, res) => {

  const [loreto, amazonas, tumbes, piura, lambayeque, cajamarca, libertad, ancash, sanmartin, huanuco, ucayali, pasco, lima, junin, huancavelica, ica, ayacucho, apurimac, cusco, madrededios, puno, arequipa, moquegua, tacna, callao] = await obtenerDepartamentos(["-provincias", "-url", "-createdAt"]);

  const departamentos = [loreto[0], amazonas[0], tumbes[0], piura[0], lambayeque[0], cajamarca[0], libertad[0], ancash[0], sanmartin[0], huanuco[0], ucayali[0], pasco[0], lima[0], junin[0], huancavelica[0], ica[0], ayacucho[0], apurimac[0], cusco[0], madrededios[0], puno[0], arequipa[0], moquegua[0], tacna[0], callao[0]]
  return res.status(200).json(departamentos);
})

Router.get("/provincias", async (req, res) => {
 
  const [loreto, amazonas, tumbes, piura, lambayeque, cajamarca, libertad, ancash, sanmartin, huanuco, ucayali, pasco, lima, junin, huancavelica, ica, ayacucho, apurimac, cusco, madrededios, puno, arequipa, moquegua, tacna, callao] = await obtenerDepartamentos(["provincias"]);

  const provincias = [...loreto[0].provincias, ...amazonas[0].provincias, ...tumbes[0].provincias, ...piura[0].provincias, ...lambayeque[0].provincias, ...cajamarca[0].provincias, ...libertad[0].provincias, ...ancash[0].provincias, ...sanmartin[0].provincias, ...huanuco[0].provincias, ...ucayali[0].provincias, ...pasco[0].provincias, ...lima[0].provincias, ...junin[0].provincias, ...huancavelica[0].provincias, ...ica[0].provincias, ...ayacucho[0].provincias, ...apurimac[0].provincias, ...cusco[0].provincias, ...madrededios[0].provincias, ...puno[0].provincias, ...arequipa[0].provincias, ...moquegua[0].provincias, ...tacna[0].provincias, ...callao[0].provincias]

  return res.status(200).json(provincias);
})

Router.get('/pais', async (req, res, next) => {
  const limit = req.query.limit ? parseInt(req.query.limit) : 1;
  if(isNaN(limit) || limit < 1 || limit > 100){
   return next();
  }
  const nacional = await Peru.find({}).limit(limit).sort({createdAt: -1}).select(["-mapa_hijos", "-createdAt"]);

  if(limit > 1){
    return res.status(200).json(nacional);
  }
  return res.status(200).json(nacional[0]);
})

module.exports = Router;