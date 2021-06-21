import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_cajamarca = 1446823
positivos_cajamarca = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "CAJAMARCA"].shape)[0]
positivos_hombres_cajamarca = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CAJAMARCA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cajamarca = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CAJAMARCA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cajamarca = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "CAJAMARCA"].shape)[0]
fallecidos_hombres_cajamarca  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CAJAMARCA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CAJAMARCA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Cajamarca - Etapa de vida
fallecidos_preinfancia_cajamarca = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Cajamarca
#!Cajamarca-Cajamarca
poblacion_cajamarca_cajamarca = 374714
positivos_cajamarca_cajamarca = list(casos_positivos[casos_positivos['PROVINCIA'] == "CAJAMARCA"].shape)[0]
positivos_hombres_cajamarca_cajamarca = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CAJAMARCA")].shape)[0]
positivos_mujeres_cajamarca_cajamarca = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CAJAMARCA")].shape)[0]
fallecidos_cajamarca_cajamarca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CAJAMARCA"].shape)[0]
fallecidos_hombres_cajamarca_cajamarca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJAMARCA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_cajamarca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJAMARCA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Cajamarca - Etapa de vida
fallecidos_preinfancia_cajamarca_cajamarca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_cajamarca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_cajamarca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_cajamarca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_cajamarca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_cajamarca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJAMARCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]
    
#!Cajamarca-Cajabamba
poblacion_cajamarca_cajabamba = 77369
positivos_cajamarca_cajabamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "CAJABAMBA"].shape)[0]
positivos_hombres_cajamarca_cajabamba = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CAJABAMBA")].shape)[0]
positivos_mujeres_cajamarca_cajabamba = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CAJABAMBA")].shape)[0]
fallecidos_cajamarca_cajabamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CAJABAMBA"].shape)[0]
fallecidos_hombres_cajamarca_cajabamba  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJABAMBA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_cajabamba  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJABAMBA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Cajabamba - Etapa de vida
fallecidos_preinfancia_cajamarca_cajabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_cajabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_cajabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_cajabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_cajabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_cajabamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]
    
#!Cajamarca-Celendin
poblacion_cajamarca_celendin = 89342
positivos_cajamarca_celendin = list(casos_positivos[casos_positivos['PROVINCIA'] == "CELENDIN"].shape)[0]
positivos_hombres_cajamarca_celendin = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CELENDIN")].shape)[0]
positivos_mujeres_cajamarca_celendin = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CELENDIN")].shape)[0]
fallecidos_cajamarca_celendin = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CELENDIN"].shape)[0]
fallecidos_hombres_cajamarca_celendin  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CELENDIN") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_celendin  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CELENDIN") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Celendin - Etapa de vida
fallecidos_preinfancia_cajamarca_celendin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CELENDIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_celendin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CELENDIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_celendin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CELENDIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_celendin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CELENDIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_celendin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CELENDIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_celendin = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CELENDIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Cajamarca-Chota
poblacion_cajamarca_chota = 153867
positivos_cajamarca_chota = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHOTA"].shape)[0]
positivos_hombres_cajamarca_chota = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CHOTA")].shape)[0]
positivos_mujeres_cajamarca_chota = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CHOTA")].shape)[0]
fallecidos_cajamarca_chota = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHOTA"].shape)[0]
fallecidos_hombres_cajamarca_chota  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHOTA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_chota  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHOTA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Chota - Etapa de vida
fallecidos_preinfancia_cajamarca_chota = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_chota = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_chota = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_chota = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_chota = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_chota = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]
    
