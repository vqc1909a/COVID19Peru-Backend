import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

#!Departamento Puno
poblacion_puno = 1214793
positivos_puno = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "PUNO"].shape)[0]
positivos_hombres_puno = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PUNO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PUNO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "PUNO"].shape)[0]
fallecidos_hombres_puno  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PUNO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PUNO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Puno - Etapa de vida
fallecidos_preinfancia_puno = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincias Puno
#!Puno-Puno
poblacion_puno_puno = 212107
positivos_puno_puno = list(casos_positivos[casos_positivos['PROVINCIA'] == "PUNO"].shape)[0]
positivos_hombres_puno_puno = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PUNO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_puno = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PUNO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_puno = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PUNO"].shape)[0]
fallecidos_hombres_puno_puno  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUNO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_puno  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUNO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Puno - Etapa de vida
fallecidos_preinfancia_puno_puno = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_puno = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_puno = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_puno = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_puno = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_puno = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUNO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Puno-Azangaro
poblacion_puno_azangaro = 113872
positivos_puno_azangaro = list(casos_positivos[casos_positivos['PROVINCIA'] == "AZANGARO"].shape)[0]
positivos_hombres_puno_azangaro = list(casos_positivos[(casos_positivos['PROVINCIA'] == "AZANGARO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_azangaro = list(casos_positivos[(casos_positivos['PROVINCIA'] == "AZANGARO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_azangaro = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "AZANGARO"].shape)[0]
fallecidos_hombres_puno_azangaro  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AZANGARO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_azangaro = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "AZANGARO") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Azangaro - Etapa de vida
fallecidos_preinfancia_puno_azangaro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AZANGARO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_azangaro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AZANGARO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_azangaro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AZANGARO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_azangaro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AZANGARO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_azangaro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AZANGARO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_azangaro = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AZANGARO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Puno-Carabaya
poblacion_puno_carabaya = 77566
positivos_puno_carabaya = list(casos_positivos[casos_positivos['PROVINCIA'] == "CARABAYA"].shape)[0]
positivos_hombres_puno_carabaya = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CARABAYA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_carabaya = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CARABAYA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_carabaya = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CARABAYA"].shape)[0]
fallecidos_hombres_puno_carabaya  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARABAYA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_carabaya  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARABAYA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Carabaya - Etapa de vida
fallecidos_preinfancia_puno_carabaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARABAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_carabaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARABAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_carabaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARABAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_carabaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARABAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_carabaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARABAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_carabaya = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARABAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Puno-Chucuito
poblacion_puno_chucuito = 118077
positivos_puno_chucuito = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHUCUITO"].shape)[0]
positivos_hombres_puno_chucuito = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHUCUITO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_chucuito = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHUCUITO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_chucuito = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHUCUITO"].shape)[0]
fallecidos_hombres_puno_chucuito  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUCUITO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_chucuito  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUCUITO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Chucuito - Etapa de vida
fallecidos_preinfancia_puno_chucuito = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUCUITO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_chucuito = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUCUITO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_chucuito = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUCUITO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_chucuito = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUCUITO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_chucuito = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUCUITO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_chucuito = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUCUITO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Puno-Collao
poblacion_puno_collao = 73446
positivos_puno_collao = list(casos_positivos[casos_positivos['PROVINCIA'] == "EL COLLAO"].shape)[0]
positivos_hombres_puno_collao = list(casos_positivos[(casos_positivos['PROVINCIA'] == "EL COLLAO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_collao = list(casos_positivos[(casos_positivos['PROVINCIA'] == "EL COLLAO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_collao = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "EL COLLAO"].shape)[0]
fallecidos_hombres_puno_collao  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL COLLAO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_collao  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL COLLAO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Collao - Etapa de vida
fallecidos_preinfancia_puno_collao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL COLLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_collao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL COLLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_collao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL COLLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_collao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL COLLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_collao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL COLLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_collao = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL COLLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Puno-Huancane
poblacion_puno_huancane = 53467
positivos_puno_huancane = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUANCANE"].shape)[0]
positivos_hombres_puno_huancane = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANCANE") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_huancane = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANCANE") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_huancane = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUANCANE"].shape)[0]
fallecidos_hombres_puno_huancane  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCANE") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_huancane  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCANE") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Huancane - Etapa de vida
fallecidos_preinfancia_puno_huancane = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCANE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_huancane = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCANE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_huancane = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCANE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_huancane = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCANE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_huancane = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCANE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_huancane = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCANE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]
    

