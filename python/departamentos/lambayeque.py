import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_lambayeque = 1327433
positivos_lambayeque = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "LAMBAYEQUE"].shape)[0]
positivos_hombres_lambayeque = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LAMBAYEQUE") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lambayeque = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LAMBAYEQUE") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lambayeque = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE"].shape)[0]
fallecidos_hombres_lambayeque  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lambayeque  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Lambayeque - Etapa de vida
fallecidos_preinfancia_lambayeque = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lambayeque = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lambayeque = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lambayeque = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lambayeque = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lambayeque = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincias Lambayeque
#!Lambayeque-Chiclayo
poblacion_lambayeque_chiclayo = 902375
positivos_lambayeque_chiclayo = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHICLAYO"].shape)[0]
positivos_hombres_lambayeque_chiclayo = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CHICLAYO")].shape)[0]
positivos_mujeres_lambayeque_chiclayo = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CHICLAYO")].shape)[0]
fallecidos_lambayeque_chiclayo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHICLAYO"].shape)[0]
fallecidos_hombres_lambayeque_chiclayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lambayeque_chiclayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Chiclayo - Etapa de vida
fallecidos_preinfancia_lambayeque_chiclayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lambayeque_chiclayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lambayeque_chiclayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lambayeque_chiclayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lambayeque_chiclayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lambayeque_chiclayo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Lambayeque-Ferreñafe
poblacion_lambayeque_ferrenafe = 110750
positivos_lambayeque_ferrenafe = list(casos_positivos[casos_positivos['PROVINCIA'] == "FERREÑAFE"].shape)[0]
positivos_hombres_lambayeque_ferrenafe = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "FERREÑAFE")].shape)[0]
positivos_mujeres_lambayeque_ferrenafe = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "FERREÑAFE")].shape)[0]
fallecidos_lambayeque_ferrenafe = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "FERREÑAFE"].shape)[0]
fallecidos_hombres_lambayeque_ferrenafe  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lambayeque_ferrenafe  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Ferreñafe - Etapa de vida
fallecidos_preinfancia_lambayeque_ferrenafe = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lambayeque_ferrenafe = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lambayeque_ferrenafe = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lambayeque_ferrenafe = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lambayeque_ferrenafe = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lambayeque_ferrenafe = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Lambayeque-Lambayeque
poblacion_lambayeque_lambayeque = 314308
positivos_lambayeque_lambayeque = list(casos_positivos[casos_positivos['PROVINCIA'] == "LAMBAYEQUE"].shape)[0]
positivos_hombres_lambayeque_lambayeque = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "LAMBAYEQUE")].shape)[0]
positivos_mujeres_lambayeque_lambayeque = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "LAMBAYEQUE")].shape)[0]
fallecidos_lambayeque_lambayeque = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE"].shape)[0]
fallecidos_hombres_lambayeque_lambayeque = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lambayeque_lambayeque = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Lambayeque - Etapa de vida
fallecidos_preinfancia_lambayeque_lambayeque = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lambayeque_lambayeque = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lambayeque_lambayeque = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lambayeque_lambayeque = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lambayeque_lambayeque = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lambayeque_lambayeque = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


lambayeque = {
      "name": "Lambayeque",
      "poblacion": poblacion_lambayeque,
      "positivos": positivos_lambayeque,
      "hombres_infectados": positivos_hombres_lambayeque,
      "mujeres_infectados": positivos_mujeres_lambayeque,
      "fallecidos": fallecidos_lambayeque,
      "hombres_fallecidos": fallecidos_hombres_lambayeque,
      "mujeres_fallecidos": fallecidos_mujeres_lambayeque,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lambayeque,
       "infancia": fallecidos_infancia_lambayeque,
       "adolescencia": fallecidos_adolescencia_lambayeque,
       "juventud": fallecidos_juventud_lambayeque,
       "adultez": fallecidos_adultez_lambayeque,
       "persona_mayor": fallecidos_persona_mayor_lambayeque
      },
      "url": "lambayeque",
      "provincias": [
          {"name": "Chiclayo", "positivos": positivos_lambayeque_chiclayo, "poblacion": poblacion_lambayeque_chiclayo, "hombres_infectados": positivos_hombres_lambayeque_chiclayo, "mujeres_infectados": positivos_mujeres_lambayeque_chiclayo, "fallecidos": fallecidos_lambayeque_chiclayo, "hombres_fallecidos": fallecidos_hombres_lambayeque_chiclayo,
           "mujeres_fallecidos": fallecidos_mujeres_lambayeque_chiclayo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lambayeque_chiclayo,
       "infancia": fallecidos_infancia_lambayeque_chiclayo,
       "adolescencia": fallecidos_adolescencia_lambayeque_chiclayo,
       "juventud": fallecidos_juventud_lambayeque_chiclayo,
       "adultez": fallecidos_adultez_lambayeque_chiclayo,
       "persona_mayor": fallecidos_persona_mayor_lambayeque_chiclayo
      }},

          {"name": "Ferreñafe", "positivos": positivos_lambayeque_ferrenafe, "poblacion": poblacion_lambayeque_ferrenafe, "hombres_infectados": positivos_hombres_lambayeque_ferrenafe,"mujeres_infectados": positivos_mujeres_lambayeque_ferrenafe, "fallecidos": fallecidos_lambayeque_ferrenafe, "hombres_fallecidos": fallecidos_hombres_lambayeque_ferrenafe,
           "mujeres_fallecidos": fallecidos_mujeres_lambayeque_ferrenafe,"type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lambayeque_ferrenafe,
       "infancia": fallecidos_infancia_lambayeque_ferrenafe,
       "adolescencia": fallecidos_adolescencia_lambayeque_ferrenafe,
       "juventud": fallecidos_juventud_lambayeque_ferrenafe,
       "adultez": fallecidos_adultez_lambayeque_ferrenafe,
       "persona_mayor": fallecidos_persona_mayor_lambayeque_ferrenafe
      }},

          {"name": "Lambayeque", "positivos": positivos_lambayeque_lambayeque, "poblacion": poblacion_lambayeque_lambayeque, "hombres_infectados": positivos_hombres_lambayeque_lambayeque, "mujeres_infectados": positivos_mujeres_lambayeque_lambayeque, "fallecidos": fallecidos_lambayeque_lambayeque, "hombres_fallecidos": fallecidos_hombres_lambayeque_lambayeque,
           "mujeres_fallecidos": fallecidos_mujeres_lambayeque_lambayeque, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lambayeque_lambayeque,
       "infancia": fallecidos_infancia_lambayeque_lambayeque,
       "adolescencia": fallecidos_adolescencia_lambayeque_lambayeque,
       "juventud": fallecidos_juventud_lambayeque_lambayeque,
       "adultez": fallecidos_adultez_lambayeque_lambayeque,
       "persona_mayor": fallecidos_persona_mayor_lambayeque_lambayeque
      }}
      ]
    }
    
print(json.dumps(lambayeque));
sys.stdout.flush();