#!Cajamarca-Contumaza
poblacion_cajamarca_contumaza = 29384
positivos_cajamarca_contumaza = list(casos_positivos[casos_positivos['PROVINCIA'] == "CONTUMAZA"].shape)[0]
positivos_hombres_cajamarca_contumaza = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CONTUMAZA")].shape)[0]
positivos_mujeres_cajamarca_contumaza = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CONTUMAZA")].shape)[0]
fallecidos_cajamarca_contumaza = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CONTUMAZA"].shape)[0]
fallecidos_hombres_cajamarca_contumaza  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHOTA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_contumaza  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHOTA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Contumaza - Etapa de vida
fallecidos_preinfancia_cajamarca_contumaza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTUMAZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_contumaza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTUMAZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_contumaza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTUMAZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_contumaza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTUMAZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_contumaza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTUMAZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_contumaza = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTUMAZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Cajamarca-Cutervo
poblacion_cajamarca_cutervo = 129913
positivos_cajamarca_cutervo = list(casos_positivos[casos_positivos['PROVINCIA'] == "CUTERVO"].shape)[0]
positivos_hombres_cajamarca_cutervo = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CUTERVO")].shape)[0]
positivos_mujeres_cajamarca_cutervo = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CUTERVO")].shape)[0]
fallecidos_cajamarca_cutervo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CUTERVO"].shape)[0]
fallecidos_hombres_cajamarca_cutervo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUTERVO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_cutervo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUTERVO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Cutervo - Etapa de vida
fallecidos_preinfancia_cajamarca_cutervo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUTERVO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_cutervo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUTERVO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_cutervo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUTERVO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_cutervo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUTERVO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_cutervo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUTERVO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_cutervo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CUTERVO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Cajamarca-Hualgayoc
poblacion_cajamarca_hualgayoc = 95820
positivos_cajamarca_hualgayoc = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUALGAYOC"].shape)[0]
positivos_hombres_cajamarca_hualgayoc = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUALGAYOC")].shape)[0]
positivos_mujeres_cajamarca_hualgayoc = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUALGAYOC")].shape)[0]
fallecidos_cajamarca_hualgayoc = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUALGAYOC"].shape)[0]
fallecidos_hombres_cajamarca_hualgayoc  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALGAYOC") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_hualgayoc  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALGAYOC") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Hualgayoc - Etapa de vida
fallecidos_preinfancia_cajamarca_hualgayoc = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALGAYOC") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_hualgayoc = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALGAYOC") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_hualgayoc = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALGAYOC") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_hualgayoc = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALGAYOC") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_hualgayoc = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALGAYOC") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_hualgayoc = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALGAYOC") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Cajamarca-Jaen
poblacion_cajamarca_jaen = 191230
positivos_cajamarca_jaen = list(casos_positivos[casos_positivos['PROVINCIA'] == "JAEN"].shape)[0]
positivos_hombres_cajamarca_jaen = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "JAEN")].shape)[0]
positivos_mujeres_cajamarca_jaen = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "JAEN")].shape)[0]
fallecidos_cajamarca_jaen = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "JAEN"].shape)[0]
fallecidos_hombres_cajamarca_jaen  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAEN") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_jaen  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAEN") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Jaen - Etapa de vida
fallecidos_preinfancia_cajamarca_jaen = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_jaen = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_jaen = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_jaen = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_jaen = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_jaen = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Cajamarca-San Ignacio
poblacion_cajamarca_san_ignacio = 138248
positivos_cajamarca_san_ignacio = list(casos_positivos[casos_positivos['PROVINCIA'] == "SAN IGNACIO"].shape)[0]
positivos_hombres_cajamarca_san_ignacio = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SAN IGNACIO")].shape)[0]
positivos_mujeres_cajamarca_san_ignacio = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SAN IGNACIO")].shape)[0]
fallecidos_cajamarca_san_ignacio = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SAN IGNACIO"].shape)[0]
fallecidos_hombres_cajamarca_san_ignacio  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN IGNACIO") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_san_ignacio  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN IGNACIO") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia San Ignacio - Etapa de vida
fallecidos_preinfancia_cajamarca_san_ignacio = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN IGNACIO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_san_ignacio = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN IGNACIO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_san_ignacio = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN IGNACIO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_san_ignacio = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN IGNACIO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_san_ignacio = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN IGNACIO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_san_ignacio = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN IGNACIO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Cajamarca-San Marcos
poblacion_cajamarca_san_marcos = 51750
positivos_cajamarca_san_marcos = list(casos_positivos[casos_positivos['PROVINCIA'] == "SAN MARCOS"].shape)[0]
positivos_hombres_cajamarca_san_marcos = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SAN MARCOS")].shape)[0]
positivos_mujeres_cajamarca_san_marcos = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SAN MARCOS")].shape)[0]
fallecidos_cajamarca_san_marcos = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SAN MARCOS"].shape)[0]
fallecidos_hombres_cajamarca_san_marcos  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARCOS") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_san_marcos  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARCOS") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia San Marcos - Etapa de vida
fallecidos_preinfancia_cajamarca_san_marcos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_san_marcos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_san_marcos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_san_marcos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_san_marcos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_san_marcos = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Cajamarca-San Miguel
poblacion_cajamarca_san_miguel = 51435
positivos_cajamarca_san_miguel = list(casos_positivos[casos_positivos['PROVINCIA'] == "SAN MIGUEL"].shape)[0]
positivos_hombres_cajamarca_san_miguel = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SAN MIGUEL")].shape)[0]
positivos_mujeres_cajamarca_san_miguel = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SAN MIGUEL")].shape)[0]
fallecidos_cajamarca_san_miguel = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SAN MIGUEL"].shape)[0]
fallecidos_hombres_cajamarca_san_miguel  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MIGUEL") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_san_miguel  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MIGUEL") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia San Miguel - Etapa de vida
fallecidos_preinfancia_cajamarca_san_miguel = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MIGUEL") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_san_miguel = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MIGUEL") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_san_miguel = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MIGUEL") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_san_miguel = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MIGUEL") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_san_miguel = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MIGUEL") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_san_miguel = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MIGUEL") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Cajamarca-San Pablo
poblacion_cajamarca_san_pablo = 21645
positivos_cajamarca_san_pablo = list(casos_positivos[casos_positivos['PROVINCIA'] == "SAN PABLO"].shape)[0]
positivos_hombres_cajamarca_san_pablo = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SAN PABLO")].shape)[0]
positivos_mujeres_cajamarca_san_pablo = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SAN PABLO")].shape)[0]
fallecidos_cajamarca_san_pablo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SAN PABLO"].shape)[0]
fallecidos_hombres_cajamarca_san_pablo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN PABLO") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_san_pablo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN PABLO") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia San Pablo - Etapa de vida
fallecidos_preinfancia_cajamarca_san_pablo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN PABLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_san_pablo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN PABLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_san_pablo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN PABLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_san_pablo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN PABLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_san_pablo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN PABLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_san_pablo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN PABLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Cajamarca-Santa Cruz
poblacion_cajamarca_santa_cruz = 42106
positivos_cajamarca_santa_cruz = list(casos_positivos[casos_positivos['PROVINCIA'] == "SANTA CRUZ"].shape)[0]
positivos_hombres_cajamarca_santa_cruz = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SANTA CRUZ")].shape)[0]
positivos_mujeres_cajamarca_santa_cruz = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SANTA CRUZ")].shape)[0]
fallecidos_cajamarca_santa_cruz = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SANTA CRUZ"].shape)[0]
fallecidos_hombres_cajamarca_santa_cruz  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA CRUZ") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_cajamarca_santa_cruz  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA CRUZ") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Santa Cruz - Etapa de vida
fallecidos_preinfancia_cajamarca_santa_cruz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA CRUZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_cajamarca_santa_cruz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA CRUZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_cajamarca_santa_cruz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA CRUZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_cajamarca_santa_cruz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA CRUZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_cajamarca_santa_cruz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA CRUZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_cajamarca_santa_cruz = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA CRUZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0];

