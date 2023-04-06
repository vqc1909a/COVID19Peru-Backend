
const mongoose = require('mongoose');
const meses = require("../helpers/meses");


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

const PeruSchema = new mongoose.Schema({
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
      required: true
    },
    mujeres_fallecidos: {
      type: Number,
      required: true
    },
    etapa_de_vida_fallecidos: EtapaSchema,
    fecha: {
      type: Date,
      required: true
    }
}, {
    timestamps: true,
    versionKey: false,
    minimize: false
})

const Peru = mongoose.model('Peru', PeruSchema);
module.exports = Peru;