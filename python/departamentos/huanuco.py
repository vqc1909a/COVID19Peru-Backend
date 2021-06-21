import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_huanuco = 756847
positivos_huanuco = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "HUANUCO"].shape)[0]
positivos_hombres_huanuco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "HUANUCO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huanuco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "HUANUCO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huanuco = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "HUANUCO"].shape)[0]
fallecidos_hombres_huanuco  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANUCO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANUCO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Huanuco - Etapa de vida
fallecidos_preinfancia_huanuco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Huanuco
#!Huanuco-Huanuco
poblacion_huanuco_huanuco = 258430
positivos_huanuco_huanuco = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUANUCO"].shape)[0]
positivos_hombres_huanuco_huanuco = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUANUCO")].shape)[0]
positivos_mujeres_huanuco_huanuco = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUANUCO")].shape)[0]
fallecidos_huanuco_huanuco = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUANUCO"].shape)[0]
fallecidos_hombres_huanuco_huanuco  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANUCO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_huanuco = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "HUANUCO") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Huanuco - Etapa de vida
fallecidos_preinfancia_huanuco_huanuco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_huanuco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_huanuco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_huanuco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_huanuco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_huanuco = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Ambo
poblacion_huanuco_ambo = 47152
positivos_huanuco_ambo = list(casos_positivos[casos_positivos['PROVINCIA'] == "AMBO"].shape)[0]
positivos_hombres_huanuco_ambo = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "AMBO")].shape)[0]
positivos_mujeres_huanuco_ambo = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "AMBO")].shape)[0]
fallecidos_huanuco_ambo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "AMBO"].shape)[0]
fallecidos_hombres_huanuco_ambo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AMBO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_ambo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AMBO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Ambo - Etapa de vida
fallecidos_preinfancia_huanuco_ambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_ambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_ambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_ambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_ambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_ambo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Provincia Dos De Mayo
poblacion_huanuco_dos_de_mayo = 41508
positivos_huanuco_dos_de_mayo = list(casos_positivos[casos_positivos['PROVINCIA'] == "DOS DE MAYO"].shape)[0]
positivos_hombres_huanuco_dos_de_mayo = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "DOS DE MAYO")].shape)[0]
positivos_mujeres_huanuco_dos_de_mayo = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "DOS DE MAYO")].shape)[0]
fallecidos_huanuco_dos_de_mayo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "DOS DE MAYO"].shape)[0]
fallecidos_hombres_huanuco_dos_de_mayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DOS DE MAYO") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_dos_de_mayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DOS DE MAYO") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Dos De Mayo - Etapa de vida
fallecidos_preinfancia_huanuco_dos_de_mayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DOS DE MAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_dos_de_mayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DOS DE MAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_dos_de_mayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DOS DE MAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_dos_de_mayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DOS DE MAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_dos_de_mayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DOS DE MAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_dos_de_mayo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DOS DE MAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Huacaybamba
poblacion_huanuco_huacaybamba = 17892
positivos_huanuco_huacaybamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUACAYBAMBA"].shape)[0]
positivos_hombres_huanuco_huacaybamba = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUACAYBAMBA")].shape)[0]
positivos_mujeres_huanuco_huacaybamba = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUACAYBAMBA")].shape)[0]
fallecidos_huanuco_huacaybamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUACAYBAMBA"].shape)[0]
fallecidos_hombres_huanuco_huacaybamba  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUACAYBAMBA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_huacaybamba  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUACAYBAMBA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Huacaybamba - Etapa de vida
fallecidos_preinfancia_huanuco_huacaybamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUACAYBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_huacaybamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUACAYBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_huacaybamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUACAYBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_huacaybamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUACAYBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_huacaybamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUACAYBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_huacaybamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUACAYBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Huamalies
poblacion_huanuco_huamalies = 59511
positivos_huanuco_huamalies = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUAMALIES"].shape)[0]
positivos_hombres_huanuco_huamalies = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUAMALIES")].shape)[0]
positivos_mujeres_huanuco_huamalies = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUAMALIES")].shape)[0]
fallecidos_huanuco_huamalies = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUAMALIES"].shape)[0]
fallecidos_hombres_huanuco_huamalies  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMALIES") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_huamalies  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMALIES") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Huamalies - Etapa de vida
fallecidos_preinfancia_huanuco_huamalies = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMALIES") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_huamalies = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMALIES") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_huamalies = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMALIES") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_huamalies = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMALIES") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_huamalies = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMALIES") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_huamalies = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMALIES") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huanuco-Leoncio Prado
poblacion_huanuco_leoncio_prado = 163940
positivos_huanuco_leoncio_prado = list(casos_positivos[casos_positivos['PROVINCIA'] == "LEONCIO PRADO"].shape)[0]
positivos_hombres_huanuco_leoncio_prado = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "LEONCIO PRADO")].shape)[0]
positivos_mujeres_huanuco_leoncio_prado = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "LEONCIO PRADO")].shape)[0]
fallecidos_huanuco_leoncio_prado = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LEONCIO PRADO"].shape)[0]
fallecidos_hombres_huanuco_leoncio_prado  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LEONCIO PRADO") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_leoncio_prado  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LEONCIO PRADO") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Leoncio Prado - Etapa de vida
fallecidos_preinfancia_huanuco_leoncio_prado = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LEONCIO PRADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_leoncio_prado = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LEONCIO PRADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_leoncio_prado = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LEONCIO PRADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_leoncio_prado = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LEONCIO PRADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_leoncio_prado = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LEONCIO PRADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_leoncio_prado = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LEONCIO PRADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huanuco-Marañon
poblacion_huanuco_marañon = 25987
positivos_huanuco_marañon = list(casos_positivos[casos_positivos['PROVINCIA'] == "MARAÑON"].shape)[0]
positivos_hombres_huanuco_marañon = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "MARAÑON")].shape)[0]
positivos_mujeres_huanuco_marañon = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "MARAÑON")].shape)[0]
fallecidos_huanuco_marañon = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MARAÑON"].shape)[0]
fallecidos_hombres_huanuco_marañon  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARAÑON") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_marañon  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARAÑON") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Marañon - Etapa de vida
fallecidos_preinfancia_huanuco_marañon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_marañon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_marañon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_marañon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_marañon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_marañon = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Pachitea
poblacion_huanuco_pachitea = 582828
positivos_huanuco_pachitea = list(casos_positivos[casos_positivos['PROVINCIA'] == "PACHITEA"].shape)[0]
positivos_hombres_huanuco_pachitea = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PACHITEA")].shape)[0]
positivos_mujeres_huanuco_pachitea = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PACHITEA")].shape)[0]
fallecidos_huanuco_pachitea = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PACHITEA"].shape)[0]
fallecidos_hombres_huanuco_pachitea  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACHITEA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_pachitea  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACHITEA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Marañon - Etapa de vida
fallecidos_preinfancia_huanuco_pachitea = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACHITEA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_pachitea = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACHITEA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_pachitea = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACHITEA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_pachitea = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACHITEA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_pachitea = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACHITEA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_pachitea = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACHITEA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Huanuco-Puerto Inca
poblacion_huanuco_puerto_inca = 28858
positivos_huanuco_puerto_inca = list(casos_positivos[casos_positivos['PROVINCIA'] == "PUERTO INCA"].shape)[0]
positivos_hombres_huanuco_puerto_inca = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PUERTO INCA")].shape)[0]
positivos_mujeres_huanuco_puerto_inca = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PUERTO INCA")].shape)[0]
fallecidos_huanuco_puerto_inca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PUERTO INCA"].shape)[0]
fallecidos_hombres_huanuco_puerto_inca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUERTO INCA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_puerto_inca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUERTO INCA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Marañon - Etapa de vida
fallecidos_preinfancia_huanuco_puerto_inca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUERTO INCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_puerto_inca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUERTO INCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_puerto_inca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUERTO INCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_puerto_inca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUERTO INCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_puerto_inca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUERTO INCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_puerto_inca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUERTO INCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huanuco-Lauricocha
poblacion_huanuco_lauricocha = 29714
positivos_huanuco_lauricocha = list(casos_positivos[casos_positivos['PROVINCIA'] == "LAURICOCHA"].shape)[0]
positivos_hombres_huanuco_lauricocha = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "LAURICOCHA")].shape)[0]
positivos_mujeres_huanuco_lauricocha = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "LAURICOCHA")].shape)[0]
fallecidos_huanuco_lauricocha = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LAURICOCHA"].shape)[0]
fallecidos_hombres_huanuco_lauricocha  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAURICOCHA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_lauricocha  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAURICOCHA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Lauricocha - Etapa de vida
fallecidos_preinfancia_huanuco_lauricocha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAURICOCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_lauricocha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAURICOCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_lauricocha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAURICOCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_lauricocha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAURICOCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_lauricocha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAURICOCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_lauricocha = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAURICOCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huanuco-Yarowilca
poblacion_huanuco_yarowilca = 25567
positivos_huanuco_yarowilca = list(casos_positivos[casos_positivos['PROVINCIA'] == "YAROWILCA"].shape)[0]
positivos_hombres_huanuco_yarowilca = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "YAROWILCA")].shape)[0]
positivos_mujeres_huanuco_yarowilca = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "YAROWILCA")].shape)[0]
fallecidos_huanuco_yarowilca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "YAROWILCA"].shape)[0]
fallecidos_hombres_huanuco_yarowilca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAROWILCA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_huanuco_yarowilca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAROWILCA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]



