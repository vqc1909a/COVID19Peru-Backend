import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_cusco = 1360013
positivos_cusco = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "CUSCO"].shape)[0]
positivos_hombres_cusco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CUSCO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CUSCO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "CUSCO"].shape)[0]
fallecidos_hombres_cusco  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CUSCO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CUSCO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Departamento Cusco - Etapa de vida
fallecidos_preinfancia_cusco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincias Cusco
#!Cusco-Cusco
poblacion_cusco_cusco = 477462
positivos_cusco_cusco = list(casos_positivos[casos_positivos['PROVINCIA'] == "CUSCO"].shape)[0]
positivos_hombres_cusco_cusco = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CUSCO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_cusco = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CUSCO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_cusco = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CUSCO"].shape)[0]
fallecidos_hombres_cusco_cusco  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUSCO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_cusco  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUSCO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Cusco - Etapa de vida
fallecidos_preinfancia_cusco_cusco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_cusco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_cusco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_cusco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_cusco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_cusco = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUSCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


    
#!Cusco-Acomayo
poblacion_cusco_acomayo = 26977
positivos_cusco_acomayo = list(casos_positivos[casos_positivos['PROVINCIA'] == "ACOMAYO"].shape)[0]
positivos_hombres_cusco_acomayo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ACOMAYO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_acomayo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ACOMAYO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_acomayo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ACOMAYO"].shape)[0]
fallecidos_hombres_cusco_acomayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOMAYO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_acomayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOMAYO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Acomayo - Etapa de vida
fallecidos_preinfancia_cusco_acomayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_acomayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_acomayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_acomayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_acomayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_acomayo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Cusco-Anta
poblacion_cusco_anta = 58268
positivos_cusco_anta = list(casos_positivos[casos_positivos['PROVINCIA'] == "ANTA"].shape)[0]
positivos_hombres_cusco_anta = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ANTA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_anta = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ANTA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_anta = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ANTA"].shape)[0]
fallecidos_hombres_cusco_anta  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_anta  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Anta - Etapa de vida
fallecidos_preinfancia_cusco_anta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_anta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_anta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_anta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_anta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_anta = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Cusco-Calca
poblacion_cusco_calca = 75968
positivos_cusco_calca = list(casos_positivos[casos_positivos['PROVINCIA'] == "CALCA"].shape)[0]
positivos_hombres_cusco_calca = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CALCA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_calca = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CALCA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_calca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CALCA"].shape)[0]
fallecidos_hombres_cusco_calca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CALCA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_calca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CALCA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Calca - Etapa de vida
fallecidos_preinfancia_cusco_calca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CALCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_calca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CALCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_calca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CALCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_calca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CALCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_calca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CALCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_calca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CALCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Cusco-Canas
poblacion_cusco_canas = 38696
positivos_cusco_canas = list(casos_positivos[casos_positivos['PROVINCIA'] == "CANAS"].shape)[0]
positivos_hombres_cusco_canas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANAS") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_canas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANAS") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_canas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CANAS"].shape)[0]
fallecidos_hombres_cusco_canas  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANAS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_canas  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANAS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Canas - Etapa de vida
fallecidos_preinfancia_cusco_canas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_canas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_canas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_canas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_canas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_canas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Cusco-Canchis
poblacion_cusco_canchis = 104056
positivos_cusco_canchis = list(casos_positivos[casos_positivos['PROVINCIA'] == "CANCHIS"].shape)[0]
positivos_hombres_cusco_canchis = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANCHIS") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_canchis = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANCHIS") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_canchis = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CANCHIS"].shape)[0]
fallecidos_hombres_cusco_canchis  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANCHIS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_canchis  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANCHIS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Canchis - Etapa de vida
fallecidos_preinfancia_cusco_canchis = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANCHIS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_canchis = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANCHIS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_canchis = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANCHIS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_canchis = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANCHIS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_canchis = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANCHIS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_canchis = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANCHIS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Cusco-Chumbivilcas
poblacion_cusco_chumbivilcas = 81415
positivos_cusco_chumbivilcas = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHUMBIVILCAS"].shape)[0]
positivos_hombres_cusco_chumbivilcas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHUMBIVILCAS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_chumbivilcas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHUMBIVILCAS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_chumbivilcas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHUMBIVILCAS"].shape)[0]
fallecidos_hombres_cusco_chumbivilcas  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUMBIVILCAS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_chumbivilcas  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUMBIVILCAS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Canchis - Etapa de vida
fallecidos_preinfancia_cusco_chumbivilcas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUMBIVILCAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_chumbivilcas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUMBIVILCAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_chumbivilcas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUMBIVILCAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_chumbivilcas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUMBIVILCAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_chumbivilcas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUMBIVILCAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_chumbivilcas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUMBIVILCAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Cusco-Espinar
poblacion_cusco_espinar = 70132
positivos_cusco_espinar = list(casos_positivos[casos_positivos['PROVINCIA'] == "ESPINAR"].shape)[0]
positivos_hombres_cusco_espinar = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ESPINAR") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_espinar = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ESPINAR") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_espinar = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ESPINAR"].shape)[0]
fallecidos_hombres_cusco_espinar  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ESPINAR") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_espinar  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ESPINAR") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Espinar - Etapa de vida
fallecidos_preinfancia_cusco_espinar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ESPINAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_espinar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ESPINAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_espinar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ESPINAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_espinar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ESPINAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_espinar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ESPINAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_espinar = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ESPINAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Cusco-Convencion
poblacion_cusco_convencion = 186667
positivos_cusco_convencion = list(casos_positivos[casos_positivos['PROVINCIA'] == "LA CONVENCION"].shape)[0]
positivos_hombres_cusco_convencion = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LA CONVENCION") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_convencion = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LA CONVENCION") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_convencion = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LA CONVENCION"].shape)[0]
fallecidos_hombres_cusco_convencion  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA CONVENCION") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_convencion  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA CONVENCION") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Espinar - Etapa de vida
fallecidos_preinfancia_cusco_convencion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA CONVENCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_convencion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA CONVENCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_convencion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA CONVENCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_convencion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA CONVENCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_convencion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA CONVENCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_convencion = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA CONVENCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Cusco-Paruro
poblacion_cusco_paruro = 29818
positivos_cusco_paruro = list(casos_positivos[casos_positivos['PROVINCIA'] == "PARURO"].shape)[0]
positivos_hombres_cusco_paruro = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PARURO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_paruro = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PARURO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_paruro = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PARURO"].shape)[0]
fallecidos_hombres_cusco_paruro  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARURO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_paruro  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARURO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Paruro - Etapa de vida
fallecidos_preinfancia_cusco_paruro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARURO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_paruro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARURO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_paruro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARURO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_paruro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARURO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_paruro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARURO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_paruro = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARURO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Cusco-Paucartambo
poblacion_cusco_paucartambo = 51150
positivos_cusco_paucartambo = list(casos_positivos[casos_positivos['PROVINCIA'] == "PAUCARTAMBO"].shape)[0]
positivos_hombres_cusco_paucartambo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PAUCARTAMBO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_paucartambo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PAUCARTAMBO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_paucartambo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PAUCARTAMBO"].shape)[0]
fallecidos_hombres_cusco_paucartambo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCARTAMBO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_paucartambo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCARTAMBO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Paucartambo - Etapa de vida
fallecidos_preinfancia_cusco_paucartambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCARTAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_paucartambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCARTAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_paucartambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCARTAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_paucartambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCARTAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_paucartambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCARTAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_paucartambo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCARTAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Cusco-Quispicanchi
poblacion_cusco_quispicanchi = 92060
positivos_cusco_quispicanchi = list(casos_positivos[casos_positivos['PROVINCIA'] == "QUISPICANCHI"].shape)[0]
positivos_hombres_cusco_quispicanchi = list(casos_positivos[(casos_positivos['PROVINCIA'] == "QUISPICANCHI") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_quispicanchi = list(casos_positivos[(casos_positivos['PROVINCIA'] == "QUISPICANCHI") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_quispicanchi = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "QUISPICANCHI"].shape)[0]
fallecidos_hombres_cusco_quispicanchi  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "QUISPICANCHI") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_quispicanchi  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "QUISPICANCHI") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Paucartambo - Etapa de vida
fallecidos_preinfancia_cusco_quispicanchi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "QUISPICANCHI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_quispicanchi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "QUISPICANCHI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_quispicanchi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "QUISPICANCHI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_quispicanchi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "QUISPICANCHI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_quispicanchi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "QUISPICANCHI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_quispicanchi = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "QUISPICANCHI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Cusco-Urubamba
poblacion_cusco_urubamba = 67344
positivos_cusco_urubamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "URUBAMBA"].shape)[0]
positivos_hombres_cusco_urubamba = list(casos_positivos[(casos_positivos['PROVINCIA'] == "URUBAMBA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco_urubamba = list(casos_positivos[(casos_positivos['PROVINCIA'] == "URUBAMBA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco_urubamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "URUBAMBA"].shape)[0]
fallecidos_hombres_cusco_urubamba  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "URUBAMBA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cusco_urubamba  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "URUBAMBA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Urubamba - Etapa de vida
fallecidos_preinfancia_cusco_urubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cusco_urubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cusco_urubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cusco_urubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cusco_urubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cusco_urubamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

cusco =  {
      "name": "Cusco",
      "poblacion": poblacion_cusco,
      "positivos": positivos_cusco,
      "hombres_infectados": positivos_hombres_cusco,
      "mujeres_infectados": positivos_mujeres_cusco,
      "fallecidos": fallecidos_cusco,
      "hombres_fallecidos": fallecidos_hombres_cusco, 
      "mujeres_fallecidos": fallecidos_mujeres_cusco,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco,
       "infancia": fallecidos_infancia_cusco,
       "adolescencia": fallecidos_adolescencia_cusco,
       "juventud": fallecidos_juventud_cusco,
       "adultez": fallecidos_adultez_cusco,
       "persona_mayor": fallecidos_persona_mayor_cusco
      },
      "url": "cusco",
      "provincias": [
        {"name": "Cusco", "positivos": positivos_cusco_cusco,"poblacion": poblacion_cusco_cusco , "hombres_infectados": positivos_hombres_cusco_cusco,"mujeres_infectados": positivos_mujeres_cusco_cusco, "fallecidos": fallecidos_cusco_cusco, "hombres_fallecidos": fallecidos_hombres_cusco_cusco, "mujeres_fallecidos": fallecidos_mujeres_cusco_cusco, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_cusco,
       "infancia": fallecidos_infancia_cusco_cusco,
       "adolescencia": fallecidos_adolescencia_cusco_cusco,
       "juventud": fallecidos_juventud_cusco_cusco,
       "adultez": fallecidos_adultez_cusco_cusco,
       "persona_mayor": fallecidos_persona_mayor_cusco_cusco
      }},

        {"name": "Acomayo", "positivos": positivos_cusco_acomayo,"poblacion": poblacion_cusco_acomayo , "hombres_infectados": positivos_hombres_cusco_acomayo,"mujeres_infectados": positivos_mujeres_cusco_acomayo, "fallecidos": fallecidos_cusco_acomayo, "hombres_fallecidos": fallecidos_hombres_cusco_acomayo, "mujeres_fallecidos": fallecidos_mujeres_cusco_acomayo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_acomayo,
       "infancia": fallecidos_infancia_cusco_acomayo,
       "adolescencia": fallecidos_adolescencia_cusco_acomayo,
       "juventud": fallecidos_juventud_cusco_acomayo,
       "adultez": fallecidos_adultez_cusco_acomayo,
       "persona_mayor": fallecidos_persona_mayor_cusco_acomayo
      }},

        {"name": "Anta", "positivos": positivos_cusco_anta,"poblacion": poblacion_cusco_anta , "hombres_infectados": positivos_hombres_cusco_anta,"mujeres_infectados": positivos_mujeres_cusco_anta, "fallecidos": fallecidos_cusco_anta, "hombres_fallecidos": fallecidos_hombres_cusco_anta, "mujeres_fallecidos": fallecidos_mujeres_cusco_anta, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_anta,
       "infancia": fallecidos_infancia_cusco_anta,
       "adolescencia": fallecidos_adolescencia_cusco_anta,
       "juventud": fallecidos_juventud_cusco_anta,
       "adultez": fallecidos_adultez_cusco_anta,
       "persona_mayor": fallecidos_persona_mayor_cusco_anta
      }},

        {"name": "Calca", "positivos": positivos_cusco_calca,"poblacion": poblacion_cusco_calca , "hombres_infectados": positivos_hombres_cusco_calca,"mujeres_infectados": positivos_mujeres_cusco_calca, "fallecidos": fallecidos_cusco_calca, "hombres_fallecidos": fallecidos_hombres_cusco_calca, "mujeres_fallecidos": fallecidos_mujeres_cusco_calca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_calca,
       "infancia": fallecidos_infancia_cusco_calca,
       "adolescencia": fallecidos_adolescencia_cusco_calca,
       "juventud": fallecidos_juventud_cusco_calca,
       "adultez": fallecidos_adultez_cusco_calca,
       "persona_mayor": fallecidos_persona_mayor_cusco_calca
      }},

        {"name": "Canas", "positivos": positivos_cusco_canas,"poblacion": poblacion_cusco_canas , "hombres_infectados": positivos_hombres_cusco_canas,"mujeres_infectados": positivos_mujeres_cusco_canas, "fallecidos": fallecidos_cusco_canas, "hombres_fallecidos": fallecidos_hombres_cusco_canas, "mujeres_fallecidos": fallecidos_mujeres_cusco_canas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_canas,
       "infancia": fallecidos_infancia_cusco_canas,
       "adolescencia": fallecidos_adolescencia_cusco_canas,
       "juventud": fallecidos_juventud_cusco_canas,
       "adultez": fallecidos_adultez_cusco_canas,
       "persona_mayor": fallecidos_persona_mayor_cusco_canas
      }},

        {"name": "Canchis", "positivos": positivos_cusco_canchis,"poblacion": poblacion_cusco_canchis , "hombres_infectados": positivos_hombres_cusco_canchis,"mujeres_infectados": positivos_mujeres_cusco_canchis, "fallecidos": fallecidos_cusco_canchis, "hombres_fallecidos": fallecidos_hombres_cusco_canchis, "mujeres_fallecidos": fallecidos_mujeres_cusco_canchis, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_canchis,
       "infancia": fallecidos_infancia_cusco_canchis,
       "adolescencia": fallecidos_adolescencia_cusco_canchis,
       "juventud": fallecidos_juventud_cusco_canchis,
       "adultez": fallecidos_adultez_cusco_canchis,
       "persona_mayor": fallecidos_persona_mayor_cusco_canchis
      }},

        {"name": "Chumbivilcas", "positivos": positivos_cusco_chumbivilcas,"poblacion": poblacion_cusco_chumbivilcas , "hombres_infectados": positivos_hombres_cusco_chumbivilcas,"mujeres_infectados": positivos_mujeres_cusco_chumbivilcas, "fallecidos": fallecidos_cusco_chumbivilcas, "hombres_fallecidos": fallecidos_hombres_cusco_chumbivilcas, "mujeres_fallecidos": fallecidos_mujeres_cusco_chumbivilcas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_chumbivilcas,
       "infancia": fallecidos_infancia_cusco_chumbivilcas,
       "adolescencia": fallecidos_adolescencia_cusco_chumbivilcas,
       "juventud": fallecidos_juventud_cusco_chumbivilcas,
       "adultez": fallecidos_adultez_cusco_chumbivilcas,
       "persona_mayor": fallecidos_persona_mayor_cusco_chumbivilcas
      }},

        {"name": "Espinar", "positivos": positivos_cusco_espinar,"poblacion": poblacion_cusco_espinar , "hombres_infectados": positivos_hombres_cusco_espinar,"mujeres_infectados": positivos_mujeres_cusco_espinar, "fallecidos": fallecidos_cusco_espinar, "hombres_fallecidos": fallecidos_hombres_cusco_espinar, "mujeres_fallecidos": fallecidos_mujeres_cusco_espinar, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_espinar,
       "infancia": fallecidos_infancia_cusco_espinar,
       "adolescencia": fallecidos_adolescencia_cusco_espinar,
       "juventud": fallecidos_juventud_cusco_espinar,
       "adultez": fallecidos_adultez_cusco_espinar,
       "persona_mayor": fallecidos_persona_mayor_cusco_espinar
      }},

        {"name": "La Convencion", "positivos": positivos_cusco_convencion,"poblacion": poblacion_cusco_convencion , "hombres_infectados": positivos_hombres_cusco_convencion,"mujeres_infectados": positivos_mujeres_cusco_convencion, "fallecidos": fallecidos_cusco_convencion, "hombres_fallecidos": fallecidos_hombres_cusco_convencion, "mujeres_fallecidos": fallecidos_mujeres_cusco_convencion, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_convencion,
       "infancia": fallecidos_infancia_cusco_convencion,
       "adolescencia": fallecidos_adolescencia_cusco_convencion,
       "juventud": fallecidos_juventud_cusco_convencion,
       "adultez": fallecidos_adultez_cusco_convencion,
       "persona_mayor": fallecidos_persona_mayor_cusco_convencion
      }},

        {"name": "Paruro", "positivos": positivos_cusco_paruro,"poblacion": poblacion_cusco_paruro , "hombres_infectados": positivos_hombres_cusco_paruro,"mujeres_infectados": positivos_mujeres_cusco_paruro, "fallecidos": fallecidos_cusco_paruro, "hombres_fallecidos": fallecidos_hombres_cusco_paruro, "mujeres_fallecidos": fallecidos_mujeres_cusco_paruro, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_paruro,
       "infancia": fallecidos_infancia_cusco_paruro,
       "adolescencia": fallecidos_adolescencia_cusco_paruro,
       "juventud": fallecidos_juventud_cusco_paruro,
       "adultez": fallecidos_adultez_cusco_paruro,
       "persona_mayor": fallecidos_persona_mayor_cusco_paruro
      }},

        {"name": "Paucartambo", "positivos": positivos_cusco_paucartambo,"poblacion": poblacion_cusco_paucartambo , "hombres_infectados": positivos_hombres_cusco_paucartambo,"mujeres_infectados": positivos_mujeres_cusco_paucartambo, "fallecidos": fallecidos_cusco_paucartambo, "hombres_fallecidos": fallecidos_hombres_cusco_paucartambo, "mujeres_fallecidos": fallecidos_mujeres_cusco_paucartambo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_paucartambo,
       "infancia": fallecidos_infancia_cusco_paucartambo,
       "adolescencia": fallecidos_adolescencia_cusco_paucartambo,
       "juventud": fallecidos_juventud_cusco_paucartambo,
       "adultez": fallecidos_adultez_cusco_paucartambo,
       "persona_mayor": fallecidos_persona_mayor_cusco_paucartambo
      }},

        {"name": "Quispicanchi", "positivos": positivos_cusco_quispicanchi,"poblacion": poblacion_cusco_quispicanchi , "hombres_infectados": positivos_hombres_cusco_quispicanchi,"mujeres_infectados": positivos_mujeres_cusco_quispicanchi, "fallecidos": fallecidos_cusco_quispicanchi, "hombres_fallecidos": fallecidos_hombres_cusco_quispicanchi, "mujeres_fallecidos": fallecidos_mujeres_cusco_quispicanchi, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_quispicanchi,
       "infancia": fallecidos_infancia_cusco_quispicanchi,
       "adolescencia": fallecidos_adolescencia_cusco_quispicanchi,
       "juventud": fallecidos_juventud_cusco_quispicanchi,
       "adultez": fallecidos_adultez_cusco_quispicanchi,
       "persona_mayor": fallecidos_persona_mayor_cusco_quispicanchi
      }},

        {"name": "Urubamba", "positivos": positivos_cusco_urubamba,"poblacion": poblacion_cusco_urubamba , "hombres_infectados": positivos_hombres_cusco_urubamba,"mujeres_infectados": positivos_mujeres_cusco_urubamba, "fallecidos": fallecidos_cusco_urubamba, "hombres_fallecidos": fallecidos_hombres_cusco_urubamba, "mujeres_fallecidos": fallecidos_mujeres_cusco_urubamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_urubamba,
       "infancia": fallecidos_infancia_cusco_urubamba,
       "adolescencia": fallecidos_adolescencia_cusco_urubamba,
       "juventud": fallecidos_juventud_cusco_urubamba,
       "adultez": fallecidos_adultez_cusco_urubamba,
       "persona_mayor": fallecidos_persona_mayor_cusco_urubamba
      }}
      ]
    }

print(json.dumps(cusco));
sys.stdout.flush();