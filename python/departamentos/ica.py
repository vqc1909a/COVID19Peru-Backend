import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_ica = 983511
positivos_ica = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "ICA"].shape)[0]
positivos_hombres_ica = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "ICA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "ICA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "ICA"].shape)[0]
fallecidos_hombres_ica  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ica  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Ica - Etapa de vida
fallecidos_preinfancia_ica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Ica
#!Ica-Ica
poblacion_ica_ica = 451473
positivos_ica_ica = list(casos_positivos[casos_positivos['PROVINCIA'] == "ICA"].shape)[0]
positivos_hombres_ica_ica = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ICA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica_ica = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ICA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica_ica = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ICA"].shape)[0]
fallecidos_hombres_ica_ica  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ica_ica  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia ICA - Etapa de vida
fallecidos_preinfancia_ica_ica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica_ica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica_ica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica_ica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica_ica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica_ica = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ica-Chincha
poblacion_ica_chincha = 271793
positivos_ica_chincha = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHINCHA"].shape)[0]
positivos_hombres_ica_chincha = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHINCHA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica_chincha = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHINCHA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica_chincha = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHINCHA"].shape)[0]
fallecidos_hombres_ica_chincha  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ica_chincha  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Chincha - Etapa de vida
fallecidos_preinfancia_ica_chincha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica_chincha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica_chincha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica_chincha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica_chincha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica_chincha = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ica-Nazca
poblacion_ica_nazca = 74828
positivos_ica_nazca = list(casos_positivos[casos_positivos['PROVINCIA'] == "NAZCA"].shape)[0]
positivos_hombres_ica_nazca = list(casos_positivos[(casos_positivos['PROVINCIA'] == "NAZCA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica_nazca = list(casos_positivos[(casos_positivos['PROVINCIA'] == "NAZCA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica_nazca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "NAZCA"].shape)[0]
fallecidos_hombres_ica_nazca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ica_nazca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Nazca - Etapa de vida
fallecidos_preinfancia_ica_nazca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica_nazca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica_nazca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica_nazca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica_nazca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica_nazca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ica-Palpa
poblacion_ica_palpa = 15331
positivos_ica_palpa = list(casos_positivos[casos_positivos['PROVINCIA'] == "PALPA"].shape)[0]
positivos_hombres_ica_palpa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PALPA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica_palpa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PALPA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica_palpa = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PALPA"].shape)[0]
fallecidos_hombres_ica_palpa  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ica_palpa  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Palpa - Etapa de vida
fallecidos_preinfancia_ica_palpa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica_palpa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica_palpa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica_palpa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica_palpa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica_palpa = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Ica-Pisco
poblacion_ica_pisco = 170086
positivos_ica_pisco = list(casos_positivos[casos_positivos['PROVINCIA'] == "PISCO"].shape)[0]
positivos_hombres_ica_pisco = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PISCO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica_pisco = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PISCO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica_pisco = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PISCO"].shape)[0]
fallecidos_hombres_ica_pisco  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ica_pisco  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Pisco - Etapa de vida
fallecidos_preinfancia_ica_pisco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica_pisco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica_pisco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica_pisco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica_pisco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica_pisco = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

ica = {
      "name": "Ica",
      "poblacion": poblacion_ica,
      "positivos": positivos_ica,
      "hombres_infectados": positivos_hombres_ica,
      "mujeres_infectados": positivos_mujeres_ica,
      "fallecidos": fallecidos_ica,
      "hombres_fallecidos": fallecidos_hombres_ica,
      "mujeres_fallecidos": fallecidos_mujeres_ica,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica,
       "infancia": fallecidos_infancia_ica,
       "adolescencia": fallecidos_adolescencia_ica,
       "juventud": fallecidos_juventud_ica,
       "adultez": fallecidos_adultez_ica,
       "persona_mayor": fallecidos_persona_mayor_ica
      },
      "url": "ica",
      "provincias": [
          {"name": "Ica", "positivos": positivos_ica_ica, "poblacion": poblacion_ica_ica, "hombres_infectados": positivos_hombres_ica_ica, "mujeres_infectados": positivos_mujeres_ica_ica, "fallecidos": fallecidos_ica_ica, "hombres_fallecidos": fallecidos_hombres_ica_ica, "mujeres_fallecidos": fallecidos_mujeres_ica_ica, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica_ica,
       "infancia": fallecidos_infancia_ica_ica,
       "adolescencia": fallecidos_adolescencia_ica_ica,
       "juventud": fallecidos_juventud_ica_ica,
       "adultez": fallecidos_adultez_ica_ica,
       "persona_mayor": fallecidos_persona_mayor_ica_ica
      }},
          
          {"name": "Chincha", "positivos": positivos_ica_chincha,"poblacion": poblacion_ica_chincha , "hombres_infectados": positivos_hombres_ica_chincha,"mujeres_infectados": positivos_mujeres_ica_chincha, "fallecidos": fallecidos_ica_chincha, "hombres_fallecidos": fallecidos_hombres_ica_chincha, "mujeres_fallecidos": fallecidos_mujeres_ica_chincha, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica_chincha,
       "infancia": fallecidos_infancia_ica_chincha,
       "adolescencia": fallecidos_adolescencia_ica_chincha,
       "juventud": fallecidos_juventud_ica_chincha,
       "adultez": fallecidos_adultez_ica_chincha,
       "persona_mayor": fallecidos_persona_mayor_ica_chincha
      }},

          {"name": "Nazca", "positivos": positivos_ica_nazca,"poblacion": poblacion_ica_nazca , "hombres_infectados": positivos_hombres_ica_nazca,"mujeres_infectados": positivos_mujeres_ica_nazca, "fallecidos": fallecidos_ica_nazca, "hombres_fallecidos": fallecidos_hombres_ica_nazca, "mujeres_fallecidos": fallecidos_mujeres_ica_nazca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica_nazca,
       "infancia": fallecidos_infancia_ica_nazca,
       "adolescencia": fallecidos_adolescencia_ica_nazca,
       "juventud": fallecidos_juventud_ica_nazca,
       "adultez": fallecidos_adultez_ica_nazca,
       "persona_mayor": fallecidos_persona_mayor_ica_nazca
      }},

          {"name": "Palpa", "positivos": positivos_ica_palpa,"poblacion": poblacion_ica_palpa , "hombres_infectados": positivos_hombres_ica_palpa,"mujeres_infectados": positivos_mujeres_ica_palpa, "fallecidos": fallecidos_ica_palpa,"hombres_fallecidos": fallecidos_hombres_ica_palpa, "mujeres_fallecidos": fallecidos_mujeres_ica_palpa, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica_palpa,
       "infancia": fallecidos_infancia_ica_palpa,
       "adolescencia": fallecidos_adolescencia_ica_palpa,
       "juventud": fallecidos_juventud_ica_palpa,
       "adultez": fallecidos_adultez_ica_palpa,
       "persona_mayor": fallecidos_persona_mayor_ica_palpa
      }},

          {"name": "Pisco", "positivos": positivos_ica_pisco,"poblacion": poblacion_ica_pisco , "hombres_infectados": positivos_hombres_ica_pisco,"mujeres_infectados": positivos_mujeres_ica_pisco, "fallecidos": fallecidos_ica_pisco, "hombres_fallecidos": fallecidos_hombres_ica_pisco, "mujeres_fallecidos": fallecidos_mujeres_ica_pisco, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica_pisco,
       "infancia": fallecidos_infancia_ica_pisco,
       "adolescencia": fallecidos_adolescencia_ica_pisco,
       "juventud": fallecidos_juventud_ica_pisco,
       "adultez": fallecidos_adultez_ica_pisco,
       "persona_mayor": fallecidos_persona_mayor_ica_pisco
      }}
      ]
    }

print(json.dumps(ica));
sys.stdout.flush();