cajamarca =  {
      "name": "Cajamarca",
      "poblacion": poblacion_cajamarca,
      "positivos": positivos_cajamarca,
      "hombres_infectados": positivos_hombres_cajamarca,
      "mujeres_infectados": positivos_mujeres_cajamarca,
      "fallecidos": fallecidos_cajamarca,
      "hombres_fallecidos": fallecidos_hombres_cajamarca,
      "mujeres_fallecidos": fallecidos_mujeres_cajamarca,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca,
       "infancia": fallecidos_infancia_cajamarca,
       "adolescencia": fallecidos_adolescencia_cajamarca,
       "juventud": fallecidos_juventud_cajamarca,
       "adultez": fallecidos_adultez_cajamarca,
       "persona_mayor": fallecidos_persona_mayor_cajamarca
      },
      "url": "cajamarca",
      "provincias": [
          {"name": "Cajamarca", "positivos": positivos_cajamarca_cajamarca, "poblacion": poblacion_cajamarca_cajamarca, "hombres_infectados": positivos_hombres_cajamarca_cajamarca, "mujeres_infectados": positivos_mujeres_cajamarca_cajamarca, "fallecidos": fallecidos_cajamarca_cajamarca, "hombres_fallecidos": fallecidos_hombres_cajamarca_cajamarca,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_cajamarca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_cajamarca,
       "infancia": fallecidos_infancia_cajamarca_cajamarca,
       "adolescencia": fallecidos_adolescencia_cajamarca_cajamarca,
       "juventud": fallecidos_juventud_cajamarca_cajamarca,
       "adultez": fallecidos_adultez_cajamarca_cajamarca,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_cajamarca
      }},

          {"name": "Cajabamba", "positivos": positivos_cajamarca_cajabamba,"poblacion": poblacion_cajamarca_cajabamba , "hombres_infectados": positivos_hombres_cajamarca_cajabamba,"mujeres_infectados": positivos_mujeres_cajamarca_cajabamba, "fallecidos": fallecidos_cajamarca_cajabamba, "hombres_fallecidos": fallecidos_hombres_cajamarca_cajabamba,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_cajabamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_cajabamba,
       "infancia": fallecidos_infancia_cajamarca_cajabamba,
       "adolescencia": fallecidos_adolescencia_cajamarca_cajabamba,
       "juventud": fallecidos_juventud_cajamarca_cajabamba,
       "adultez": fallecidos_adultez_cajamarca_cajabamba,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_cajabamba
      }},

          {"name": "Celendin", "positivos": positivos_cajamarca_celendin,"poblacion": poblacion_cajamarca_celendin , "hombres_infectados": positivos_hombres_cajamarca_celendin,"mujeres_infectados": positivos_mujeres_cajamarca_celendin, "fallecidos": fallecidos_cajamarca_celendin, "hombres_fallecidos": fallecidos_hombres_cajamarca_celendin,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_celendin, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_celendin,
       "infancia": fallecidos_infancia_cajamarca_celendin,
       "adolescencia": fallecidos_adolescencia_cajamarca_celendin,
       "juventud": fallecidos_juventud_cajamarca_celendin,
       "adultez": fallecidos_adultez_cajamarca_celendin,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_celendin
      }},

          {"name": "Chota", "positivos": positivos_cajamarca_chota,"poblacion": poblacion_cajamarca_chota, "hombres_infectados": positivos_hombres_cajamarca_chota,"mujeres_infectados": positivos_mujeres_cajamarca_chota, "fallecidos": fallecidos_cajamarca_chota, "hombres_fallecidos": fallecidos_hombres_cajamarca_chota,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_chota, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_chota,
       "infancia": fallecidos_infancia_cajamarca_chota,
       "adolescencia": fallecidos_adolescencia_cajamarca_chota,
       "juventud": fallecidos_juventud_cajamarca_chota,
       "adultez": fallecidos_adultez_cajamarca_chota,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_chota
      }},

          {"name": "Contumaza", "positivos": positivos_cajamarca_contumaza,"poblacion": poblacion_cajamarca_contumaza, "hombres_infectados": positivos_hombres_cajamarca_contumaza,"mujeres_infectados": positivos_mujeres_cajamarca_contumaza, "fallecidos": fallecidos_cajamarca_contumaza, "hombres_fallecidos": fallecidos_hombres_cajamarca_contumaza,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_contumaza, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_contumaza,
       "infancia": fallecidos_infancia_cajamarca_contumaza,
       "adolescencia": fallecidos_adolescencia_cajamarca_contumaza,
       "juventud": fallecidos_juventud_cajamarca_contumaza,
       "adultez": fallecidos_adultez_cajamarca_contumaza,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_contumaza
      }},

          {"name": "Cutervo", "positivos": positivos_cajamarca_cutervo,"poblacion": poblacion_cajamarca_cutervo, "hombres_infectados": positivos_hombres_cajamarca_cutervo,"mujeres_infectados": positivos_mujeres_cajamarca_cutervo, "fallecidos": fallecidos_cajamarca_cutervo, "hombres_fallecidos": fallecidos_hombres_cajamarca_cutervo,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_cutervo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_cutervo,
       "infancia": fallecidos_infancia_cajamarca_cutervo,
       "adolescencia": fallecidos_adolescencia_cajamarca_cutervo,
       "juventud": fallecidos_juventud_cajamarca_cutervo,
       "adultez": fallecidos_adultez_cajamarca_cutervo,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_cutervo
      }},

          {"name": "Hualgayoc", "positivos": positivos_cajamarca_hualgayoc,"poblacion": poblacion_cajamarca_hualgayoc, "hombres_infectados": positivos_hombres_cajamarca_hualgayoc,"mujeres_infectados": positivos_mujeres_cajamarca_hualgayoc, "fallecidos": fallecidos_cajamarca_hualgayoc, "hombres_fallecidos": fallecidos_hombres_cajamarca_hualgayoc,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_hualgayoc, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_hualgayoc,
       "infancia": fallecidos_infancia_cajamarca_hualgayoc,
       "adolescencia": fallecidos_adolescencia_cajamarca_hualgayoc,
       "juventud": fallecidos_juventud_cajamarca_hualgayoc,
       "adultez": fallecidos_adultez_cajamarca_hualgayoc,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_hualgayoc
      }},

          {"name": "Jaen", "positivos": positivos_cajamarca_jaen,"poblacion": poblacion_cajamarca_jaen, "hombres_infectados": positivos_hombres_cajamarca_jaen,"mujeres_infectados": positivos_mujeres_cajamarca_jaen, "fallecidos": fallecidos_cajamarca_jaen, "hombres_fallecidos": fallecidos_hombres_cajamarca_jaen,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_jaen, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_jaen,
       "infancia": fallecidos_infancia_cajamarca_jaen,
       "adolescencia": fallecidos_adolescencia_cajamarca_jaen,
       "juventud": fallecidos_juventud_cajamarca_jaen,
       "adultez": fallecidos_adultez_cajamarca_jaen,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_jaen
       }},

          {"name": "San Ignacio", "positivos": positivos_cajamarca_san_ignacio,"poblacion": poblacion_cajamarca_san_ignacio, "hombres_infectados": positivos_hombres_cajamarca_san_ignacio,"mujeres_infectados": positivos_mujeres_cajamarca_san_ignacio, "fallecidos": fallecidos_cajamarca_san_ignacio, "hombres_fallecidos": fallecidos_hombres_cajamarca_san_ignacio,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_san_ignacio, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_san_ignacio,
       "infancia": fallecidos_infancia_cajamarca_san_ignacio,
       "adolescencia": fallecidos_adolescencia_cajamarca_san_ignacio,
       "juventud": fallecidos_juventud_cajamarca_san_ignacio,
       "adultez": fallecidos_adultez_cajamarca_san_ignacio,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_san_ignacio
      }}, 

          {"name": "San Marcos", "positivos": positivos_cajamarca_san_marcos, "poblacion": poblacion_cajamarca_san_marcos, "hombres_infectados": positivos_hombres_cajamarca_san_marcos, "mujeres_infectados": positivos_mujeres_cajamarca_san_marcos, "fallecidos": fallecidos_cajamarca_san_marcos, "hombres_fallecidos": fallecidos_hombres_cajamarca_san_marcos,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_san_marcos, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_san_marcos,
       "infancia": fallecidos_infancia_cajamarca_san_marcos,
       "adolescencia": fallecidos_adolescencia_cajamarca_san_marcos,
       "juventud": fallecidos_juventud_cajamarca_san_marcos,
       "adultez": fallecidos_adultez_cajamarca_san_marcos,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_san_marcos
      }},

          {"name": "San Miguel", "positivos": positivos_cajamarca_san_miguel,"poblacion": poblacion_cajamarca_san_miguel, "hombres_infectados": positivos_hombres_cajamarca_san_miguel,"mujeres_infectados": positivos_mujeres_cajamarca_san_miguel, "fallecidos": fallecidos_cajamarca_san_miguel, "hombres_fallecidos": fallecidos_hombres_cajamarca_san_miguel,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_san_miguel, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_san_miguel,
       "infancia": fallecidos_infancia_cajamarca_san_miguel,
       "adolescencia": fallecidos_adolescencia_cajamarca_san_miguel,
       "juventud": fallecidos_juventud_cajamarca_san_miguel,
       "adultez": fallecidos_adultez_cajamarca_san_miguel,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_san_miguel
      }},

          {"name": "San Pablo", "positivos": positivos_cajamarca_san_pablo,"poblacion": poblacion_cajamarca_san_pablo, "hombres_infectados": positivos_hombres_cajamarca_san_pablo,"mujeres_infectados": positivos_mujeres_cajamarca_san_pablo, "fallecidos": fallecidos_cajamarca_san_pablo, "hombres_fallecidos": fallecidos_hombres_cajamarca_san_pablo,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_san_pablo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_san_pablo,
       "infancia": fallecidos_infancia_cajamarca_san_pablo,
       "adolescencia": fallecidos_adolescencia_cajamarca_san_pablo,
       "juventud": fallecidos_juventud_cajamarca_san_pablo,
       "adultez": fallecidos_adultez_cajamarca_san_pablo,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_san_pablo
      }},

          {"name": "Santa Cruz", "positivos": positivos_cajamarca_santa_cruz,"poblacion": poblacion_cajamarca_santa_cruz, "hombres_infectados": positivos_hombres_cajamarca_santa_cruz,"mujeres_infectados": positivos_mujeres_cajamarca_santa_cruz, "fallecidos": fallecidos_cajamarca_santa_cruz, "hombres_fallecidos": fallecidos_hombres_cajamarca_santa_cruz,
           "mujeres_fallecidos": fallecidos_mujeres_cajamarca_santa_cruz, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_santa_cruz,
       "infancia": fallecidos_infancia_cajamarca_santa_cruz,
       "adolescencia": fallecidos_adolescencia_cajamarca_santa_cruz,
       "juventud": fallecidos_juventud_cajamarca_santa_cruz,
       "adultez": fallecidos_adultez_cajamarca_santa_cruz,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_santa_cruz
      }}
      ]
    }

print(json.dumps(cajamarca));
sys.stdout.flush();