#!Provincia Yarowilca - Etapa de vida
fallecidos_preinfancia_huanuco_yarowilca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAROWILCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huanuco_yarowilca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAROWILCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huanuco_yarowilca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAROWILCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huanuco_yarowilca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAROWILCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huanuco_yarowilca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAROWILCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huanuco_yarowilca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAROWILCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

huanuco =  {
      "name": "Huanuco",
      "poblacion": poblacion_huanuco,
      "positivos": positivos_huanuco,
      "hombres_infectados": positivos_hombres_huanuco,
      "mujeres_infectados": positivos_mujeres_huanuco,
      "fallecidos": fallecidos_huanuco,
      "hombres_fallecidos": fallecidos_hombres_huanuco,
      "mujeres_fallecidos": fallecidos_mujeres_huanuco,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco,
       "infancia": fallecidos_infancia_huanuco,
       "adolescencia": fallecidos_adolescencia_huanuco,
       "juventud": fallecidos_juventud_huanuco,
       "adultez": fallecidos_adultez_huanuco,
       "persona_mayor": fallecidos_persona_mayor_huanuco
      },
      "url": "huanuco",
      "provincias": [
         {"name": "Huanuco", "positivos": positivos_huanuco_huanuco,"poblacion": poblacion_huanuco_huanuco , "hombres_infectados": positivos_hombres_huanuco_huanuco,"mujeres_infectados": positivos_mujeres_huanuco_huanuco, "fallecidos": fallecidos_huanuco_huanuco, "hombres_fallecidos": fallecidos_hombres_huanuco_huanuco, "mujeres_fallecidos": fallecidos_mujeres_huanuco_huanuco, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_huanuco,
       "infancia": fallecidos_infancia_huanuco_huanuco,
       "adolescencia": fallecidos_adolescencia_huanuco_huanuco,
       "juventud": fallecidos_juventud_huanuco_huanuco,
       "adultez": fallecidos_adultez_huanuco_huanuco,
       "persona_mayor": fallecidos_persona_mayor_huanuco_huanuco
      }},

          {"name": "Ambo", "positivos": positivos_huanuco_ambo,"poblacion": poblacion_huanuco_ambo , "hombres_infectados": positivos_hombres_huanuco_ambo,"mujeres_infectados": positivos_mujeres_huanuco_ambo, "fallecidos": fallecidos_huanuco_ambo, "hombres_fallecidos": fallecidos_hombres_huanuco_ambo, "mujeres_fallecidos": fallecidos_mujeres_huanuco_ambo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_ambo,
       "infancia": fallecidos_infancia_huanuco_ambo,
       "adolescencia": fallecidos_adolescencia_huanuco_ambo,
       "juventud": fallecidos_juventud_huanuco_ambo,
       "adultez": fallecidos_adultez_huanuco_ambo,
       "persona_mayor": fallecidos_persona_mayor_huanuco_ambo
      }},

          {"name": "Dos de Mayo", "positivos": positivos_huanuco_dos_de_mayo,"poblacion": poblacion_huanuco_dos_de_mayo , "hombres_infectados": positivos_hombres_huanuco_dos_de_mayo,"mujeres_infectados": positivos_mujeres_huanuco_dos_de_mayo, "fallecidos": fallecidos_huanuco_dos_de_mayo, "hombres_fallecidos": fallecidos_hombres_huanuco_dos_de_mayo, "mujeres_fallecidos": fallecidos_mujeres_huanuco_dos_de_mayo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_dos_de_mayo,
       "infancia": fallecidos_infancia_huanuco_dos_de_mayo,
       "adolescencia": fallecidos_adolescencia_huanuco_dos_de_mayo,
       "juventud": fallecidos_juventud_huanuco_dos_de_mayo,
       "adultez": fallecidos_adultez_huanuco_dos_de_mayo,
       "persona_mayor": fallecidos_persona_mayor_huanuco_dos_de_mayo
      }},
          
          {"name": "Huacaybamba", "positivos": positivos_huanuco_huacaybamba,"poblacion": poblacion_huanuco_huacaybamba , "hombres_infectados": positivos_hombres_huanuco_huacaybamba,"mujeres_infectados": positivos_mujeres_huanuco_huacaybamba, "fallecidos": fallecidos_huanuco_huacaybamba, "hombres_fallecidos": fallecidos_hombres_huanuco_huacaybamba, "mujeres_fallecidos": fallecidos_mujeres_huanuco_huacaybamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_huacaybamba,
       "infancia": fallecidos_infancia_huanuco_huacaybamba,
       "adolescencia": fallecidos_adolescencia_huanuco_huacaybamba,
       "juventud": fallecidos_juventud_huanuco_huacaybamba,
       "adultez": fallecidos_adultez_huanuco_huacaybamba,
       "persona_mayor": fallecidos_persona_mayor_huanuco_huacaybamba
      }},

          {"name": "Huamalies", "positivos": positivos_huanuco_huamalies,"poblacion": poblacion_huanuco_huamalies , "hombres_infectados": positivos_hombres_huanuco_huamalies,"mujeres_infectados": positivos_mujeres_huanuco_huamalies, "fallecidos": fallecidos_huanuco_huamalies, "hombres_fallecidos": fallecidos_hombres_huanuco_huamalies, "mujeres_fallecidos": fallecidos_mujeres_huanuco_huamalies, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_huamalies,
       "infancia": fallecidos_infancia_huanuco_huamalies,
       "adolescencia": fallecidos_adolescencia_huanuco_huamalies,
       "juventud": fallecidos_juventud_huanuco_huamalies,
       "adultez": fallecidos_adultez_huanuco_huamalies,
       "persona_mayor": fallecidos_persona_mayor_huanuco_huamalies
      }},

          {"name": "Leoncio Prado", "positivos": positivos_huanuco_leoncio_prado,"poblacion": poblacion_huanuco_leoncio_prado , "hombres_infectados": positivos_hombres_huanuco_leoncio_prado,"mujeres_infectados": positivos_mujeres_huanuco_leoncio_prado, "fallecidos": fallecidos_huanuco_leoncio_prado, "hombres_fallecidos": fallecidos_hombres_huanuco_leoncio_prado, "mujeres_fallecidos": fallecidos_mujeres_huanuco_leoncio_prado, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_leoncio_prado,
       "infancia": fallecidos_infancia_huanuco_leoncio_prado,
       "adolescencia": fallecidos_adolescencia_huanuco_leoncio_prado,
       "juventud": fallecidos_juventud_huanuco_leoncio_prado,
       "adultez": fallecidos_adultez_huanuco_leoncio_prado,
       "persona_mayor": fallecidos_persona_mayor_huanuco_leoncio_prado
      }},

          {"name": "Marañon", "positivos": positivos_huanuco_marañon,"poblacion": poblacion_huanuco_marañon , "hombres_infectados": positivos_hombres_huanuco_marañon,"mujeres_infectados": positivos_mujeres_huanuco_marañon, "fallecidos": fallecidos_huanuco_marañon, "hombres_fallecidos": fallecidos_hombres_huanuco_marañon, "mujeres_fallecidos": fallecidos_mujeres_huanuco_marañon, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_marañon,
       "infancia": fallecidos_infancia_huanuco_marañon,
       "adolescencia": fallecidos_adolescencia_huanuco_marañon,
       "juventud": fallecidos_juventud_huanuco_marañon,
       "adultez": fallecidos_adultez_huanuco_marañon,
       "persona_mayor": fallecidos_persona_mayor_huanuco_marañon
      }},

          {"name": "Pachitea", "positivos": positivos_huanuco_pachitea,"poblacion": poblacion_huanuco_pachitea , "hombres_infectados": positivos_hombres_huanuco_pachitea,"mujeres_infectados": positivos_mujeres_huanuco_pachitea, "fallecidos": fallecidos_huanuco_pachitea, "hombres_fallecidos": fallecidos_hombres_huanuco_pachitea, "mujeres_fallecidos": fallecidos_mujeres_huanuco_pachitea, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_pachitea,
       "infancia": fallecidos_infancia_huanuco_pachitea,
       "adolescencia": fallecidos_adolescencia_huanuco_pachitea,
       "juventud": fallecidos_juventud_huanuco_pachitea,
       "adultez": fallecidos_adultez_huanuco_pachitea,
       "persona_mayor": fallecidos_persona_mayor_huanuco_pachitea
      }},

          {"name": "Puerto Inca", "positivos": positivos_huanuco_puerto_inca,"poblacion": poblacion_huanuco_puerto_inca , "hombres_infectados": positivos_hombres_huanuco_puerto_inca,"mujeres_infectados": positivos_mujeres_huanuco_puerto_inca, "fallecidos": fallecidos_huanuco_puerto_inca, "hombres_fallecidos": fallecidos_hombres_huanuco_puerto_inca, "mujeres_fallecidos": fallecidos_mujeres_huanuco_puerto_inca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_puerto_inca,
       "infancia": fallecidos_infancia_huanuco_puerto_inca,
       "adolescencia": fallecidos_adolescencia_huanuco_puerto_inca,
       "juventud": fallecidos_juventud_huanuco_puerto_inca,
       "adultez": fallecidos_adultez_huanuco_puerto_inca,
       "persona_mayor": fallecidos_persona_mayor_huanuco_puerto_inca
      }},

          {"name": "Lauricocha", "positivos": positivos_huanuco_lauricocha,"poblacion": poblacion_huanuco_lauricocha , "hombres_infectados": positivos_hombres_huanuco_lauricocha,"mujeres_infectados": positivos_mujeres_huanuco_lauricocha, "fallecidos": fallecidos_huanuco_lauricocha, "hombres_fallecidos": fallecidos_hombres_huanuco_lauricocha, "mujeres_fallecidos": fallecidos_mujeres_huanuco_lauricocha, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_lauricocha,
       "infancia": fallecidos_infancia_huanuco_lauricocha,
       "adolescencia": fallecidos_adolescencia_huanuco_lauricocha,
       "juventud": fallecidos_juventud_huanuco_lauricocha,
       "adultez": fallecidos_adultez_huanuco_lauricocha,
       "persona_mayor": fallecidos_persona_mayor_huanuco_lauricocha
      }},

          {"name": "Yarowilca", "positivos": positivos_huanuco_yarowilca,"poblacion": poblacion_huanuco_yarowilca , "hombres_infectados": positivos_hombres_huanuco_yarowilca,"mujeres_infectados": positivos_mujeres_huanuco_yarowilca, "fallecidos": fallecidos_huanuco_yarowilca, "hombres_fallecidos": fallecidos_hombres_huanuco_yarowilca, "mujeres_fallecidos": fallecidos_mujeres_huanuco_yarowilca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_yarowilca,
       "infancia": fallecidos_infancia_huanuco_yarowilca,
       "adolescencia": fallecidos_adolescencia_huanuco_yarowilca,
       "juventud": fallecidos_juventud_huanuco_yarowilca,
       "adultez": fallecidos_adultez_huanuco_yarowilca,
       "persona_mayor": fallecidos_persona_mayor_huanuco_yarowilca
      }}
      ]
    }
print(json.dumps(huanuco));
sys.stdout.flush();
