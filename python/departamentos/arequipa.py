import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos
    
poblacion_arequipa = 1526342
positivos_arequipa = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "AREQUIPA"].shape)[0]
positivos_hombres_arequipa = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AREQUIPA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AREQUIPA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "AREQUIPA"].shape)[0]
fallecidos_hombres_arequipa  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AREQUIPA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_arequipa  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AREQUIPA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Arequipa - Etapa de vida
fallecidos_preinfancia_arequipa = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_arequipa = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_arequipa = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_arequipa = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_arequipa = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_arequipa = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Provincias Arequipa
#!Arequipa-Arequipa
poblacion_arequipa_arequipa = 1154522
positivos_arequipa_arequipa = list(casos_positivos[casos_positivos['PROVINCIA'] == "AREQUIPA"].shape)[0]
positivos_hombres_arequipa_arequipa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "AREQUIPA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa_arequipa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "AREQUIPA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa_arequipa = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "AREQUIPA"].shape)[0]
fallecidos_hombres_arequipa_arequipa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AREQUIPA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_arequipa_arequipa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AREQUIPA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Arequipa - Etapa de vida
fallecidos_preinfancia_arequipa_arequipa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_arequipa_arequipa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_arequipa_arequipa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_arequipa_arequipa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_arequipa_arequipa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_arequipa_arequipa = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AREQUIPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Arequipa-Camana 
poblacion_arequipa_camana = 67841
positivos_arequipa_camana = list(casos_positivos[casos_positivos['PROVINCIA'] == "CAMANA"].shape)[0]
positivos_hombres_arequipa_camana = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CAMANA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa_camana = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CAMANA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa_camana = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CAMANA"].shape)[0]
fallecidos_hombres_arequipa_camana = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "CAMANA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_arequipa_camana = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "CAMANA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Camana  - Etapa de vida
fallecidos_preinfancia_arequipa_camana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAMANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_arequipa_camana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAMANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_arequipa_camana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAMANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_arequipa_camana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAMANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_arequipa_camana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAMANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_arequipa_camana = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAMANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Arequipa-Caraveli
poblacion_arequipa_caraveli = 49954
positivos_arequipa_caraveli = list(casos_positivos[casos_positivos['PROVINCIA'] == "CARAVELI"].shape)[0]
positivos_hombres_arequipa_caraveli = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CARAVELI") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa_caraveli = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CARAVELI") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa_caraveli = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CARAVELI"].shape)[0]
fallecidos_hombres_arequipa_caraveli = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "CARAVELI") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_arequipa_caraveli = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "CARAVELI") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Caraveli  - Etapa de vida
fallecidos_preinfancia_arequipa_caraveli = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CARAVELI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_arequipa_caraveli = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CARAVELI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_arequipa_caraveli = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CARAVELI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_arequipa_caraveli = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CARAVELI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_arequipa_caraveli = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CARAVELI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_arequipa_caraveli = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CARAVELI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]




