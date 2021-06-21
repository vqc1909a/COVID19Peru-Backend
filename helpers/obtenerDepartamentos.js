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

const obtenerDepartamentos = async (campos, limit = 1) => {
  const promiseLoreto = Loreto.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseAmazonas = Amazonas.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseTumbes = Tumbes.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promisePiura = Piura.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseLambayeque = Lambayeque.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseCajamarca = Cajamarca.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseLaLibertad = LaLibertad.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseAncash = Ancash.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseSanMartin = SanMartin.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseHuanuco = Huanuco.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseUcayali = Ucayali.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promisePasco = Pasco.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseLima = Lima.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseJunin = Junin.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseHuancavelica = Huancavelica.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseIca = Ica.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseAyacucho = Ayacucho.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseApurimac = Apurimac.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseCusco = Cusco.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseMadreDeDios = MadreDeDios.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promisePuno = Puno.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseArequipa = Arequipa.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseMoquegua = Moquegua.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseTacna = Tacna.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);
  const promiseCallao = Callao.find({}).limit(limit).sort({createdAt: -1}).select([...campos]);

  const departamentos = await Promise.all([promiseLoreto, promiseAmazonas, promiseTumbes, promisePiura, promiseLambayeque, promiseCajamarca, promiseLaLibertad, promiseAncash, promiseSanMartin, promiseHuanuco, promiseUcayali, promisePasco, promiseLima, promiseJunin, promiseHuancavelica, promiseIca, promiseAyacucho, promiseApurimac, promiseCusco, promiseMadreDeDios, promisePuno, promiseArequipa, promiseMoquegua, promiseTacna, promiseCallao]);

  return departamentos;
}
module.exports = obtenerDepartamentos;