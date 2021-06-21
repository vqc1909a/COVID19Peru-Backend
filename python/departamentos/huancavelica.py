# import pandas as pd
# import json
# import sys

# casos_positivos = pd.read_csv(
#     "https://cloud.minsa.gob.pe/s/Y8w3wHsEdYQSZRp/download", sep=";")

# casos_fallecidos = pd.read_csv(
#     "https://cloud.minsa.gob.pe/s/Md37cjXmjT9qYSa/download", encoding="ISO-8859-1", sep=";")

import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_huancavelica = 353645
positivos_huancavelica = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "HUANCAVELICA"].shape)[0]
positivos_hombres_huancavelica = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA"].shape)[0]
fallecidos_hombres_huancavelica  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huancavelica  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Huancavelica - Etapa de vida
fallecidos_preinfancia_huancavelica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Huancavelica
#!Huancavelica-Huancavelica
poblacion_huancavelica_huancavelica = 113706
positivos_huancavelica_huancavelica = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUANCAVELICA"].shape)[0]
positivos_hombres_huancavelica_huancavelica = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANCAVELICA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_huancavelica = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANCAVELICA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_huancavelica = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUANCAVELICA"].shape)[0]
fallecidos_hombres_huancavelica_huancavelica  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huancavelica_huancavelica  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Huancavelica - Etapa de vida
fallecidos_preinfancia_huancavelica_huancavelica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_huancavelica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_huancavelica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_huancavelica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_huancavelica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_huancavelica = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huancavelica-Acobamba
poblacion_huancavelica_acobamba = 54275
positivos_huancavelica_acobamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "ACOBAMBA"].shape)[0]
positivos_hombres_huancavelica_acobamba = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ACOBAMBA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_acobamba = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ACOBAMBA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_acobamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ACOBAMBA"].shape)[0]
fallecidos_hombres_huancavelica_acobamba  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huancavelica_acobamba  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Acobamba - Etapa de vida
fallecidos_preinfancia_huancavelica_acobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_acobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_acobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_acobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_acobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_acobamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huancavelica-Angaraes
poblacion_huancavelica_angaraes = 45385
positivos_huancavelica_angaraes = list(casos_positivos[casos_positivos['PROVINCIA'] == "ANGARAES"].shape)[0]
positivos_hombres_huancavelica_angaraes = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ANGARAES") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_angaraes = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ANGARAES") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_angaraes = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ANGARAES"].shape)[0]
fallecidos_hombres_huancavelica_angaraes  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huancavelica_angaraes  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Angaraes - Etapa de vida
fallecidos_preinfancia_huancavelica_angaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_angaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_angaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_angaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_angaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_angaraes = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Huancavelica-Castrovirreyna
poblacion_huancavelica_castrovirreyna = 14030
positivos_huancavelica_castrovirreyna = list(casos_positivos[casos_positivos['PROVINCIA'] == "CASTROVIRREYNA"].shape)[0]
positivos_hombres_huancavelica_castrovirreyna = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_castrovirreyna = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_castrovirreyna = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA"].shape)[0]
fallecidos_hombres_huancavelica_castrovirreyna  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huancavelica_castrovirreyna  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Castrovirreyna - Etapa de vida
fallecidos_preinfancia_huancavelica_castrovirreyna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_castrovirreyna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_castrovirreyna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_castrovirreyna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_castrovirreyna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_castrovirreyna = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huancavelica-Churcampa
poblacion_huancavelica_churcampa = 31887
positivos_huancavelica_churcampa = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHURCAMPA"].shape)[0]
positivos_hombres_huancavelica_churcampa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHURCAMPA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_churcampa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHURCAMPA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_churcampa = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHURCAMPA"].shape)[0]
fallecidos_hombres_huancavelica_churcampa  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huancavelica_churcampa  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Churcampa - Etapa de vida
fallecidos_preinfancia_huancavelica_churcampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_churcampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_churcampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_churcampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_churcampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_churcampa = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Huancavelica-Huaytara
poblacion_huancavelica_huaytara = 17016
positivos_huancavelica_huaytara = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUAYTARA"].shape)[0]
positivos_hombres_huancavelica_huaytara = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUAYTARA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_huaytara = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUAYTARA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_huaytara = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUAYTARA"].shape)[0]
fallecidos_hombres_huancavelica_huaytara  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huancavelica_huaytara  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Huaytara - Etapa de vida
fallecidos_preinfancia_huancavelica_huaytara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_huaytara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_huaytara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_huaytara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_huaytara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_huaytara = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huancavelica-Tayacaja
poblacion_huancavelica_tayacaja = 77346
positivos_huancavelica_tayacaja = list(casos_positivos[casos_positivos['PROVINCIA'] == "TAYACAJA"].shape)[0]
positivos_hombres_huancavelica_tayacaja = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAYACAJA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_tayacaja = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAYACAJA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_tayacaja = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TAYACAJA"].shape)[0]
fallecidos_hombres_huancavelica_tayacaja  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huancavelica_tayacaja  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Tayacaja - Etapa de vida
fallecidos_preinfancia_huancavelica_tayacaja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_tayacaja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_tayacaja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_tayacaja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_tayacaja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_tayacaja = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