#!Arequipa-Castilla
poblacion_arequipa_castilla = 43684
positivos_arequipa_castilla = list(casos_positivos[casos_positivos['PROVINCIA'] == "CASTILLA"].shape)[0]
positivos_hombres_arequipa_castilla = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CASTILLA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa_castilla = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CASTILLA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa_castilla = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CASTILLA"].shape)[0]
fallecidos_hombres_arequipa_castilla = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "CASTILLA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_arequipa_castilla = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "CASTILLA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Castilla  - Etapa de vida
fallecidos_preinfancia_arequipa_castilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_arequipa_castilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_arequipa_castilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_arequipa_castilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_arequipa_castilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_arequipa_castilla = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Arequipa-Caylloma
poblacion_arequipa_caylloma = 106801
positivos_arequipa_caylloma = list(casos_positivos[casos_positivos['PROVINCIA'] == "CAYLLOMA"].shape)[0]
positivos_hombres_arequipa_caylloma = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CAYLLOMA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa_caylloma = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CAYLLOMA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa_caylloma = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CAYLLOMA"].shape)[0]
fallecidos_hombres_arequipa_caylloma = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "CAYLLOMA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_arequipa_caylloma = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "CAYLLOMA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Castilla  - Etapa de vida
fallecidos_preinfancia_arequipa_caylloma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_arequipa_caylloma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_arequipa_caylloma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_arequipa_caylloma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_arequipa_caylloma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_arequipa_caylloma = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Arequipa-Condesuyos
poblacion_arequipa_condesuyos = 24691
positivos_arequipa_condesuyos = list(casos_positivos[casos_positivos['PROVINCIA'] == "CONDESUYOS"].shape)[0]
positivos_hombres_arequipa_condesuyos = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CONDESUYOS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa_condesuyos = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CONDESUYOS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa_condesuyos = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CONDESUYOS"].shape)[0]
fallecidos_hombres_arequipa_condesuyos = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "CONDESUYOS") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_arequipa_condesuyos = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "CONDESUYOS") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Condesuyos  - Etapa de vida
fallecidos_preinfancia_arequipa_condesuyos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CONDESUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_arequipa_condesuyos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CONDESUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_arequipa_condesuyos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CONDESUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_arequipa_condesuyos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CONDESUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_arequipa_condesuyos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CONDESUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_arequipa_condesuyos = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CONDESUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Arequipa-Islay
poblacion_arequipa_islay = 61009
positivos_arequipa_islay = list(casos_positivos[casos_positivos['PROVINCIA'] == "ISLAY"].shape)[0]
positivos_hombres_arequipa_islay = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ISLAY") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa_islay = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ISLAY") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa_islay = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ISLAY"].shape)[0]
fallecidos_hombres_arequipa_islay = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "ISLAY") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_arequipa_islay = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "ISLAY") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Islay - Etapa de vida
fallecidos_preinfancia_arequipa_islay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ISLAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_arequipa_islay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ISLAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_arequipa_islay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ISLAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_arequipa_islay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ISLAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_arequipa_islay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ISLAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_arequipa_islay = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ISLAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Arequipa-Union
poblacion_arequipa_union = 17840
positivos_arequipa_union = list(casos_positivos[casos_positivos['PROVINCIA'] == "LA UNION"].shape)[0]
positivos_hombres_arequipa_union = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LA UNION") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa_union = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LA UNION") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa_union = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LA UNION"].shape)[0]
fallecidos_hombres_arequipa_union = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "LA UNION") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_arequipa_union = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "LA UNION") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Union - Etapa de vida
fallecidos_preinfancia_arequipa_union = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="LA UNION") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_arequipa_union = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="LA UNION") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_arequipa_union = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="LA UNION") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_arequipa_union = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="LA UNION") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_arequipa_union = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="LA UNION") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_arequipa_union = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="LA UNION") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


