import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos


poblacion_tumbes = 256423
positivos_tumbes = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "TUMBES"].shape)[0]
positivos_hombres_tumbes = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "TUMBES") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tumbes = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "TUMBES") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tumbes = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "TUMBES"].shape)[0]
fallecidos_hombres_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (
    casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (
    casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Tumbes - Etapa de vida
fallecidos_preinfancia_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tumbes = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Tumbes
#!Tumbes-Tumbes
poblacion_tumbes_tumbes = 177707
positivos_tumbes_tumbes = list(casos_positivos[casos_positivos['PROVINCIA'] == "TUMBES"].shape)[0]
positivos_hombres_tumbes_tumbes = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "TUMBES")].shape)[0]
positivos_mujeres_tumbes_tumbes = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "TUMBES")].shape)[0]
fallecidos_tumbes_tumbes = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TUMBES"].shape)[0]
fallecidos_hombres_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (
    casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (
    casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Tumbes - Etapa de vida
fallecidos_preinfancia_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tumbes_tumbes = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Tumbes-Contralmirante Villar
poblacion_tumbes_contralmirante_villar = 21684
positivos_tumbes_contralmirante_villar = list(casos_positivos[casos_positivos['PROVINCIA'] == "CONTRALMIRANTE VILLAR"].shape)[0]
positivos_hombres_tumbes_contralmirante_villar = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CONTRALMIRANTE VILLAR")].shape)[0]
positivos_mujeres_tumbes_contralmirante_villar = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CONTRALMIRANTE VILLAR")].shape)[0]
fallecidos_tumbes_contralmirante_villar = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR"].shape)[0]
fallecidos_hombres_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (
    casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (
    casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Contralmirante Villar - Etapa de vida
fallecidos_preinfancia_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tumbes_contralmirante_villar = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Zarumilla
poblacion_tumbes_zarumilla = 57032
positivos_tumbes_zarumilla = list(casos_positivos[casos_positivos['PROVINCIA'] == "ZARUMILLA"].shape)[0]
positivos_hombres_tumbes_zarumilla = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "ZARUMILLA")].shape)[0]
positivos_mujeres_tumbes_zarumilla = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "ZARUMILLA")].shape)[0]
fallecidos_tumbes_zarumilla = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ZARUMILLA"].shape)[0]
fallecidos_hombres_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Contralmirante Villar - Etapa de vida
fallecidos_preinfancia_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tumbes_zarumilla = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

tumbes =   {
      "name": "Tumbes",
      "poblacion": poblacion_tumbes,
      "positivos": positivos_tumbes,
      "hombres_infectados": positivos_hombres_tumbes,
      "mujeres_infectados": positivos_mujeres_tumbes,
      "fallecidos": fallecidos_tumbes,
      "hombres_fallecidos": fallecidos_hombres_tumbes,
      "mujeres_fallecidos": fallecidos_mujeres_tumbes,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tumbes,
       "infancia": fallecidos_infancia_tumbes,
       "adolescencia": fallecidos_adolescencia_tumbes,
       "juventud": fallecidos_juventud_tumbes,
       "adultez": fallecidos_adultez_tumbes,
       "persona_mayor": fallecidos_persona_mayor_tumbes
      },
      "url": "tumbes",
      "provincias": [
          {"name": "Tumbes", "positivos": positivos_tumbes_tumbes, "poblacion": poblacion_tumbes_tumbes, "hombres_infectados": positivos_hombres_tumbes_tumbes,"mujeres_infectados": positivos_mujeres_tumbes_tumbes, "fallecidos": fallecidos_tumbes_tumbes,  "hombres_fallecidos": fallecidos_hombres_tumbes_tumbes, "mujeres_fallecidos": fallecidos_mujeres_tumbes_tumbes, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tumbes_tumbes,
       "infancia": fallecidos_infancia_tumbes_tumbes,
       "adolescencia": fallecidos_adolescencia_tumbes_tumbes,
       "juventud": fallecidos_juventud_tumbes_tumbes,
       "adultez": fallecidos_adultez_tumbes_tumbes,
       "persona_mayor": fallecidos_persona_mayor_tumbes_tumbes
      }},

          {"name": "Contralmirante Villar", "positivos": positivos_tumbes_contralmirante_villar, "poblacion": poblacion_tumbes_contralmirante_villar, "hombres_infectados": positivos_hombres_tumbes_contralmirante_villar,"mujeres_infectados": positivos_mujeres_tumbes_contralmirante_villar, "fallecidos": fallecidos_tumbes_contralmirante_villar, "hombres_fallecidos": fallecidos_hombres_tumbes_contralmirante_villar, "mujeres_fallecidos": fallecidos_mujeres_tumbes_contralmirante_villar, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tumbes_contralmirante_villar,
       "infancia": fallecidos_infancia_tumbes_contralmirante_villar,
       "adolescencia": fallecidos_adolescencia_tumbes_contralmirante_villar,
       "juventud": fallecidos_juventud_tumbes_contralmirante_villar,
       "adultez": fallecidos_adultez_tumbes_contralmirante_villar,
       "persona_mayor": fallecidos_persona_mayor_tumbes_contralmirante_villar
      }},

          {"name": "Zarumilla", "positivos": positivos_tumbes_zarumilla, "poblacion": poblacion_tumbes_zarumilla, "hombres_infectados": positivos_hombres_tumbes_zarumilla,"mujeres_infectados": positivos_mujeres_tumbes_zarumilla, "fallecidos": fallecidos_tumbes_zarumilla, "hombres_fallecidos": fallecidos_hombres_tumbes_zarumilla, "mujeres_fallecidos": fallecidos_mujeres_tumbes_zarumilla, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tumbes_zarumilla,
       "infancia": fallecidos_infancia_tumbes_zarumilla,
       "adolescencia": fallecidos_adolescencia_tumbes_zarumilla,
       "juventud": fallecidos_juventud_tumbes_zarumilla,
       "adultez": fallecidos_adultez_tumbes_zarumilla,
       "persona_mayor": fallecidos_persona_mayor_tumbes_zarumilla
      }}
      ]
    }
print(json.dumps(tumbes));
sys.stdout.flush();