huancavelica =   {
      "name": "Huancavelica",
      "poblacion": poblacion_huancavelica,
      "positivos": positivos_huancavelica,
      "hombres_infectados": positivos_hombres_huancavelica,
      "mujeres_infectados": positivos_mujeres_huancavelica,
      "fallecidos": fallecidos_huancavelica,
      "hombres_fallecidos": fallecidos_hombres_huancavelica, 
      "mujeres_fallecidos": fallecidos_mujeres_huancavelica,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica,
       "infancia": fallecidos_infancia_huancavelica,
       "adolescencia": fallecidos_adolescencia_huancavelica,
       "juventud": fallecidos_juventud_huancavelica,
       "adultez": fallecidos_adultez_huancavelica,
       "persona_mayor": fallecidos_persona_mayor_huancavelica
      },
      "url": "huancavelica",
      "provincias": [
          {"name": "Huancavelica", "positivos": positivos_huancavelica_huancavelica, "poblacion": poblacion_huancavelica_huancavelica , "hombres_infectados": positivos_hombres_huancavelica_huancavelica,"mujeres_infectados": positivos_mujeres_huancavelica_huancavelica, "fallecidos": fallecidos_huancavelica_huancavelica, "hombres_fallecidos": fallecidos_hombres_huancavelica_huancavelica, "mujeres_fallecidos": fallecidos_mujeres_huancavelica_huancavelica, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_huancavelica,
       "infancia": fallecidos_infancia_huancavelica_huancavelica,
       "adolescencia": fallecidos_adolescencia_huancavelica_huancavelica,
       "juventud": fallecidos_juventud_huancavelica_huancavelica,
       "adultez": fallecidos_adultez_huancavelica_huancavelica,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_huancavelica
      }},

          {"name": "Acobamba", "positivos": positivos_huancavelica_acobamba,"poblacion": poblacion_huancavelica_acobamba , "hombres_infectados": positivos_hombres_huancavelica_acobamba,"mujeres_infectados": positivos_mujeres_huancavelica_acobamba, "fallecidos": fallecidos_huancavelica_acobamba, "hombres_fallecidos": fallecidos_hombres_huancavelica_acobamba, "mujeres_fallecidos": fallecidos_mujeres_huancavelica_acobamba, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_acobamba,
       "infancia": fallecidos_infancia_huancavelica_acobamba,
       "adolescencia": fallecidos_adolescencia_huancavelica_acobamba,
       "juventud": fallecidos_juventud_huancavelica_acobamba,
       "adultez": fallecidos_adultez_huancavelica_acobamba,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_acobamba
      }},

          {"name": "Angaraes", "positivos": positivos_huancavelica_angaraes,"poblacion": poblacion_huancavelica_angaraes , "hombres_infectados": positivos_hombres_huancavelica_angaraes,"mujeres_infectados": positivos_mujeres_huancavelica_angaraes, "fallecidos": fallecidos_huancavelica_angaraes, "hombres_fallecidos": fallecidos_hombres_huancavelica_angaraes, "mujeres_fallecidos": fallecidos_mujeres_huancavelica_angaraes, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_angaraes,
       "infancia": fallecidos_infancia_huancavelica_angaraes,
       "adolescencia": fallecidos_adolescencia_huancavelica_angaraes,
       "juventud": fallecidos_juventud_huancavelica_angaraes,
       "adultez": fallecidos_adultez_huancavelica_angaraes,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_angaraes
      }},

          {"name": "Castrovirreyna", "positivos": positivos_huancavelica_castrovirreyna, "poblacion": poblacion_huancavelica_castrovirreyna , "hombres_infectados": positivos_hombres_huancavelica_castrovirreyna,"mujeres_infectados": positivos_mujeres_huancavelica_castrovirreyna, "fallecidos": fallecidos_huancavelica_castrovirreyna, "hombres_fallecidos": fallecidos_hombres_huancavelica_castrovirreyna, "mujeres_fallecidos": fallecidos_mujeres_huancavelica_castrovirreyna, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_castrovirreyna,
       "infancia": fallecidos_infancia_huancavelica_castrovirreyna,
       "adolescencia": fallecidos_adolescencia_huancavelica_castrovirreyna,
       "juventud": fallecidos_juventud_huancavelica_castrovirreyna,
       "adultez": fallecidos_adultez_huancavelica_castrovirreyna,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_castrovirreyna
      }},

          {"name": "Churcampa", "positivos": positivos_huancavelica_churcampa,"poblacion": poblacion_huancavelica_churcampa , "hombres_infectados": positivos_hombres_huancavelica_churcampa,"mujeres_infectados": positivos_mujeres_huancavelica_churcampa, "fallecidos": fallecidos_huancavelica_churcampa, "hombres_fallecidos": fallecidos_hombres_huancavelica_churcampa, "mujeres_fallecidos": fallecidos_mujeres_huancavelica_churcampa, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_churcampa,
       "infancia": fallecidos_infancia_huancavelica_churcampa,
       "adolescencia": fallecidos_adolescencia_huancavelica_churcampa,
       "juventud": fallecidos_juventud_huancavelica_churcampa,
       "adultez": fallecidos_adultez_huancavelica_churcampa,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_churcampa
      }},

          {"name": "Huaytara", "positivos": positivos_huancavelica_huaytara,"poblacion": poblacion_huancavelica_huaytara , "hombres_infectados": positivos_hombres_huancavelica_huaytara,"mujeres_infectados": positivos_mujeres_huancavelica_huaytara, "fallecidos": fallecidos_huancavelica_huaytara, "hombres_fallecidos": fallecidos_hombres_huancavelica_huaytara, "mujeres_fallecidos": fallecidos_mujeres_huancavelica_huaytara, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_huaytara,
       "infancia": fallecidos_infancia_huancavelica_huaytara,
       "adolescencia": fallecidos_adolescencia_huancavelica_huaytara,
       "juventud": fallecidos_juventud_huancavelica_huaytara,
       "adultez": fallecidos_adultez_huancavelica_huaytara,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_huaytara
      }},

          {"name": "Tayacaja", "positivos": positivos_huancavelica_tayacaja,"poblacion": poblacion_huancavelica_tayacaja , "hombres_infectados": positivos_hombres_huancavelica_tayacaja,"mujeres_infectados": positivos_mujeres_huancavelica_tayacaja, "fallecidos": fallecidos_huancavelica_tayacaja, "hombres_fallecidos": fallecidos_hombres_huancavelica_tayacaja, "mujeres_fallecidos": fallecidos_mujeres_huancavelica_tayacaja, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_tayacaja,
       "infancia": fallecidos_infancia_huancavelica_tayacaja,
       "adolescencia": fallecidos_adolescencia_huancavelica_tayacaja,
       "juventud": fallecidos_juventud_huancavelica_tayacaja,
       "adultez": fallecidos_adultez_huancavelica_tayacaja,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_tayacaja
      }}
      ]
    }
    
print(json.dumps(huancavelica));
sys.stdout.flush();