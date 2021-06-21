const mongoose = require('mongoose');
const meses  = require("../helpers/meses");


const EtapaSchema = new mongoose.Schema({
  primera_infancia: {
    type: Number,
    required:true
  },
  infancia: {
    type: Number,
    required:true
  },
  adolescencia: {
    type: Number,
    required:true
  },
  juventud: {
    type: Number,
    required:true
  },
  adultez: {
    type: Number,
    required:true
  },
  persona_mayor: {
    type: Number,
    required:true
  }
});

const ProvinciaSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  positivos: {
    type: Number,
    required:true
  },
  poblacion: {
    type: Number,
    required:true
  },
  hombres_infectados: {
     type: Number,
    required:true
  },
  mujeres_infectados: {
    type: Number,
    required:true
  },
  fallecidos: {
    type: Number,
    required: true
  },
  hombres_fallecidos: {
    type: Number,
    required:true
  },
  mujeres_fallecidos: {
    type: Number,
    required:true
  },
  type: {
    type: String,
    enum: ['Provincia'],
    required: true
  },
  etapa_de_vida_fallecidos: EtapaSchema,
  fecha: {
    type: Number,
    default: new Date().getFullYear()
  },
  mes: {
    type: String,
    default: meses[new Date().getMonth()]
  },
  dia: {
    type: Number,
    default: new Date().getDate()
  } 
})

const DepartamentoSchema = new mongoose.Schema({
    name: {
      type: String,
      required: true,
    },
    poblacion: {
      type: Number,
      required: true
    },
    positivos: {
      type: Number,
      required: true
    },
    hombres_infectados: {
      type: Number,
      required: true
    },
    mujeres_infectados: {
      type: Number,
      required: true
    },
    fallecidos: {
      type: Number,
      required: true
    },  
    hombres_fallecidos: {
      type: Number,
      required:true
    },
    mujeres_fallecidos: {
      type: Number,
      required:true
    },
    type: {
      type: String,
      enum: ['Departamento'],
      required: true
    },
    etapa_de_vida_fallecidos: EtapaSchema,
    url: {
      type: String,
      require: true
    },
    provincias: [ProvinciaSchema],
    createdAt: {
      type: Date,
      default: Date.now()
    },
    fecha: Number,
    mes: String,
    dia: Number
})


DepartamentoSchema.pre("save", function(next){
  const data = new Date(`${this.createdAt}`);
  this.fecha = data.getFullYear();
  this.mes = meses[data.getMonth()];
  this.dia = data.getDate();
  next()
})

const Loreto = mongoose.model('Loreto', DepartamentoSchema);
const Amazonas = mongoose.model('Amazonas', DepartamentoSchema);
const Tumbes = mongoose.model('Tumbes', DepartamentoSchema);
const Piura = mongoose.model('Piura', DepartamentoSchema);
const Lambayeque = mongoose.model('Lambayeque', DepartamentoSchema);
const Cajamarca = mongoose.model('Cajamarca', DepartamentoSchema);
const LaLibertad = mongoose.model('LaLibertad', DepartamentoSchema);
const Ancash = mongoose.model('Ancash', DepartamentoSchema);
const SanMartin = mongoose.model('SanMartin', DepartamentoSchema);
const Huanuco = mongoose.model('Huanuco', DepartamentoSchema);
const Ucayali = mongoose.model('Ucayali', DepartamentoSchema);
const Pasco = mongoose.model('Pasco', DepartamentoSchema);
const Lima = mongoose.model('Lima', DepartamentoSchema);
const Junin = mongoose.model('Junin', DepartamentoSchema);
const Huancavelica = mongoose.model('Huancavelica', DepartamentoSchema);
const Ica = mongoose.model('Ica', DepartamentoSchema);
const Ayacucho = mongoose.model('Ayacucho', DepartamentoSchema);
const Apurimac = mongoose.model('Apurimac', DepartamentoSchema);
const Cusco = mongoose.model('Cusco', DepartamentoSchema);
const MadreDeDios = mongoose.model('MadreDeDios', DepartamentoSchema);
const Puno = mongoose.model('Puno', DepartamentoSchema);
const Arequipa = mongoose.model('Arequipa', DepartamentoSchema);
const Moquegua = mongoose.model('Moquegua', DepartamentoSchema);
const Tacna = mongoose.model('Tacna', DepartamentoSchema);
const Callao = mongoose.model('Callao', DepartamentoSchema);

module.exports = {
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
  Callao
}






















