import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

#!Departamento Tacna
poblacion_tacna = 378316
positivos_tacna = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "TACNA"].shape)[0]
positivos_hombres_tacna = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "TACNA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tacna = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "TACNA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tacna = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "TACNA"].shape)[0]
fallecidos_hombres_tacna  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_tacna  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Tacna - Etapa de vida
fallecidos_preinfancia_tacna = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tacna = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tacna = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tacna = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tacna = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tacna = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Tacna
#!Tacna-Tacna
poblacion_tacna_tacna = 350222
positivos_tacna_tacna = list(casos_positivos[casos_positivos['PROVINCIA'] == "TACNA"].shape)[0]
positivos_hombres_tacna_tacna = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TACNA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tacna_tacna = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TACNA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tacna_tacna = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TACNA"].shape)[0]
fallecidos_hombres_tacna_tacna  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TACNA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_tacna_tacna  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TACNA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Tacna - Etapa de vida
fallecidos_preinfancia_tacna_tacna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tacna_tacna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tacna_tacna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tacna_tacna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tacna_tacna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tacna_tacna = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Tacna-Candarave
poblacion_tacna_candarave = 9044
positivos_tacna_candarave = list(casos_positivos[casos_positivos['PROVINCIA'] == "CANDARAVE"].shape)[0]
positivos_hombres_tacna_candarave = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANDARAVE") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tacna_candarave = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANDARAVE") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tacna_candarave = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CANDARAVE"].shape)[0]
fallecidos_hombres_tacna_candarave  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANDARAVE") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_tacna_candarave  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANDARAVE") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Candarave - Etapa de vida
fallecidos_preinfancia_tacna_candarave = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tacna_candarave = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tacna_candarave = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tacna_candarave = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tacna_candarave = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tacna_candarave = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Tacna-Jorge Basadre
poblacion_tacna_jorge_basadre = 10110
positivos_tacna_jorge_basadre = list(casos_positivos[casos_positivos['PROVINCIA'] == "JORGE BASADRE"].shape)[0]
positivos_hombres_tacna_jorge_basadre = list(casos_positivos[(casos_positivos['PROVINCIA'] == "JORGE BASADRE") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tacna_jorge_basadre = list(casos_positivos[(casos_positivos['PROVINCIA'] == "JORGE BASADRE") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tacna_jorge_basadre = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "JORGE BASADRE"].shape)[0]
fallecidos_hombres_tacna_jorge_basadre  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JORGE BASADRE") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_tacna_jorge_basadre  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JORGE BASADRE") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Candarave - Jorge Basadre
fallecidos_preinfancia_tacna_jorge_basadre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tacna_jorge_basadre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tacna_jorge_basadre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tacna_jorge_basadre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tacna_jorge_basadre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tacna_jorge_basadre = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Tacna-Tarata
poblacion_tacna_tarata = 8940
positivos_tacna_tarata = list(casos_positivos[casos_positivos['PROVINCIA'] == "TARATA"].shape)[0]
positivos_hombres_tacna_tarata = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TARATA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tacna_tarata = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TARATA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tacna_tarata = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TARATA"].shape)[0]
fallecidos_hombres_tacna_tarata  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TARATA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_tacna_tarata  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TARATA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Candarave - Tarata
fallecidos_preinfancia_tacna_tarata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tacna_tarata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tacna_tarata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tacna_tarata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tacna_tarata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tacna_tarata = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

tacna =   {
      "name": "Tacna",
      "poblacion": poblacion_tacna,
      "positivos": positivos_tacna,
      "hombres_infectados": positivos_hombres_tacna,
      "mujeres_infectados": positivos_mujeres_tacna,
      "fallecidos": fallecidos_tacna,
      "hombres_fallecidos": fallecidos_hombres_tacna,
      "mujeres_fallecidos": fallecidos_mujeres_tacna,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tacna,
       "infancia": fallecidos_infancia_tacna,
       "adolescencia": fallecidos_adolescencia_tacna,
       "juventud": fallecidos_juventud_tacna,
       "adultez": fallecidos_adultez_tacna,
       "persona_mayor": fallecidos_persona_mayor_tacna
      },
      "url": "tacna",
      "provincias": [
        {"name": "Tacna", "positivos": positivos_tacna_tacna,"poblacion": poblacion_tacna_tacna , "hombres_infectados": positivos_hombres_tacna_tacna,"mujeres_infectados": positivos_mujeres_tacna_tacna, "fallecidos": fallecidos_tacna_tacna,  "hombres_fallecidos": fallecidos_hombres_tacna_tacna, "mujeres_fallecidos": fallecidos_mujeres_tacna_tacna, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tacna_tacna,
       "infancia": fallecidos_infancia_tacna_tacna,
       "adolescencia": fallecidos_adolescencia_tacna_tacna,
       "juventud": fallecidos_juventud_tacna_tacna,
       "adultez": fallecidos_adultez_tacna_tacna,
       "persona_mayor": fallecidos_persona_mayor_tacna_tacna
      }},

        {"name": "Candarave", "positivos": positivos_tacna_candarave,"poblacion": poblacion_tacna_candarave , "hombres_infectados": positivos_hombres_tacna_candarave,"mujeres_infectados": positivos_mujeres_tacna_candarave, "fallecidos": fallecidos_tacna_candarave, "hombres_fallecidos": fallecidos_hombres_tacna_candarave, "mujeres_fallecidos": fallecidos_mujeres_tacna_candarave, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tacna_candarave,
       "infancia": fallecidos_infancia_tacna_candarave,
       "adolescencia": fallecidos_adolescencia_tacna_candarave,
       "juventud": fallecidos_juventud_tacna_candarave,
       "adultez": fallecidos_adultez_tacna_candarave,
       "persona_mayor": fallecidos_persona_mayor_tacna_candarave
      }},

        {"name": "Jorge Basadre", "positivos": positivos_tacna_jorge_basadre,"poblacion": poblacion_tacna_jorge_basadre , "hombres_infectados": positivos_hombres_tacna_jorge_basadre,"mujeres_infectados": positivos_mujeres_tacna_jorge_basadre, "fallecidos": fallecidos_tacna_jorge_basadre, "hombres_fallecidos": fallecidos_hombres_tacna_jorge_basadre, "mujeres_fallecidos": fallecidos_mujeres_tacna_jorge_basadre, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tacna_jorge_basadre,
       "infancia": fallecidos_infancia_tacna_jorge_basadre,
       "adolescencia": fallecidos_adolescencia_tacna_jorge_basadre,
       "juventud": fallecidos_juventud_tacna_jorge_basadre,
       "adultez": fallecidos_adultez_tacna_jorge_basadre,
       "persona_mayor": fallecidos_persona_mayor_tacna_jorge_basadre
      }},

        {"name": "Tarata", "positivos": positivos_tacna_tarata, "poblacion": poblacion_tacna_tarata, "hombres_infectados": positivos_hombres_tacna_tarata, "mujeres_infectados": positivos_mujeres_tacna_tarata, "fallecidos": fallecidos_tacna_tarata, "hombres_fallecidos": fallecidos_hombres_tacna_tarata, "mujeres_fallecidos": fallecidos_mujeres_tacna_tarata, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tacna_tarata,
       "infancia": fallecidos_infancia_tacna_tarata,
       "adolescencia": fallecidos_adolescencia_tacna_tarata,
       "juventud": fallecidos_juventud_tacna_tarata,
       "adultez": fallecidos_adultez_tacna_tarata,
       "persona_mayor": fallecidos_persona_mayor_tacna_tarata
      }}
      ]
    }
print(json.dumps(tacna));
sys.stdout.flush();
