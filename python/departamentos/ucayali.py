import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_ucayali = 606081
positivos_ucayali = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "UCAYALI"].shape)[0]
positivos_hombres_ucayali = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "UCAYALI") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ucayali = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "UCAYALI") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ucayali = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "UCAYALI"].shape)[0]
fallecidos_hombres_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (
    casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (
    casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Departamento Ucayali - Etapa de vida
fallecidos_preinfancia_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ucayali = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Ucayali
#!Ucayali-Coronel Portillo
poblacion_ucayali_coronel_portillo = 460293
positivos_ucayali_coronel_portillo = list(casos_positivos[casos_positivos['PROVINCIA'] == "CORONEL PORTILLO"].shape)[0]
positivos_hombres_ucayali_coronel_portillo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ucayali_coronel_portillo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ucayali_coronel_portillo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO"].shape)[0]
fallecidos_hombres_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Coronel Portillo - Etapa de vida
fallecidos_preinfancia_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ucayali_coronel_portillo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Atalaya
poblacion_ucayali_atalaya = 66950
positivos_ucayali_atalaya = list(casos_positivos[casos_positivos['PROVINCIA'] == "ATALAYA"].shape)[0]
positivos_hombres_ucayali_atalaya = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ATALAYA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ucayali_atalaya = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ATALAYA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ucayali_atalaya = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ATALAYA"].shape)[0]
fallecidos_hombres_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Coronel Portillo - Etapa de vida
fallecidos_preinfancia_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ucayali_atalaya = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Padre Abad
poblacion_ucayali_padre_abad = 73662
positivos_ucayali_padre_abad = list(casos_positivos[casos_positivos['PROVINCIA'] == "PADRE ABAD"].shape)[0]
positivos_hombres_ucayali_padre_abad = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PADRE ABAD") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ucayali_padre_abad = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PADRE ABAD") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ucayali_padre_abad = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PADRE ABAD"].shape)[0]
fallecidos_hombres_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Padre Abad - Etapa de vida
fallecidos_preinfancia_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ucayali_padre_abad = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Purus
poblacion_ucayali_purus = 5176
positivos_ucayali_purus = list(casos_positivos[casos_positivos['PROVINCIA'] == "PURUS"].shape)[0]
positivos_hombres_ucayali_purus = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PURUS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ucayali_purus = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PURUS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ucayali_purus = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PURUS"].shape)[0]
fallecidos_hombres_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Purus - Etapa de vida
fallecidos_preinfancia_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ucayali_purus = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


ucayali =  {
      "name": "Ucayali",
      "poblacion": poblacion_ucayali,
      "positivos": positivos_ucayali,
      "hombres_infectados": positivos_hombres_ucayali,
      "mujeres_infectados": positivos_mujeres_ucayali,
      "fallecidos": fallecidos_ucayali,
      "hombres_fallecidos": fallecidos_hombres_ucayali,
      "mujeres_fallecidos": fallecidos_mujeres_ucayali,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ucayali,
       "infancia": fallecidos_infancia_ucayali,
       "adolescencia": fallecidos_adolescencia_ucayali,
       "juventud": fallecidos_juventud_ucayali,
       "adultez": fallecidos_adultez_ucayali,
       "persona_mayor": fallecidos_persona_mayor_ucayali
      },
      "url": "ucayali",
      "provincias": [
          {"name": "Coronel Portillo", "positivos": positivos_ucayali_coronel_portillo,"poblacion": poblacion_ucayali_coronel_portillo , "hombres_infectados": positivos_hombres_ucayali_coronel_portillo,"mujeres_infectados": positivos_mujeres_ucayali_coronel_portillo, "fallecidos": fallecidos_ucayali_coronel_portillo, "hombres_fallecidos": fallecidos_hombres_ucayali_coronel_portillo, "mujeres_fallecidos": fallecidos_mujeres_ucayali_coronel_portillo, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ucayali_coronel_portillo,
       "infancia": fallecidos_infancia_ucayali_coronel_portillo,
       "adolescencia": fallecidos_adolescencia_ucayali_coronel_portillo,
       "juventud": fallecidos_juventud_ucayali_coronel_portillo,
       "adultez": fallecidos_adultez_ucayali_coronel_portillo,
       "persona_mayor": fallecidos_persona_mayor_ucayali_coronel_portillo
      }},

          {"name": "Atalaya", "positivos": positivos_ucayali_atalaya, "poblacion": poblacion_ucayali_atalaya, "hombres_infectados": positivos_hombres_ucayali_atalaya, "mujeres_infectados": positivos_mujeres_ucayali_atalaya, "fallecidos": fallecidos_ucayali_atalaya, "hombres_fallecidos": fallecidos_hombres_ucayali_atalaya, "mujeres_fallecidos": fallecidos_mujeres_ucayali_atalaya, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ucayali_atalaya,
       "infancia": fallecidos_infancia_ucayali_atalaya,
       "adolescencia": fallecidos_adolescencia_ucayali_atalaya,
       "juventud": fallecidos_juventud_ucayali_atalaya,
       "adultez": fallecidos_adultez_ucayali_atalaya,
       "persona_mayor": fallecidos_persona_mayor_ucayali_atalaya
      }},

          {"name": "Padre Abad", "positivos": positivos_ucayali_padre_abad, "poblacion": poblacion_ucayali_padre_abad, "hombres_infectados": positivos_hombres_ucayali_padre_abad, "mujeres_infectados": positivos_mujeres_ucayali_padre_abad, "fallecidos": fallecidos_ucayali_padre_abad, "hombres_fallecidos": fallecidos_hombres_ucayali_padre_abad, "mujeres_fallecidos": fallecidos_mujeres_ucayali_padre_abad, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ucayali_padre_abad,
       "infancia": fallecidos_infancia_ucayali_padre_abad,
       "adolescencia": fallecidos_adolescencia_ucayali_padre_abad,
       "juventud": fallecidos_juventud_ucayali_padre_abad,
       "adultez": fallecidos_adultez_ucayali_padre_abad,
       "persona_mayor": fallecidos_persona_mayor_ucayali_padre_abad
      }},
          
          {"name": "Purus", "positivos": positivos_ucayali_purus, "poblacion": poblacion_ucayali_purus, "hombres_infectados": positivos_hombres_ucayali_purus, "mujeres_infectados": positivos_mujeres_ucayali_purus, "fallecidos": fallecidos_ucayali_purus, "hombres_fallecidos": fallecidos_hombres_ucayali_purus, "mujeres_fallecidos": fallecidos_mujeres_ucayali_purus, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ucayali_purus,
       "infancia": fallecidos_infancia_ucayali_purus,
       "adolescencia": fallecidos_adolescencia_ucayali_purus,
       "juventud": fallecidos_juventud_ucayali_purus,
       "adultez": fallecidos_adultez_ucayali_purus,
       "persona_mayor": fallecidos_persona_mayor_ucayali_purus
      }}
      ]
    }
print(json.dumps(ucayali));
sys.stdout.flush();
