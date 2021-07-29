const express = require('express');
const Router = express.Router();
const obtenerDepartamentos  = require('../helpers/obtenerDepartamentos');


Router.get("/departamentos/:departamento", async (req, res, next) => {
  
  const limit = req.query.limit ? parseInt(req.query.limit.trim()) : 1;
  const depart = req.params.departamento.toLowerCase().trim()
  if(isNaN(limit) || limit < 1 || limit > 100){
   return next();
  }
  
  const [loreto, amazonas, tumbes, piura, lambayeque, cajamarca, libertad, ancash, sanmartin, huanuco, ucayali, pasco, lima, junin, huancavelica, ica, ayacucho, apurimac, cusco, madrededios, puno, arequipa, moquegua, tacna, callao] = await obtenerDepartamentos(["-provincias", "-url", "-createdAt"], limit);

  const departamentos = [loreto[0], amazonas[0], tumbes[0], piura[0], lambayeque[0], cajamarca[0], libertad[0], ancash[0], sanmartin[0], huanuco[0], ucayali[0], pasco[0], lima[0], junin[0], huancavelica[0], ica[0], ayacucho[0], apurimac[0], cusco[0], madrededios[0], puno[0], arequipa[0], moquegua[0], tacna[0], callao[0]]

  const departamento = departamentos.find(depa => depa.name.toLowerCase().trim() === depart);
  if(!departamento){
   return next();
  }
  if(limit > 1){
   switch(depart){
    case "amazonas":
     return res.status(200).json(amazonas);
    case "ancash":
     return res.status(200).json(ancash);
    case "apurimac":
     return res.status(200).json(apurimac);
    case "arequipa":
     return res.status(200).json(arequipa);
    case "ayacucho":
     return res.status(200).json(ayacucho);
    case "cajamarca":
     return res.status(200).json(cajamarca);
    case "callao":
     return res.status(200).json(callao);
    case "cusco":
     return res.status(200).json(cusco);
    case "huancavelica":
     return res.status(200).json(huancavelica);
    case "huanuco":
     return res.status(200).json(huanuco);
    case "ica":
     return res.status(200).json(ica);
    case "junin":
     return res.status(200).json(junin);
    case "la libertad":
     return res.status(200).json(libertad);
    case "lambayeque":
     return res.status(200).json(lambayeque);
    case "lima":
     return res.status(200).json(lima);
    case "loreto":
     return res.status(200).json(loreto);
    case "madre de dios":
     return res.status(200).json(madrededios);
    case "moquegua":
     return res.status(200).json(moquegua);
    case "pasco":
     return res.status(200).json(pasco);
    case "piura":
     return res.status(200).json(piura);
    case "puno":
     return res.status(200).json(puno);
    case "san martin":
     return res.status(200).json(sanmartin);
    case "tacna":
     return res.status(200).json(tacna);
    case "tumbes":
     return res.status(200).json(tumbes);
    case "ucayali":
     return res.status(200).json(ucayali);

    default :
     return next();
   }
  }

  return res.status(200).json(departamento);

})

Router.get("/departamentos/random", async (req, res, next) => {
  const [loreto, amazonas, tumbes, piura, lambayeque, cajamarca, libertad, ancash, sanmartin, huanuco, ucayali, pasco, lima, junin, huancavelica, ica, ayacucho, apurimac, cusco, madrededios, puno, arequipa, moquegua, tacna, callao] = await obtenerDepartamentos(["-provincias", "-url", "-createdAt"]);

  const departamentos = [loreto[0], amazonas[0], tumbes[0], piura[0], lambayeque[0], cajamarca[0], libertad[0], ancash[0], sanmartin[0], huanuco[0], ucayali[0], pasco[0], lima[0], junin[0], huancavelica[0], ica[0], ayacucho[0], apurimac[0], cusco[0], madrededios[0], puno[0], arequipa[0], moquegua[0], tacna[0], callao[0]]

  const numero_aleatorio = Math.floor(Math.random() * 24);

  const departamento = departamentos[numero_aleatorio];
  if(!departamento){
   return next();
  }
  return res.status(200).json(departamento);

})


module.exports = Router;
