import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_madrededios = 183162
positivos_madrededios = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "MADRE DE DIOS"].shape)[0]
positivos_hombres_madrededios = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "MADRE DE DIOS") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_madrededios = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "MADRE DE DIOS") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_madrededios = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "MADRE DE DIOS"].shape)[0]
fallecidos_hombres_madrededios  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MADRE DE DIOS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_madrededios  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MADRE DE DIOS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Departamento Madrededios - Etapa de vida
fallecidos_preinfancia_madrededios = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MADRE DE DIOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_madrededios = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MADRE DE DIOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_madrededios = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MADRE DE DIOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_madrededios = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MADRE DE DIOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_madrededios = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MADRE DE DIOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_madrededios = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "MADRE DE DIOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Madre de Dios  
#!Madrededios-tambopata
poblacion_madre_de_dios_tambopata = 135259
positivos_madre_de_dios_tambopata = list(casos_positivos[casos_positivos['PROVINCIA'] == "TAMBOPATA"].shape)[0]
positivos_hombres_madre_de_dios_tambopata = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAMBOPATA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_madre_de_dios_tambopata = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAMBOPATA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_madre_de_dios_tambopata = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TAMBOPATA"].shape)[0]
fallecidos_hombres_madre_de_dios_tambopata  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_madre_de_dios_tambopata  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Tambopata - Etapa de vida
fallecidos_preinfancia_madre_de_dios_tambopata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_madre_de_dios_tambopata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_madre_de_dios_tambopata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_madre_de_dios_tambopata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_madre_de_dios_tambopata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_madre_de_dios_tambopata = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Madrededios-manu
poblacion_madre_de_dios_manu = 29878
positivos_madre_de_dios_manu = list(casos_positivos[casos_positivos['PROVINCIA'] == "MANU"].shape)[0]
positivos_hombres_madre_de_dios_manu = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MANU") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_madre_de_dios_manu = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MANU") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_madre_de_dios_manu = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MANU"].shape)[0]
fallecidos_hombres_madre_de_dios_manu  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_madre_de_dios_manu  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Manu - Etapa de vida
fallecidos_preinfancia_madre_de_dios_manu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_madre_de_dios_manu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_madre_de_dios_manu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_madre_de_dios_manu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_madre_de_dios_manu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_madre_de_dios_manu = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Madrededios-tahuamanu
poblacion_madre_de_dios_tahuamanu = 18025
positivos_madre_de_dios_tahuamanu = list(casos_positivos[casos_positivos['PROVINCIA'] == "TAHUAMANU"].shape)[0]
positivos_hombres_madre_de_dios_tahuamanu = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAHUAMANU") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_madre_de_dios_tahuamanu = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAHUAMANU") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_madre_de_dios_tahuamanu = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TAHUAMANU"].shape)[0]
fallecidos_hombres_madre_de_dios_tahuamanu  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_madre_de_dios_tahuamanu  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Tahuamanu - Etapa de vida
fallecidos_preinfancia_madre_de_dios_tahuamanu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_madre_de_dios_tahuamanu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_madre_de_dios_tahuamanu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_madre_de_dios_tahuamanu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_madre_de_dios_tahuamanu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_madre_de_dios_tahuamanu = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

madrededios =   {
      "name": "Madre de Dios",
      "poblacion": poblacion_madrededios,
      "positivos": positivos_madrededios,
      "hombres_infectados": positivos_hombres_madrededios,
      "mujeres_infectados": positivos_mujeres_madrededios,
      "fallecidos": fallecidos_madrededios,
      "hombres_fallecidos": fallecidos_hombres_madrededios,
      "mujeres_fallecidos": fallecidos_mujeres_madrededios,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_madrededios,
       "infancia": fallecidos_infancia_madrededios,
       "adolescencia": fallecidos_adolescencia_madrededios,
       "juventud": fallecidos_juventud_madrededios,
       "adultez": fallecidos_adultez_madrededios,
       "persona_mayor": fallecidos_persona_mayor_madrededios
      },
      "url": "madre-de-dios",
      "provincias": [
          {"name": "Tambopata", "positivos": positivos_madre_de_dios_tambopata, "poblacion": poblacion_madre_de_dios_tambopata, "hombres_infectados": positivos_hombres_madre_de_dios_tambopata, "mujeres_infectados": positivos_mujeres_madre_de_dios_tambopata, "fallecidos": fallecidos_madre_de_dios_tambopata,     "hombres_fallecidos": fallecidos_hombres_madre_de_dios_tambopata,
           "mujeres_fallecidos": fallecidos_mujeres_madre_de_dios_tambopata, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_madre_de_dios_tambopata,
       "infancia": fallecidos_infancia_madre_de_dios_tambopata,
       "adolescencia": fallecidos_adolescencia_madre_de_dios_tambopata,
       "juventud": fallecidos_juventud_madre_de_dios_tambopata,
       "adultez": fallecidos_adultez_madre_de_dios_tambopata,
       "persona_mayor": fallecidos_persona_mayor_madre_de_dios_tambopata
      }},

          {"name": "Manu", "positivos": positivos_madre_de_dios_manu, "poblacion": poblacion_madre_de_dios_manu, "hombres_infectados": positivos_hombres_madre_de_dios_manu, "mujeres_infectados": positivos_mujeres_madre_de_dios_manu, "fallecidos": fallecidos_madre_de_dios_manu, "hombres_fallecidos": fallecidos_hombres_madre_de_dios_manu,
              "mujeres_fallecidos": fallecidos_mujeres_madre_de_dios_manu, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_madre_de_dios_manu,
       "infancia": fallecidos_infancia_madre_de_dios_manu,
       "adolescencia": fallecidos_adolescencia_madre_de_dios_manu,
       "juventud": fallecidos_juventud_madre_de_dios_manu,
       "adultez": fallecidos_adultez_madre_de_dios_manu,
       "persona_mayor": fallecidos_persona_mayor_madre_de_dios_manu
      }},

        {"name": "Tahuamanu", "positivos": positivos_madre_de_dios_tahuamanu,"poblacion": poblacion_madre_de_dios_tahuamanu , "hombres_infectados": positivos_hombres_madre_de_dios_tahuamanu,"mujeres_infectados": positivos_mujeres_madre_de_dios_tahuamanu, "fallecidos": fallecidos_madre_de_dios_tahuamanu, "hombres_fallecidos": fallecidos_hombres_madre_de_dios_tahuamanu, "mujeres_fallecidos": fallecidos_mujeres_madre_de_dios_tahuamanu, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_madre_de_dios_tahuamanu,
       "infancia": fallecidos_infancia_madre_de_dios_tahuamanu,
       "adolescencia": fallecidos_adolescencia_madre_de_dios_tahuamanu,
       "juventud": fallecidos_juventud_madre_de_dios_tahuamanu,
       "adultez": fallecidos_adultez_madre_de_dios_tahuamanu,
       "persona_mayor": fallecidos_persona_mayor_madre_de_dios_tahuamanu
      }}
      ]
    }
print(json.dumps(madrededios));
sys.stdout.flush();