arequipa =  {
      "name": "Arequipa",
      "poblacion": poblacion_arequipa,
      "positivos": positivos_arequipa,
      "hombres_infectados": positivos_hombres_arequipa,
      "mujeres_infectados": positivos_mujeres_arequipa,
      "fallecidos": fallecidos_arequipa,
      "hombres_fallecidos": fallecidos_hombres_arequipa,
      "mujeres_fallecidos": fallecidos_mujeres_arequipa,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa,
       "infancia": fallecidos_infancia_arequipa,
       "adolescencia": fallecidos_adolescencia_arequipa,
       "juventud": fallecidos_juventud_arequipa,
       "adultez": fallecidos_adultez_arequipa,
       "persona_mayor": fallecidos_persona_mayor_arequipa
      },
      "url": "arequipa",
      "provincias": [
          {"name": "Arequipa", "positivos": positivos_arequipa_arequipa, "poblacion": poblacion_arequipa_arequipa, "hombres_infectados": positivos_hombres_arequipa_arequipa, "mujeres_infectados": positivos_mujeres_arequipa_arequipa, "fallecidos": fallecidos_arequipa_arequipa, "hombres_fallecidos": fallecidos_hombres_arequipa_arequipa,
           "mujeres_fallecidos": fallecidos_mujeres_arequipa_arequipa, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_arequipa,
       "infancia": fallecidos_infancia_arequipa_arequipa,
       "adolescencia": fallecidos_adolescencia_arequipa_arequipa,
       "juventud": fallecidos_juventud_arequipa_arequipa,
       "adultez": fallecidos_adultez_arequipa_arequipa,
       "persona_mayor": fallecidos_persona_mayor_arequipa_arequipa
      }},

        {"name": "Camana", "positivos": positivos_arequipa_camana,"poblacion": poblacion_arequipa_camana , "hombres_infectados": positivos_hombres_arequipa_camana,"mujeres_infectados": positivos_mujeres_arequipa_camana, "fallecidos": fallecidos_arequipa_camana, "hombres_fallecidos": fallecidos_hombres_arequipa_camana,
           "mujeres_fallecidos": fallecidos_mujeres_arequipa_camana, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_camana,
       "infancia": fallecidos_infancia_arequipa_camana,
       "adolescencia": fallecidos_adolescencia_arequipa_camana,
       "juventud": fallecidos_juventud_arequipa_camana,
       "adultez": fallecidos_adultez_arequipa_camana,
       "persona_mayor": fallecidos_persona_mayor_arequipa_camana
      }},

        {"name": "Caraveli", "positivos": positivos_arequipa_caraveli,"poblacion": poblacion_arequipa_caraveli , "hombres_infectados": positivos_hombres_arequipa_caraveli,"mujeres_infectados": positivos_mujeres_arequipa_caraveli, "fallecidos": fallecidos_arequipa_caraveli, "hombres_fallecidos": fallecidos_hombres_arequipa_caraveli,
           "mujeres_fallecidos": fallecidos_mujeres_arequipa_caraveli, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_caraveli,
       "infancia": fallecidos_infancia_arequipa_caraveli,
       "adolescencia": fallecidos_adolescencia_arequipa_caraveli,
       "juventud": fallecidos_juventud_arequipa_caraveli,
       "adultez": fallecidos_adultez_arequipa_caraveli,
       "persona_mayor": fallecidos_persona_mayor_arequipa_caraveli
      }},

        {"name": "Castilla", "positivos": positivos_arequipa_castilla,"poblacion": poblacion_arequipa_castilla , "hombres_infectados": positivos_hombres_arequipa_castilla,"mujeres_infectados": positivos_mujeres_arequipa_castilla, "fallecidos": fallecidos_arequipa_castilla, "hombres_fallecidos": fallecidos_hombres_arequipa_castilla,
           "mujeres_fallecidos": fallecidos_mujeres_arequipa_castilla, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_castilla,
       "infancia": fallecidos_infancia_arequipa_castilla,
       "adolescencia": fallecidos_adolescencia_arequipa_castilla,
       "juventud": fallecidos_juventud_arequipa_castilla,
       "adultez": fallecidos_adultez_arequipa_castilla,
       "persona_mayor": fallecidos_persona_mayor_arequipa_castilla
      }},

        {"name": "Caylloma", "positivos": positivos_arequipa_caylloma,"poblacion": poblacion_arequipa_caylloma , "hombres_infectados": positivos_hombres_arequipa_caylloma,"mujeres_infectados": positivos_mujeres_arequipa_caylloma, "fallecidos": fallecidos_arequipa_caylloma, "hombres_fallecidos": fallecidos_hombres_arequipa_caylloma,
           "mujeres_fallecidos": fallecidos_mujeres_arequipa_caylloma, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_caylloma,
       "infancia": fallecidos_infancia_arequipa_caylloma,
       "adolescencia": fallecidos_adolescencia_arequipa_caylloma,
       "juventud": fallecidos_juventud_arequipa_caylloma,
       "adultez": fallecidos_adultez_arequipa_caylloma,
       "persona_mayor": fallecidos_persona_mayor_arequipa_caylloma
      }},

        {"name": "Condesuyos", "positivos": positivos_arequipa_condesuyos,"poblacion": poblacion_arequipa_condesuyos , "hombres_infectados": positivos_hombres_arequipa_condesuyos,"mujeres_infectados": positivos_mujeres_arequipa_condesuyos, "fallecidos": fallecidos_arequipa_condesuyos, "hombres_fallecidos": fallecidos_hombres_arequipa_condesuyos,
           "mujeres_fallecidos": fallecidos_mujeres_arequipa_condesuyos, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_condesuyos,
       "infancia": fallecidos_infancia_arequipa_condesuyos,
       "adolescencia": fallecidos_adolescencia_arequipa_condesuyos,
       "juventud": fallecidos_juventud_arequipa_condesuyos,
       "adultez": fallecidos_adultez_arequipa_condesuyos,
       "persona_mayor": fallecidos_persona_mayor_arequipa_condesuyos
      }},

        {"name": "Islay", "positivos": positivos_arequipa_islay,"poblacion": poblacion_arequipa_islay , "hombres_infectados": positivos_hombres_arequipa_islay,"mujeres_infectados": positivos_mujeres_arequipa_islay, "fallecidos": fallecidos_arequipa_islay, "hombres_fallecidos": fallecidos_hombres_arequipa_islay,
           "mujeres_fallecidos": fallecidos_mujeres_arequipa_islay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_islay,
       "infancia": fallecidos_infancia_arequipa_islay,
       "adolescencia": fallecidos_adolescencia_arequipa_islay,
       "juventud": fallecidos_juventud_arequipa_islay,
       "adultez": fallecidos_adultez_arequipa_islay,
       "persona_mayor": fallecidos_persona_mayor_arequipa_islay
      }},

        {"name": "La Union", "positivos": positivos_arequipa_union,"poblacion": poblacion_arequipa_union , "hombres_infectados": positivos_hombres_arequipa_union,"mujeres_infectados": positivos_mujeres_arequipa_union, "fallecidos": fallecidos_arequipa_union, "hombres_fallecidos": fallecidos_hombres_arequipa_union,
           "mujeres_fallecidos": fallecidos_mujeres_arequipa_union, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_union,
       "infancia": fallecidos_infancia_arequipa_union,
       "adolescencia": fallecidos_adolescencia_arequipa_union,
       "juventud": fallecidos_juventud_arequipa_union,
       "adultez": fallecidos_adultez_arequipa_union,
       "persona_mayor": fallecidos_persona_mayor_arequipa_union
      }}
      ]
    }
print(json.dumps(arequipa));
sys.stdout.flush();
