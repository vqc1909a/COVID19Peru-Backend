import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_piura = 2085441
positivos_piura = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "PIURA"].shape)[0]
positivos_hombres_piura = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PIURA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_piura = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PIURA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_piura = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "PIURA"].shape)[0]
fallecidos_hombres_piura  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_piura  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Departamento Piura - Etapa de vida
fallecidos_preinfancia_piura = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincias Piura
#!Piura-Piura
poblacion_piura_piura = 870137
positivos_piura_piura = list(casos_positivos[casos_positivos['PROVINCIA'] == "PIURA"].shape)[0]
positivos_hombres_piura_piura = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PIURA")].shape)[0]
positivos_mujeres_piura_piura = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PIURA")].shape)[0]
fallecidos_piura_piura = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PIURA"].shape)[0]
fallecidos_hombres_piura_piura  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_piura_piura  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Piura - Etapa de vida
fallecidos_preinfancia_piura_piura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_piura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_piura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_piura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_piura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_piura = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Piura-Ayabaca
poblacion_piura_ayabaca = 154083
positivos_piura_ayabaca = list(casos_positivos[casos_positivos['PROVINCIA'] == "AYABACA"].shape)[0]
positivos_hombres_piura_ayabaca = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "AYABACA")].shape)[0]
positivos_mujeres_piura_ayabaca = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "AYABACA")].shape)[0]
fallecidos_piura_ayabaca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "AYABACA"].shape)[0]
fallecidos_hombres_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Ayabaca - Etapa de vida
fallecidos_preinfancia_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_ayabaca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Piura-Huancambamba
poblacion_piura_huancabamba = 140066
positivos_piura_huancabamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUANCABAMBA"].shape)[0]
positivos_hombres_piura_huancabamba = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUANCABAMBA")].shape)[0]
positivos_mujeres_piura_huancabamba = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUANCABAMBA")].shape)[0]
fallecidos_piura_huancabamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUANCABAMBA"].shape)[0]
fallecidos_hombres_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Huancambamba - Etapa de vida
fallecidos_preinfancia_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_huancabamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Piura-Morropon
poblacion_piura_morropon = 178381
positivos_piura_morropon = list(casos_positivos[casos_positivos['PROVINCIA'] == "MORROPON"].shape)[0]
positivos_hombres_piura_morropon = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "MORROPON")].shape)[0]
positivos_mujeres_piura_morropon = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "MORROPON")].shape)[0]
fallecidos_piura_morropon = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MORROPON"].shape)[0]
fallecidos_hombres_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Morropon - Etapa de vida
fallecidos_preinfancia_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_morropon = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Piura-Paita
poblacion_piura_paita = 145085
positivos_piura_paita = list(casos_positivos[casos_positivos['PROVINCIA'] == "PAITA"].shape)[0]
positivos_hombres_piura_paita = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PAITA")].shape)[0]
positivos_mujeres_piura_paita = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PAITA")].shape)[0]
fallecidos_piura_paita = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PAITA"].shape)[0]
fallecidos_hombres_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Morropon - Etapa de vida
fallecidos_preinfancia_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_paita = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Piura-Sullana
poblacion_piura_sullana = 358893
positivos_piura_sullana = list(casos_positivos[casos_positivos['PROVINCIA'] == "SULLANA"].shape)[0]
positivos_hombres_piura_sullana = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SULLANA")].shape)[0]
positivos_mujeres_piura_sullana = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SULLANA")].shape)[0]
fallecidos_piura_sullana = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SULLANA"].shape)[0]
fallecidos_hombres_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Sullana - Etapa de vida
fallecidos_preinfancia_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_sullana = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Piura-Talara
poblacion_piura_talara = 153209
positivos_piura_talara = list(casos_positivos[casos_positivos['PROVINCIA'] == "TALARA"].shape)[0]
positivos_hombres_piura_talara = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "TALARA")].shape)[0]
positivos_mujeres_piura_talara = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "TALARA")].shape)[0]
fallecidos_piura_talara = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TALARA"].shape)[0]
fallecidos_hombres_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Talara - Etapa de vida
fallecidos_preinfancia_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_talara = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Sechura
poblacion_piura_sechura = 85587
positivos_piura_sechura = list(casos_positivos[casos_positivos['PROVINCIA'] == "SECHURA"].shape)[0]
positivos_hombres_piura_sechura = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SECHURA")].shape)[0]
positivos_mujeres_piura_sechura = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SECHURA")].shape)[0]
fallecidos_piura_sechura = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SECHURA"].shape)[0]
fallecidos_hombres_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Sechura - Etapa de vida
fallecidos_preinfancia_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_sechura = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

    
piura =  {
      "name": "Piura",
      "poblacion": poblacion_piura,
      "positivos": positivos_piura,
      "hombres_infectados": positivos_hombres_piura,
      "mujeres_infectados": positivos_mujeres_piura,
      "fallecidos": fallecidos_piura,
      "hombres_fallecidos": fallecidos_hombres_piura,
      "mujeres_fallecidos": fallecidos_mujeres_piura,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura,
       "infancia": fallecidos_infancia_piura,
       "adolescencia": fallecidos_adolescencia_piura,
       "juventud": fallecidos_juventud_piura,
       "adultez": fallecidos_adultez_piura,
       "persona_mayor": fallecidos_persona_mayor_piura
      },
      "url": "piura",
      "provincias": [
          {"name": "Piura", "positivos": positivos_piura_piura,"poblacion": poblacion_piura_piura,"hombres_infectados": positivos_hombres_piura_piura,"mujeres_infectados": positivos_mujeres_piura_piura, "fallecidos": fallecidos_piura_piura, "hombres_fallecidos": fallecidos_hombres_piura_piura, "mujeres_fallecidos": fallecidos_mujeres_piura_piura, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_piura,
       "infancia": fallecidos_infancia_piura_piura,
       "adolescencia": fallecidos_adolescencia_piura_piura,
       "juventud": fallecidos_juventud_piura_piura,
       "adultez": fallecidos_adultez_piura_piura,
       "persona_mayor": fallecidos_persona_mayor_piura_piura
      }},

          {"name": "Ayabaca", "positivos": positivos_piura_ayabaca,"poblacion": poblacion_piura_ayabaca,"hombres_infectados": positivos_hombres_piura_ayabaca,"mujeres_infectados": positivos_mujeres_piura_ayabaca, "fallecidos": fallecidos_piura_ayabaca, "hombres_fallecidos": fallecidos_hombres_piura_ayabaca, "mujeres_fallecidos": fallecidos_mujeres_piura_ayabaca, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_ayabaca,
       "infancia": fallecidos_infancia_piura_ayabaca,
       "adolescencia": fallecidos_adolescencia_piura_ayabaca,
       "juventud": fallecidos_juventud_piura_ayabaca,
       "adultez": fallecidos_adultez_piura_ayabaca,
       "persona_mayor": fallecidos_persona_mayor_piura_ayabaca
      }},

          {"name": "Huancabamba", "positivos": positivos_piura_huancabamba,"poblacion": poblacion_piura_huancabamba,"hombres_infectados": positivos_hombres_piura_huancabamba,"mujeres_infectados": positivos_mujeres_piura_huancabamba, "fallecidos": fallecidos_piura_huancabamba, "hombres_fallecidos": fallecidos_hombres_piura_huancabamba, "mujeres_fallecidos": fallecidos_mujeres_piura_huancabamba, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_huancabamba,
       "infancia": fallecidos_infancia_piura_huancabamba,
       "adolescencia": fallecidos_adolescencia_piura_huancabamba,
       "juventud": fallecidos_juventud_piura_huancabamba,
       "adultez": fallecidos_adultez_piura_huancabamba,
       "persona_mayor": fallecidos_persona_mayor_piura_huancabamba
      }},

          {"name": "Morropon", "positivos": positivos_piura_morropon, "poblacion": poblacion_piura_morropon, "hombres_infectados": positivos_hombres_piura_morropon, "mujeres_infectados": positivos_mujeres_piura_morropon, "fallecidos": fallecidos_piura_morropon, "hombres_fallecidos": fallecidos_hombres_piura_morropon, "mujeres_fallecidos": fallecidos_mujeres_piura_morropon, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_morropon,
       "infancia": fallecidos_infancia_piura_morropon,
       "adolescencia": fallecidos_adolescencia_piura_morropon,
       "juventud": fallecidos_juventud_piura_morropon,
       "adultez": fallecidos_adultez_piura_morropon,
       "persona_mayor": fallecidos_persona_mayor_piura_morropon
      }},

          {"name": "Paita", "positivos": positivos_piura_paita,"poblacion": poblacion_piura_paita,"hombres_infectados": positivos_hombres_piura_paita,"mujeres_infectados": positivos_mujeres_piura_paita, "fallecidos": fallecidos_piura_paita, "hombres_fallecidos": fallecidos_hombres_piura_paita, "mujeres_fallecidos": fallecidos_mujeres_piura_paita, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_paita,
       "infancia": fallecidos_infancia_piura_paita,
       "adolescencia": fallecidos_adolescencia_piura_paita,
       "juventud": fallecidos_juventud_piura_paita,
       "adultez": fallecidos_adultez_piura_paita,
       "persona_mayor": fallecidos_persona_mayor_piura_paita
      }},

          {"name": "Sullana", "positivos": positivos_piura_sullana,"poblacion": poblacion_piura_sullana,"hombres_infectados": positivos_hombres_piura_sullana,"mujeres_infectados": positivos_mujeres_piura_sullana, "fallecidos": fallecidos_piura_sullana, "hombres_fallecidos": fallecidos_hombres_piura_sullana, "mujeres_fallecidos": fallecidos_mujeres_piura_sullana, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_sullana,
       "infancia": fallecidos_infancia_piura_sullana,
       "adolescencia": fallecidos_adolescencia_piura_sullana,
       "juventud": fallecidos_juventud_piura_sullana,
       "adultez": fallecidos_adultez_piura_sullana,
       "persona_mayor": fallecidos_persona_mayor_piura_sullana
      }},

          {"name": "Talara", "positivos": positivos_piura_talara,"poblacion": poblacion_piura_talara,"hombres_infectados": positivos_hombres_piura_talara,"mujeres_infectados": positivos_mujeres_piura_talara, "fallecidos": fallecidos_piura_talara, "hombres_fallecidos": fallecidos_hombres_piura_talara, "mujeres_fallecidos": fallecidos_mujeres_piura_talara, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_talara,
       "infancia": fallecidos_infancia_piura_talara,
       "adolescencia": fallecidos_adolescencia_piura_talara,
       "juventud": fallecidos_juventud_piura_talara,
       "adultez": fallecidos_adultez_piura_talara,
       "persona_mayor": fallecidos_persona_mayor_piura_talara
      }},

          {"name": "Sechura", "positivos": positivos_piura_sechura,"poblacion": poblacion_piura_sechura, "hombres_infectados": positivos_hombres_piura_sechura,"mujeres_infectados": positivos_mujeres_piura_sechura, "fallecidos": fallecidos_piura_sechura, "hombres_fallecidos": fallecidos_hombres_piura_sechura, "mujeres_fallecidos": fallecidos_mujeres_piura_sechura, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_sechura,
       "infancia": fallecidos_infancia_piura_sechura,
       "adolescencia": fallecidos_adolescencia_piura_sechura,
       "juventud": fallecidos_juventud_piura_sechura,
       "adultez": fallecidos_adultez_piura_sechura,
       "persona_mayor": fallecidos_persona_mayor_piura_sechura
      }}
      ]
    }
    
print(json.dumps(piura))
sys.stdout.flush();