#!Puno-Lampa
poblacion_puno_lampa = 42635
positivos_puno_lampa = list(casos_positivos[casos_positivos['PROVINCIA'] == "LAMPA"].shape)[0]
positivos_hombres_puno_lampa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LAMPA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_lampa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LAMPA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_lampa = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LAMPA"].shape)[0]
fallecidos_hombres_puno_lampa  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMPA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_lampa  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMPA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Huancane - Etapa de vida
fallecidos_preinfancia_puno_lampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_lampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_lampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_lampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_lampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_lampa = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Puno-Melgar
poblacion_puno_melgar = 64364
positivos_puno_melgar = list(casos_positivos[casos_positivos['PROVINCIA'] == "MELGAR"].shape)[0]
positivos_hombres_puno_melgar = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MELGAR") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_melgar = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MELGAR") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_melgar = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MELGAR"].shape)[0]
fallecidos_hombres_puno_melgar  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MELGAR") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_melgar  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MELGAR") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Melgar - Etapa de vida
fallecidos_preinfancia_puno_melgar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MELGAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_melgar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MELGAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_melgar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MELGAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_melgar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MELGAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_melgar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MELGAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_melgar = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MELGAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Puno Moho
poblacion_puno_moho = 20877
positivos_puno_moho = list(casos_positivos[casos_positivos['PROVINCIA'] == "MOHO"].shape)[0]
positivos_hombres_puno_moho = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MOHO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_moho = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MOHO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_moho = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MOHO"].shape)[0]
fallecidos_hombres_puno_moho  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOHO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_moho  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOHO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Moho - Etapa de vida
fallecidos_preinfancia_puno_moho = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_moho = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_moho = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_moho = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_moho = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_moho = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Puno-San Antonio de Putina
poblacion_puno_san_antonio_de_putina = 56589
positivos_puno_san_antonio_de_putina = list(casos_positivos[casos_positivos['PROVINCIA'] == "SAN ANTONIO DE PUTINA"].shape)[0]
positivos_hombres_puno_san_antonio_de_putina = list(casos_positivos[(casos_positivos['PROVINCIA'] == "SAN ANTONIO DE PUTINA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_san_antonio_de_putina = list(casos_positivos[(casos_positivos['PROVINCIA'] == "SAN ANTONIO DE PUTINA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_san_antonio_de_putina = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SAN ANTONIO DE PUTINA"].shape)[0]
fallecidos_hombres_puno_san_antonio_de_putina  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ANTONIO DE PUTINA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_san_antonio_de_putina  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ANTONIO DE PUTINA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia San Antonio de Putina - Etapa de vida
fallecidos_preinfancia_puno_san_antonio_de_putina = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ANTONIO DE PUTINA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_san_antonio_de_putina = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ANTONIO DE PUTINA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_san_antonio_de_putina = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ANTONIO DE PUTINA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_san_antonio_de_putina = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ANTONIO DE PUTINA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_san_antonio_de_putina = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ANTONIO DE PUTINA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_san_antonio_de_putina = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ANTONIO DE PUTINA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Puno-San Roman
poblacion_puno_san_roman = 286778
positivos_puno_san_roman = list(casos_positivos[casos_positivos['PROVINCIA'] == "SAN ROMAN"].shape)[0]
positivos_hombres_puno_san_roman = list(casos_positivos[(casos_positivos['PROVINCIA'] == "SAN ROMAN") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_san_roman = list(casos_positivos[(casos_positivos['PROVINCIA'] == "SAN ROMAN") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_san_roman = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SAN ROMAN"].shape)[0]
fallecidos_hombres_puno_san_roman  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ROMAN") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_san_roman  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ROMAN") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia San Roman - Etapa de vida
fallecidos_preinfancia_puno_san_roman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ROMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_san_roman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ROMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_san_roman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ROMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_san_roman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ROMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_san_roman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ROMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_san_roman = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN ROMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Puno-Sandia
poblacion_puno_sandia = 57095
positivos_puno_sandia = list(casos_positivos[casos_positivos['PROVINCIA'] == "SANDIA"].shape)[0]
positivos_hombres_puno_sandia = list(casos_positivos[(casos_positivos['PROVINCIA'] == "SANDIA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_sandia = list(casos_positivos[(casos_positivos['PROVINCIA'] == "SANDIA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_sandia = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SANDIA"].shape)[0]
fallecidos_hombres_puno_sandia  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANDIA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_sandia  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANDIA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Sandia - Etapa de vida
fallecidos_preinfancia_puno_sandia = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANDIA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_sandia = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANDIA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_sandia = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANDIA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_sandia = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANDIA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_sandia = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANDIA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_sandia = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANDIA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Puno-Yunguyo
poblacion_puno_yunguyo = 37920
positivos_puno_yunguyo = list(casos_positivos[casos_positivos['PROVINCIA'] == "YUNGUYO"].shape)[0]
positivos_hombres_puno_yunguyo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "YUNGUYO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno_yunguyo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "YUNGUYO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno_yunguyo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "YUNGUYO"].shape)[0]
fallecidos_hombres_puno_yunguyo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGUYO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_puno_yunguyo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGUYO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Yunguyo - Etapa de vida
fallecidos_preinfancia_puno_yunguyo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGUYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_puno_yunguyo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGUYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_puno_yunguyo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGUYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_puno_yunguyo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGUYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_puno_yunguyo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGUYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_puno_yunguyo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGUYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


puno =  {
      "name": "Puno",
      "poblacion": poblacion_puno,
      "positivos": positivos_puno,
      "hombres_infectados": positivos_hombres_puno,
      "mujeres_infectados": positivos_mujeres_puno,
      "fallecidos": fallecidos_puno,
      "hombres_fallecidos": fallecidos_hombres_puno,
      "mujeres_fallecidos": fallecidos_mujeres_puno,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno,
       "infancia": fallecidos_infancia_puno,
       "adolescencia": fallecidos_adolescencia_puno,
       "juventud": fallecidos_juventud_puno,
       "adultez": fallecidos_adultez_puno,
       "persona_mayor": fallecidos_persona_mayor_puno
      },
      "url": "puno",
      "provincias": [
        {"name": "Puno", "positivos": positivos_puno_puno,"poblacion": poblacion_puno_puno , "hombres_infectados": positivos_hombres_puno_puno,"mujeres_infectados": positivos_mujeres_puno_puno, "fallecidos": fallecidos_puno_puno, "hombres_fallecidos": fallecidos_hombres_puno_puno, "mujeres_fallecidos": fallecidos_mujeres_puno_puno, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_puno,
       "infancia": fallecidos_infancia_puno_puno,
       "adolescencia": fallecidos_adolescencia_puno_puno,
       "juventud": fallecidos_juventud_puno_puno,
       "adultez": fallecidos_adultez_puno_puno,
       "persona_mayor": fallecidos_persona_mayor_puno_puno
      }},

        {"name": "Azangaro", "positivos": positivos_puno_azangaro,"poblacion": poblacion_puno_azangaro , "hombres_infectados": positivos_hombres_puno_azangaro,"mujeres_infectados": positivos_mujeres_puno_azangaro, "fallecidos": fallecidos_puno_azangaro, "hombres_fallecidos": fallecidos_hombres_puno_azangaro, "mujeres_fallecidos": fallecidos_mujeres_puno_azangaro, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_azangaro,
       "infancia": fallecidos_infancia_puno_azangaro,
       "adolescencia": fallecidos_adolescencia_puno_azangaro,
       "juventud": fallecidos_juventud_puno_azangaro,
       "adultez": fallecidos_adultez_puno_azangaro,
       "persona_mayor": fallecidos_persona_mayor_puno_azangaro
      }},

        {"name": "Carabaya", "positivos": positivos_puno_carabaya,"poblacion": poblacion_puno_carabaya , "hombres_infectados": positivos_hombres_puno_carabaya,"mujeres_infectados": positivos_mujeres_puno_carabaya, "fallecidos": fallecidos_puno_carabaya, "hombres_fallecidos": fallecidos_hombres_puno_carabaya, "mujeres_fallecidos": fallecidos_mujeres_puno_carabaya, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_carabaya,
       "infancia": fallecidos_infancia_puno_carabaya,
       "adolescencia": fallecidos_adolescencia_puno_carabaya,
       "juventud": fallecidos_juventud_puno_carabaya,
       "adultez": fallecidos_adultez_puno_carabaya,
       "persona_mayor": fallecidos_persona_mayor_puno_carabaya
      }},

        {"name": "Chucuito", "positivos": positivos_puno_chucuito,"poblacion": poblacion_puno_chucuito , "hombres_infectados": positivos_hombres_puno_chucuito,"mujeres_infectados": positivos_mujeres_puno_chucuito, "fallecidos": fallecidos_puno_chucuito, "hombres_fallecidos": fallecidos_hombres_puno_chucuito, "mujeres_fallecidos": fallecidos_mujeres_puno_chucuito, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_chucuito,
       "infancia": fallecidos_infancia_puno_chucuito,
       "adolescencia": fallecidos_adolescencia_puno_chucuito,
       "juventud": fallecidos_juventud_puno_chucuito,
       "adultez": fallecidos_adultez_puno_chucuito,
       "persona_mayor": fallecidos_persona_mayor_puno_chucuito
      }},

        {"name": "El Collao", "positivos": positivos_puno_collao,"poblacion": poblacion_puno_collao , "hombres_infectados": positivos_hombres_puno_collao,"mujeres_infectados": positivos_mujeres_puno_collao, "fallecidos": fallecidos_puno_collao, "hombres_fallecidos": fallecidos_hombres_puno_collao, "mujeres_fallecidos": fallecidos_mujeres_puno_collao, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_collao,
       "infancia": fallecidos_infancia_puno_collao,
       "adolescencia": fallecidos_adolescencia_puno_collao,
       "juventud": fallecidos_juventud_puno_collao,
       "adultez": fallecidos_adultez_puno_collao,
       "persona_mayor": fallecidos_persona_mayor_puno_collao
      }},

        {"name": "Huancane", "positivos": positivos_puno_huancane,"poblacion": poblacion_puno_huancane , "hombres_infectados": positivos_hombres_puno_huancane,"mujeres_infectados": positivos_mujeres_puno_huancane, "fallecidos": fallecidos_puno_huancane, "hombres_fallecidos": fallecidos_hombres_puno_huancane, "mujeres_fallecidos": fallecidos_mujeres_puno_huancane, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_huancane,
       "infancia": fallecidos_infancia_puno_huancane,
       "adolescencia": fallecidos_adolescencia_puno_huancane,
       "juventud": fallecidos_juventud_puno_huancane,
       "adultez": fallecidos_adultez_puno_huancane,
       "persona_mayor": fallecidos_persona_mayor_puno_huancane
      }},

        {"name": "Lampa", "positivos": positivos_puno_lampa,"poblacion": poblacion_puno_lampa , "hombres_infectados": positivos_hombres_puno_lampa,"mujeres_infectados": positivos_mujeres_puno_lampa, "fallecidos": fallecidos_puno_lampa, "hombres_fallecidos": fallecidos_hombres_puno_lampa, "mujeres_fallecidos": fallecidos_mujeres_puno_lampa, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_lampa,
       "infancia": fallecidos_infancia_puno_lampa,
       "adolescencia": fallecidos_adolescencia_puno_lampa,
       "juventud": fallecidos_juventud_puno_lampa,
       "adultez": fallecidos_adultez_puno_lampa,
       "persona_mayor": fallecidos_persona_mayor_puno_lampa
      }},

        {"name": "Melgar", "positivos": positivos_puno_melgar,"poblacion": poblacion_puno_melgar , "hombres_infectados": positivos_hombres_puno_melgar,"mujeres_infectados": positivos_mujeres_puno_melgar, "fallecidos": fallecidos_puno_melgar, "hombres_fallecidos": fallecidos_hombres_puno_melgar, "mujeres_fallecidos": fallecidos_mujeres_puno_melgar, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_melgar,
       "infancia": fallecidos_infancia_puno_melgar,
       "adolescencia": fallecidos_adolescencia_puno_melgar,
       "juventud": fallecidos_juventud_puno_melgar,
       "adultez": fallecidos_adultez_puno_melgar,
       "persona_mayor": fallecidos_persona_mayor_puno_melgar
      }},

        {"name": "Moho", "positivos": positivos_puno_moho,"poblacion": poblacion_puno_moho , "hombres_infectados": positivos_hombres_puno_moho,"mujeres_infectados": positivos_mujeres_puno_moho, "fallecidos": fallecidos_puno_moho, "hombres_fallecidos": fallecidos_hombres_puno_moho, "mujeres_fallecidos": fallecidos_mujeres_puno_moho, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_moho,
       "infancia": fallecidos_infancia_puno_moho,
       "adolescencia": fallecidos_adolescencia_puno_moho,
       "juventud": fallecidos_juventud_puno_moho,
       "adultez": fallecidos_adultez_puno_moho,
       "persona_mayor": fallecidos_persona_mayor_puno_moho
      }},

        {"name": "San Antonio de Putina", "positivos": positivos_puno_san_antonio_de_putina,"poblacion": poblacion_puno_san_antonio_de_putina , "hombres_infectados": positivos_hombres_puno_san_antonio_de_putina,"mujeres_infectados": positivos_mujeres_puno_san_antonio_de_putina, "fallecidos": fallecidos_puno_san_antonio_de_putina, "hombres_fallecidos": fallecidos_hombres_puno_san_antonio_de_putina, "mujeres_fallecidos": fallecidos_mujeres_puno_san_antonio_de_putina, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_san_antonio_de_putina,
       "infancia": fallecidos_infancia_puno_san_antonio_de_putina,
       "adolescencia": fallecidos_adolescencia_puno_san_antonio_de_putina,
       "juventud": fallecidos_juventud_puno_san_antonio_de_putina,
       "adultez": fallecidos_adultez_puno_san_antonio_de_putina,
       "persona_mayor": fallecidos_persona_mayor_puno_san_antonio_de_putina
      }},

        {"name": "San Roman", "positivos": positivos_puno_san_roman,"poblacion": poblacion_puno_san_roman , "hombres_infectados": positivos_hombres_puno_san_roman,"mujeres_infectados": positivos_mujeres_puno_san_roman, "fallecidos": fallecidos_puno_san_roman, "hombres_fallecidos": fallecidos_hombres_puno_san_roman, "mujeres_fallecidos": fallecidos_mujeres_puno_san_roman, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_san_roman,
       "infancia": fallecidos_infancia_puno_san_roman,
       "adolescencia": fallecidos_adolescencia_puno_san_roman,
       "juventud": fallecidos_juventud_puno_san_roman,
       "adultez": fallecidos_adultez_puno_san_roman,
       "persona_mayor": fallecidos_persona_mayor_puno_san_roman
      }},

        {"name": "Sandia", "positivos": positivos_puno_sandia,"poblacion": poblacion_puno_sandia , "hombres_infectados": positivos_hombres_puno_sandia,"mujeres_infectados": positivos_mujeres_puno_sandia, "fallecidos": fallecidos_puno_sandia, "hombres_fallecidos": fallecidos_hombres_puno_sandia, "mujeres_fallecidos": fallecidos_mujeres_puno_sandia, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_sandia,
       "infancia": fallecidos_infancia_puno_sandia,
       "adolescencia": fallecidos_adolescencia_puno_sandia,
       "juventud": fallecidos_juventud_puno_sandia,
       "adultez": fallecidos_adultez_puno_sandia,
       "persona_mayor": fallecidos_persona_mayor_puno_sandia
      }},

        {"name": "Yunguyo", "positivos": positivos_puno_yunguyo,"poblacion": poblacion_puno_yunguyo , "hombres_infectados": positivos_hombres_puno_yunguyo,"mujeres_infectados": positivos_mujeres_puno_yunguyo, "fallecidos": fallecidos_puno_yunguyo, "hombres_fallecidos": fallecidos_hombres_puno_yunguyo, "mujeres_fallecidos": fallecidos_mujeres_puno_yunguyo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_yunguyo,
       "infancia": fallecidos_infancia_puno_yunguyo,
       "adolescencia": fallecidos_adolescencia_puno_yunguyo,
       "juventud": fallecidos_juventud_puno_yunguyo,
       "adultez": fallecidos_adultez_puno_yunguyo,
       "persona_mayor": fallecidos_persona_mayor_puno_yunguyo
      }}
      ]
    }

print(json.dumps(puno));
sys.stdout.flush();
