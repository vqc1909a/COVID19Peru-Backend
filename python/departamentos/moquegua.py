import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos


poblacion_moquegua = 194613
positivos_moquegua = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "MOQUEGUA"].shape)[0]
positivos_hombres_moquegua = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "MOQUEGUA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_moquegua = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "MOQUEGUA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_moquegua = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "MOQUEGUA"].shape)[0]
fallecidos_hombres_moquegua  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MOQUEGUA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_moquegua  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MOQUEGUA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Departamento Moquegua - Etapa de vida
fallecidos_preinfancia_moquegua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_moquegua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_moquegua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_moquegua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_moquegua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_moquegua = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Moquegua-Mariscal Nieto
poblacion_moquegua_mariscal_nieto = 88491
positivos_moquegua_mariscal_nieto = list(casos_positivos[casos_positivos['PROVINCIA'] == "MARISCAL NIETO"].shape)[0]
positivos_hombres_moquegua_mariscal_nieto = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MARISCAL NIETO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_moquegua_mariscal_nieto = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MARISCAL NIETO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_moquegua_mariscal_nieto = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MARISCAL NIETO"].shape)[0]
fallecidos_hombres_moquegua_mariscal_nieto  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MARISCAL NIETO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_moquegua_mariscal_nieto  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MARISCAL NIETO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Mariscal Nieto - Etapa de vida
fallecidos_preinfancia_moquegua_mariscal_nieto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_moquegua_mariscal_nieto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_moquegua_mariscal_nieto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_moquegua_mariscal_nieto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_moquegua_mariscal_nieto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_moquegua_mariscal_nieto = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Moquegua-General Sanchez Cerro
poblacion_moquegua_general_sanchez_cerro = 29333
positivos_moquegua_general_sanchez_cerro = list(casos_positivos[casos_positivos['PROVINCIA'] == "GENERAL SANCHEZ CERRO"].shape)[0]
positivos_hombres_moquegua_general_sanchez_cerro = list(casos_positivos[(casos_positivos['PROVINCIA'] == "GENERAL SANCHEZ CERRO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_moquegua_general_sanchez_cerro = list(casos_positivos[(casos_positivos['PROVINCIA'] == "GENERAL SANCHEZ CERRO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_moquegua_general_sanchez_cerro = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "GENERAL SANCHEZ CERRO"].shape)[0]
fallecidos_hombres_moquegua_general_sanchez_cerro  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GENERAL SANCHEZ CERRO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_moquegua_general_sanchez_cerro  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GENERAL SANCHEZ CERRO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Sanchez Cerro - Etapa de vida
fallecidos_preinfancia_moquegua_general_sanchez_cerro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_moquegua_general_sanchez_cerro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_moquegua_general_sanchez_cerro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_moquegua_general_sanchez_cerro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_moquegua_general_sanchez_cerro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_moquegua_general_sanchez_cerro = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Moquegua-Ilo
poblacion_moquegua_ilo = 76789
positivos_moquegua_ilo = list(casos_positivos[casos_positivos['PROVINCIA'] == "ILO"].shape)[0]
positivos_hombres_moquegua_ilo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ILO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_moquegua_ilo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ILO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_moquegua_ilo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ILO"].shape)[0]
fallecidos_hombres_moquegua_ilo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ILO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_moquegua_ilo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ILO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Sanchez Cerro - Etapa de vida
fallecidos_preinfancia_moquegua_ilo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_moquegua_ilo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_moquegua_ilo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_moquegua_ilo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_moquegua_ilo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_moquegua_ilo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


moquegua =  {
      "name": "Moquegua",
      "poblacion": poblacion_moquegua,
      "positivos": positivos_moquegua,
      "hombres_infectados": positivos_hombres_moquegua,
      "mujeres_infectados": positivos_mujeres_moquegua,
      "fallecidos": fallecidos_moquegua,
      "hombres_fallecidos": fallecidos_hombres_moquegua,
      "mujeres_fallecidos": fallecidos_mujeres_moquegua,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_moquegua,
       "infancia": fallecidos_infancia_moquegua,
       "adolescencia": fallecidos_adolescencia_moquegua,
       "juventud": fallecidos_juventud_moquegua,
       "adultez": fallecidos_adultez_moquegua,
       "persona_mayor": fallecidos_persona_mayor_moquegua
      },
      "url": "moquegua",
      "provincias": [
          {"name": "Mariscal Nieto", "positivos": positivos_moquegua_mariscal_nieto, "poblacion": poblacion_moquegua_mariscal_nieto, "hombres_infectados": positivos_hombres_moquegua_mariscal_nieto, "mujeres_infectados": positivos_mujeres_moquegua_mariscal_nieto, "fallecidos": fallecidos_moquegua_mariscal_nieto,    "hombres_fallecidos": fallecidos_hombres_moquegua_mariscal_nieto, "mujeres_fallecidos": fallecidos_mujeres_moquegua_mariscal_nieto, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_moquegua_mariscal_nieto,
       "infancia": fallecidos_infancia_moquegua_mariscal_nieto,
       "adolescencia": fallecidos_adolescencia_moquegua_mariscal_nieto,
       "juventud": fallecidos_juventud_moquegua_mariscal_nieto,
       "adultez": fallecidos_adultez_moquegua_mariscal_nieto,
       "persona_mayor": fallecidos_persona_mayor_moquegua_mariscal_nieto
      }},

        {"name": "General Sanchez Cerro", "positivos": positivos_moquegua_general_sanchez_cerro,"poblacion": poblacion_moquegua_general_sanchez_cerro , "hombres_infectados": positivos_hombres_moquegua_general_sanchez_cerro,"mujeres_infectados": positivos_mujeres_moquegua_general_sanchez_cerro, "fallecidos": fallecidos_moquegua_general_sanchez_cerro, "hombres_fallecidos": fallecidos_hombres_moquegua_general_sanchez_cerro, "mujeres_fallecidos": fallecidos_mujeres_moquegua_general_sanchez_cerro, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_moquegua_general_sanchez_cerro,
       "infancia": fallecidos_infancia_moquegua_general_sanchez_cerro,
       "adolescencia": fallecidos_adolescencia_moquegua_general_sanchez_cerro,
       "juventud": fallecidos_juventud_moquegua_general_sanchez_cerro,
       "adultez": fallecidos_adultez_moquegua_general_sanchez_cerro,
       "persona_mayor": fallecidos_persona_mayor_moquegua_general_sanchez_cerro
      }},

        {"name": "Ilo", "positivos": positivos_moquegua_ilo,"poblacion": poblacion_moquegua_ilo , "hombres_infectados": positivos_hombres_moquegua_ilo,"mujeres_infectados": positivos_mujeres_moquegua_ilo, "fallecidos": fallecidos_moquegua_ilo, "hombres_fallecidos": fallecidos_hombres_moquegua_ilo, "mujeres_fallecidos": fallecidos_mujeres_moquegua_ilo, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_moquegua_ilo,
       "infancia": fallecidos_infancia_moquegua_ilo,
       "adolescencia": fallecidos_adolescencia_moquegua_ilo,
       "juventud": fallecidos_juventud_moquegua_ilo,
       "adultez": fallecidos_adultez_moquegua_ilo,
       "persona_mayor": fallecidos_persona_mayor_moquegua_ilo
      }}
      ]
    }
print(json.dumps(moquegua));
sys.stdout.flush();
