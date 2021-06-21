import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

#!Departamento Callao
poblacion_callao = 1147516
positivos_callao = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "CALLAO"].shape)[0]
positivos_hombres_callao = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CALLAO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_callao = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CALLAO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_callao = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "CALLAO"].shape)[0]
fallecidos_hombres_callao  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CALLAO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_callao  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CALLAO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Callao - Tarata
fallecidos_preinfancia_callao = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_callao = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_callao = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_callao = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_callao = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_callao = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0] 


#!Provincias Callao
#!Callao-Callao
poblacion_callao_callao = 1147516   
positivos_callao_callao = list(casos_positivos[casos_positivos['PROVINCIA'] == "CALLAO"].shape)[0]
positivos_hombres_callao_callao = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CALLAO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_callao_callao = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CALLAO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_callao_callao = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CALLAO"].shape)[0]
fallecidos_hombres_callao_callao  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CALLAO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_callao_callao  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CALLAO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Candarave - Tarata
fallecidos_preinfancia_callao_callao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_callao_callao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_callao_callao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_callao_callao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_callao_callao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_callao_callao = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

callao = {
      "name": "Callao",
      "poblacion": poblacion_callao,
      "positivos": positivos_callao,
      "hombres_infectados": positivos_hombres_callao,
      "mujeres_infectados": positivos_mujeres_callao,
      "fallecidos": fallecidos_callao,
      "hombres_fallecidos": fallecidos_hombres_callao, 
      "mujeres_fallecidos": fallecidos_mujeres_callao,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_callao,
       "infancia": fallecidos_infancia_callao,
       "adolescencia": fallecidos_adolescencia_callao,
       "juventud": fallecidos_juventud_callao,
       "adultez": fallecidos_adultez_callao,
       "persona_mayor": fallecidos_persona_mayor_callao
      },
      "url": "callao",
        "provincias": [
            {"name": "Callao", "positivos": positivos_callao_callao,"poblacion": poblacion_callao_callao , "hombres_infectados": positivos_hombres_callao_callao,"mujeres_infectados": positivos_mujeres_callao_callao, "fallecidos": fallecidos_callao_callao, "hombres_fallecidos": fallecidos_hombres_callao_callao, "mujeres_fallecidos": fallecidos_mujeres_callao_callao, "type": "Provincia",  
            "etapa_de_vida_fallecidos": {
                "primera_infancia": fallecidos_preinfancia_callao_callao,
                "infancia": fallecidos_infancia_callao_callao,
                "adolescencia": fallecidos_adolescencia_callao_callao,
                "juventud": fallecidos_juventud_callao_callao,
                "adultez": fallecidos_adultez_callao_callao,
                "persona_mayor": fallecidos_persona_mayor_callao_callao
            }}
        ]
    }

print(json.dumps(callao));
sys.stdout.flush();
