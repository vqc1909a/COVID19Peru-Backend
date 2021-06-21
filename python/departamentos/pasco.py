import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos


poblacion_pasco = 270575
positivos_pasco = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "PASCO"].shape)[0]
positivos_hombres_pasco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PASCO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_pasco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PASCO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_pasco = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "PASCO"].shape)[0]
fallecidos_hombres_pasco  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_pasco  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Departamento Pasco - Etapa de vida
fallecidos_preinfancia_pasco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_pasco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_pasco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_pasco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_pasco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_pasco = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincias
#!Provincia Pasco
poblacion_pasco_pasco = 138810
positivos_pasco_pasco = list(casos_positivos[casos_positivos['PROVINCIA'] == "PASCO"].shape)[0]
positivos_hombres_pasco_pasco = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PASCO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_pasco_pasco = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PASCO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_pasco_pasco = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PASCO"].shape)[0]
fallecidos_hombres_pasco_pasco  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_pasco_pasco  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Pasco - Etapa de vida
fallecidos_preinfancia_pasco_pasco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_pasco_pasco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_pasco_pasco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_pasco_pasco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_pasco_pasco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_pasco_pasco = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Daniel Alcides Carrion
poblacion_pasco_daniel_alcide_carrion = 46771
positivos_pasco_daniel_alcide_carrion = list(casos_positivos[casos_positivos['PROVINCIA'] == "DANIEL ALCIDES CARRION"].shape)[0]
positivos_hombres_pasco_daniel_alcide_carrion = list(casos_positivos[(casos_positivos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_pasco_daniel_alcide_carrion = list(casos_positivos[(casos_positivos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_pasco_daniel_alcide_carrion = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION"].shape)[0]
fallecidos_hombres_pasco_daniel_alcide_carrion  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_pasco_daniel_alcide_carrion  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Daniel Alcides Carrion - Etapa de vida
fallecidos_preinfancia_pasco_daniel_alcide_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_pasco_daniel_alcide_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_pasco_daniel_alcide_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_pasco_daniel_alcide_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_pasco_daniel_alcide_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_pasco_daniel_alcide_carrion = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia de Oxapampa
poblacion_pasco_oxapampa = 84994
positivos_pasco_oxapampa = list(casos_positivos[casos_positivos['PROVINCIA'] == "OXAPAMPA"].shape)[0]
positivos_hombres_pasco_oxapampa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "OXAPAMPA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_pasco_oxapampa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "OXAPAMPA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_pasco_oxapampa = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "OXAPAMPA"].shape)[0]
fallecidos_hombres_pasco_oxapampa  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_pasco_oxapampa  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Oxapampa - Etapa de vida
fallecidos_preinfancia_pasco_oxapampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_pasco_oxapampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_pasco_oxapampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_pasco_oxapampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_pasco_oxapampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_pasco_oxapampa = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


pasco = {
      "name": "Pasco",
      "poblacion": poblacion_pasco,
      "positivos": positivos_pasco,
      "hombres_infectados": positivos_hombres_pasco,
      "mujeres_infectados": positivos_mujeres_pasco,
      "fallecidos": fallecidos_pasco,
      "hombres_fallecidos": fallecidos_hombres_pasco,
      "mujeres_fallecidos": fallecidos_mujeres_pasco,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_pasco,
       "infancia": fallecidos_infancia_pasco,
       "adolescencia": fallecidos_adolescencia_pasco,
       "juventud": fallecidos_juventud_pasco,
       "adultez": fallecidos_adultez_pasco,
       "persona_mayor": fallecidos_persona_mayor_pasco
      },
      "url": "pasco",
      "provincias": [
          {"name": "Pasco", "positivos": positivos_pasco_pasco, "poblacion": poblacion_pasco_pasco, "hombres_infectados": positivos_hombres_pasco_pasco, "mujeres_infectados": positivos_mujeres_pasco_pasco, "fallecidos": fallecidos_pasco_pasco, "hombres_fallecidos": fallecidos_hombres_pasco_pasco, "mujeres_fallecidos": fallecidos_mujeres_pasco_pasco, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_pasco_pasco,
       "infancia": fallecidos_infancia_pasco_pasco,
       "adolescencia": fallecidos_adolescencia_pasco_pasco,
       "juventud": fallecidos_juventud_pasco_pasco,
       "adultez": fallecidos_adultez_pasco_pasco,
       "persona_mayor": fallecidos_persona_mayor_pasco_pasco
      }},

          {"name": "Daniel Alcides Carrion", "positivos": positivos_pasco_daniel_alcide_carrion,"poblacion": poblacion_pasco_daniel_alcide_carrion , "hombres_infectados": positivos_hombres_pasco_daniel_alcide_carrion,"mujeres_infectados": positivos_mujeres_pasco_daniel_alcide_carrion, "fallecidos": fallecidos_pasco_daniel_alcide_carrion, "hombres_fallecidos": fallecidos_hombres_pasco_daniel_alcide_carrion, "mujeres_fallecidos": fallecidos_mujeres_pasco_daniel_alcide_carrion, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_pasco_daniel_alcide_carrion,
       "infancia": fallecidos_infancia_pasco_daniel_alcide_carrion,
       "adolescencia": fallecidos_adolescencia_pasco_daniel_alcide_carrion,
       "juventud": fallecidos_juventud_pasco_daniel_alcide_carrion,
       "adultez": fallecidos_adultez_pasco_daniel_alcide_carrion,
       "persona_mayor": fallecidos_persona_mayor_pasco_daniel_alcide_carrion
      }},

          {"name": "Oxapampa", "positivos": positivos_pasco_oxapampa,"poblacion": poblacion_pasco_oxapampa , "hombres_infectados": positivos_hombres_pasco_oxapampa,"mujeres_infectados": positivos_mujeres_pasco_oxapampa, "fallecidos": fallecidos_pasco_oxapampa, "hombres_fallecidos": fallecidos_hombres_pasco_oxapampa, "mujeres_fallecidos": fallecidos_mujeres_pasco_oxapampa, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_pasco_oxapampa,
       "infancia": fallecidos_infancia_pasco_oxapampa,
       "adolescencia": fallecidos_adolescencia_pasco_oxapampa,
       "juventud": fallecidos_juventud_pasco_oxapampa,
       "adultez": fallecidos_adultez_pasco_oxapampa,
       "persona_mayor": fallecidos_persona_mayor_pasco_oxapampa
      }}

      ]
    }
    
print(json.dumps(pasco))
sys.stdout.flush();
