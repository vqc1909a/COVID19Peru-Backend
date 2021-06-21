const mongoose = require('mongoose');

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
  hombres: {
     type: Number,
    required:true
  },
  mujeres: {
    type: Number,
    required:true
  },
  fallecidos: {
    type: Number,
    required: true
  },
  type: {
    type: String,
    enum: ['Provincia'],
    required: true
  },
  etapa_de_vida: EtapaSchema
   
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
    hombres: {
      type: Number,
      required: true
    },
    mujeres: {
      type: Number,
      required: true
    },
    fallecidos: {
      type: Number,
      required: true
    },  
    type: {
      type: String,
      enum: ['Departamento'],
      required: true
    },
    etapa_de_vida: EtapaSchema,
    url: {
      type: String,
      require: true
    },
    provincias: [ProvinciaSchema],
    createdAt: {
      type: Date,
      default: Date.now()
    }

})


const Departamento = mongoose.model('Departamento', DepartamentoSchema );
module.exports = Departamento;