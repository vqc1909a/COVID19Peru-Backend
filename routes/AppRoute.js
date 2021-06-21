//! Apis de las Vistas Inicio, Explorar y Mapa 
const express = require('express');
const Peru = require('../models/PeruModel');
const {
  Loreto,
  Amazonas,
  Tumbes,
  Piura,
  Lambayeque,
  Cajamarca,
  LaLibertad,
  Ancash,
  SanMartin,
  Huanuco,
  Ucayali,
  Pasco,
  Lima,
  Junin,
  Huancavelica,
  Ica,
  Ayacucho,
  Apurimac,
  Cusco,
  MadreDeDios,
  Puno,
  Arequipa,
  Moquegua,
  Tacna,
  Callao} = require('../models/RegionModel');

const Router = express.Router();

Router.get('/peru', async (req, res) => {
  const peru = await Peru.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(peru[0]);
})

Router.get('/departamento/loreto', async (req, res) => {
  const loreto = await Loreto.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(loreto[0]);
})

Router.get('/departamento/amazonas', async (req, res) => {
  const amazonas = await Amazonas.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(amazonas[0]);
})

Router.get('/departamento/tumbes', async (req, res) => {
  const tumbes = await Tumbes.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(tumbes[0]);
})

Router.get('/departamento/piura', async (req, res) => {
  const piura = await Piura.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(piura[0]);
})

Router.get('/departamento/lambayeque', async (req, res) => {
  const lambayeque = await Lambayeque.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(lambayeque[0]);
})

Router.get('/departamento/cajamarca', async (req, res) => {
  const cajamarca = await Cajamarca.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(cajamarca[0]);
})

Router.get('/departamento/la-libertad', async (req, res) => {
  const lalibertad = await LaLibertad.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(lalibertad[0]);
})

Router.get('/departamento/ancash', async (req, res) => {
  const ancash = await Ancash.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(ancash[0]);
})

Router.get('/departamento/san-martin', async (req, res) => {
  const sanmartin = await SanMartin.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(sanmartin[0]);
})

Router.get('/departamento/huanuco', async (req, res) => {
  const huanuco = await Huanuco.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(huanuco[0]);
})

Router.get('/departamento/ucayali', async (req, res) => {
  const ucayali = await Ucayali.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(ucayali[0]);
})

Router.get('/departamento/pasco', async (req, res) => {
  const pasco = await Pasco.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(pasco[0]);
})

Router.get('/departamento/lima', async (req, res) => {
  const lima = await Lima.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(lima[0]);
})

Router.get('/departamento/junin', async (req, res) => {
  const junin = await Junin.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(junin[0]);
})

Router.get('/departamento/huancavelica', async (req, res) => {
  const huancavelica = await Huancavelica.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(huancavelica[0]);
})

Router.get('/departamento/ica', async (req, res) => {
  const ica = await Ica.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(ica[0]);
})

Router.get('/departamento/ayacucho', async (req, res) => {
  const ayacucho = await Ayacucho.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(ayacucho[0]);
})

Router.get('/departamento/apurimac', async (req, res) => {
  const apurimac = await Apurimac.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(apurimac[0]);
})

Router.get('/departamento/cusco', async (req, res) => {
  const cusco = await Cusco.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(cusco[0]);
})

Router.get('/departamento/madre-de-dios', async (req, res) => {
  const madrededios = await MadreDeDios.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(madrededios[0]);
})

Router.get('/departamento/puno', async (req, res) => {
  const puno = await Puno.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(puno[0]);
})

Router.get('/departamento/arequipa', async (req, res) => {
  const arequipa = await Arequipa.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(arequipa[0]);
})

Router.get('/departamento/moquegua', async (req, res) => {
  const moquegua = await Moquegua.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(moquegua[0]);
})

Router.get('/departamento/tacna', async (req, res) => {
  const tacna = await Tacna.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(tacna[0]);
})

Router.get('/departamento/callao', async (req, res) => {
  const callao = await Callao.find({}).limit(1).sort({createdAt: -1});
  return res.status(200).json(callao[0]);
})

module.exports = Router