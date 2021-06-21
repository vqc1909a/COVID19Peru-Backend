import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos


poblacion_lima = 10907764
positivos_lima = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LIMA") | (casos_positivos['DEPARTAMENTO'] == "LIMA REGION")].shape)[0]
positivos_hombres_lima = list(casos_positivos[((casos_positivos['DEPARTAMENTO'] == "LIMA") | (casos_positivos['DEPARTAMENTO'] == "LIMA REGION")) & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima = list(casos_positivos[((casos_positivos['DEPARTAMENTO'] == "LIMA") | (casos_positivos['DEPARTAMENTO'] == "LIMA REGION")) & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LIMA") | (casos_fallecidos['DEPARTAMENTO'] == "LIMA REGION")].shape)[0]
fallecidos_hombres_lima  = list(casos_fallecidos[((casos_fallecidos['DEPARTAMENTO'] == "LIMA") | (casos_positivos['DEPARTAMENTO'] == "LIMA REGION")) &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima  = list(casos_fallecidos[((casos_fallecidos['DEPARTAMENTO'] == "LIMA") | (casos_positivos['DEPARTAMENTO'] == "LIMA REGION")) &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Departamento Lima - Etapa de vida
fallecidos_preinfancia_lima = list(casos_fallecidos[((casos_fallecidos['DEPARTAMENTO'] == "LIMA") | (casos_fallecidos['DEPARTAMENTO'] == "LIMA REGION")) & ((casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5))].shape)[0]
fallecidos_infancia_lima = list(casos_fallecidos[((casos_fallecidos['DEPARTAMENTO'] == "LIMA") | (casos_fallecidos['DEPARTAMENTO'] == "LIMA REGION")) & ((casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11))].shape)[0]
fallecidos_adolescencia_lima = list(casos_fallecidos[((casos_fallecidos['DEPARTAMENTO'] == "LIMA") | (casos_fallecidos['DEPARTAMENTO'] == "LIMA REGION")) & ((casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18))].shape)[0]
fallecidos_juventud_lima = list(casos_fallecidos[((casos_fallecidos['DEPARTAMENTO'] == "LIMA") | (casos_fallecidos['DEPARTAMENTO'] == "LIMA REGION")) & ((casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26))].shape)[0]
fallecidos_adultez_lima = list(casos_fallecidos[((casos_fallecidos['DEPARTAMENTO'] == "LIMA") | (casos_fallecidos['DEPARTAMENTO'] == "LIMA REGION")) & ((casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59))].shape)[0]
fallecidos_persona_mayor_lima = list(
    casos_fallecidos[((casos_fallecidos['DEPARTAMENTO'] == "LIMA") | (casos_fallecidos['DEPARTAMENTO'] == "LIMA REGION")) & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Lima
#!Lima-Lima
poblacion_lima_lima = 9867824
positivos_lima_lima = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LIMA") | (casos_positivos['PROVINCIA'] == "LIMA REGION")].shape)[0]
positivos_hombres_lima_lima = list(casos_positivos[((casos_positivos['PROVINCIA'] == "LIMA") | (casos_positivos['PROVINCIA'] == "LIMA REGION")) & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima_lima = list(casos_positivos[((casos_positivos['PROVINCIA'] == "LIMA") | (casos_positivos['PROVINCIA'] == "LIMA REGION")) & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima_lima = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LIMA") | (casos_fallecidos['PROVINCIA'] == "LIMA REGION")].shape)[0]
fallecidos_hombres_lima_lima = list(casos_fallecidos[((casos_fallecidos['PROVINCIA'] == "LIMA") |(casos_fallecidos['PROVINCIA'] == "LIMA REGION")) & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima_lima = list(casos_fallecidos[((casos_fallecidos['PROVINCIA'] == "LIMA") | (
    casos_fallecidos['PROVINCIA'] == "LIMA REGION")) & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]



#!Provincias Lima - Etapa de vida
fallecidos_preinfancia_lima_lima = list(casos_fallecidos[((casos_fallecidos['PROVINCIA'] == "LIMA") | (casos_fallecidos['PROVINCIA'] == "LIMA REGION")) & ((casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5))].shape)[0]
fallecidos_infancia_lima_lima = list(casos_fallecidos[((casos_fallecidos['PROVINCIA'] == "LIMA") | (casos_fallecidos['PROVINCIA'] == "LIMA REGION")) & ((casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11))].shape)[0]
fallecidos_adolescencia_lima_lima = list(casos_fallecidos[((casos_fallecidos['PROVINCIA'] == "LIMA") | (casos_fallecidos['PROVINCIA'] == "LIMA REGION")) & ((casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18))].shape)[0]
fallecidos_juventud_lima_lima = list(casos_fallecidos[((casos_fallecidos['PROVINCIA'] == "LIMA") | (casos_fallecidos['PROVINCIA'] == "LIMA REGION")) & ((casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26))].shape)[0]
fallecidos_adultez_lima_lima = list(casos_fallecidos[((casos_fallecidos['PROVINCIA'] == "LIMA") | (casos_fallecidos['PROVINCIA'] == "LIMA REGION")) & ((casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59))].shape)[0]
fallecidos_persona_mayor_lima_lima = list(
    casos_fallecidos[((casos_fallecidos['PROVINCIA'] == "LIMA") | (casos_fallecidos['PROVINCIA'] == "LIMA REGION")) & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Provincia Barranca
poblacion_lima_barranca = 162084
positivos_lima_barranca = list(casos_positivos[casos_positivos['PROVINCIA'] == "BARRANCA"].shape)[0]
positivos_hombres_lima_barranca = list(casos_positivos[(casos_positivos['PROVINCIA'] == "BARRANCA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima_barranca = list(casos_positivos[(casos_positivos['PROVINCIA'] == "BARRANCA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima_barranca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "BARRANCA"].shape)[0]
fallecidos_hombres_lima_barranca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BARRANCA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima_barranca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BARRANCA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Barranca - Etapa de vida
fallecidos_preinfancia_lima_barranca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BARRANCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lima_barranca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BARRANCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lima_barranca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BARRANCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lima_barranca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BARRANCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lima_barranca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BARRANCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lima_barranca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BARRANCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Cajatambo
poblacion_lima_cajatambo = 8327
positivos_lima_cajatambo = list(casos_positivos[casos_positivos['PROVINCIA'] == "CAJATAMBO"].shape)[0]
positivos_hombres_lima_cajatambo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CAJATAMBO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima_cajatambo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CAJATAMBO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima_cajatambo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CAJATAMBO"].shape)[0]
fallecidos_hombres_lima_cajatambo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJATAMBO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima_cajatambo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJATAMBO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Cajatambo - Etapa de vida
fallecidos_preinfancia_lima_cajatambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJATAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lima_cajatambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJATAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lima_cajatambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJATAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lima_cajatambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJATAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lima_cajatambo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJATAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lima_cajatambo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAJATAMBO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Canta
poblacion_lima_canta = 16598
positivos_lima_canta = list(casos_positivos[casos_positivos['PROVINCIA'] == "CANTA"].shape)[0]
positivos_hombres_lima_canta = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANTA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima_canta = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANTA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima_canta = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CANTA"].shape)[0]
fallecidos_hombres_lima_canta  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANTA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima_canta  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANTA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Canta - Etapa de vida
fallecidos_preinfancia_lima_canta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lima_canta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lima_canta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lima_canta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lima_canta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lima_canta = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Cañete
poblacion_lima_canete = 254360
positivos_lima_canete = list(casos_positivos[casos_positivos['PROVINCIA'] == "CAÑETE"].shape)[0]
positivos_hombres_lima_canete = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CAÑETE") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima_canete = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CAÑETE") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima_canete = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CAÑETE"].shape)[0]
fallecidos_hombres_lima_canete  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAÑETE") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima_canete  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAÑETE") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Cañete - Etapa de vida
fallecidos_preinfancia_lima_canete = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAÑETE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lima_canete = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAÑETE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lima_canete = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAÑETE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lima_canete = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAÑETE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lima_canete = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAÑETE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lima_canete = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CAÑETE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Huaral
poblacion_lima_huaral = 209178
positivos_lima_huaral = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUARAL"].shape)[0]
positivos_hombres_lima_huaral = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUARAL") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima_huaral = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUARAL") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima_huaral = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUARAL"].shape)[0]
fallecidos_hombres_lima_huaral  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAL") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima_huaral  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAL") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Huaral - Etapa de vida
fallecidos_preinfancia_lima_huaral = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAL") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lima_huaral = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAL") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lima_huaral = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAL") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lima_huaral = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAL") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lima_huaral = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAL") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lima_huaral = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAL") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Huarochiri
poblacion_lima_huarochiri = 91529
positivos_lima_huarochiri = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUAROCHIRI"].shape)[0]
positivos_hombres_lima_huarochiri = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUAROCHIRI") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima_huarochiri = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUAROCHIRI") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima_huarochiri = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUAROCHIRI"].shape)[0]
fallecidos_hombres_lima_huarochiri  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAROCHIRI") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima_huarochiri  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAROCHIRI") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Huarochiri - Etapa de vida
fallecidos_preinfancia_lima_huarochiri = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAROCHIRI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lima_huarochiri = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAROCHIRI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lima_huarochiri = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAROCHIRI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lima_huarochiri = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAROCHIRI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lima_huarochiri = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAROCHIRI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lima_huarochiri = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAROCHIRI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Huaura
poblacion_lima_huaura = 244333
positivos_lima_huaura = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUAURA"].shape)[0]
positivos_hombres_lima_huaura = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUAURA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima_huaura = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUAURA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima_huaura = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUAURA"].shape)[0]
fallecidos_hombres_lima_huaura  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAURA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima_huaura  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAURA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Huaura - Etapa de vida
fallecidos_preinfancia_lima_huaura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lima_huaura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lima_huaura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lima_huaura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lima_huaura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lima_huaura = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Oyon
poblacion_lima_oyon = 23800
positivos_lima_oyon = list(casos_positivos[casos_positivos['PROVINCIA'] == "OYON"].shape)[0]
positivos_hombres_lima_oyon = list(casos_positivos[(casos_positivos['PROVINCIA'] == "OYON") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima_oyon = list(casos_positivos[(casos_positivos['PROVINCIA'] == "OYON") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima_oyon = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "OYON"].shape)[0]
fallecidos_hombres_lima_oyon  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OYON") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima_oyon  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OYON") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Oyon - Etapa de vida
fallecidos_preinfancia_lima_oyon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OYON") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lima_oyon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OYON") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lima_oyon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OYON") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lima_oyon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OYON") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lima_oyon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OYON") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lima_oyon = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OYON") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Yauyos
poblacion_lima_yauyos = 29731
positivos_lima_yauyos = list(casos_positivos[casos_positivos['PROVINCIA'] == "YAUYOS"].shape)[0]
positivos_hombres_lima_yauyos = list(casos_positivos[(casos_positivos['PROVINCIA'] == "YAUYOS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima_yauyos = list(casos_positivos[(casos_positivos['PROVINCIA'] == "YAUYOS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima_yauyos = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "YAUYOS"].shape)[0]
fallecidos_hombres_lima_yauyos  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAUYOS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_lima_yauyos  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAUYOS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Yauyos - Etapa de vida
fallecidos_preinfancia_lima_yauyos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lima_yauyos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lima_yauyos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lima_yauyos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lima_yauyos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lima_yauyos = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAUYOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

lima =  {
      "name": "Lima",
      "poblacion": poblacion_lima,
      "positivos": positivos_lima,
      "hombres_infectados": positivos_hombres_lima,
      "mujeres_infectados": positivos_mujeres_lima,
      "fallecidos": fallecidos_lima,
      "hombres_fallecidos": fallecidos_hombres_lima,
      "mujeres_fallecidos": fallecidos_mujeres_lima,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima,
       "infancia": fallecidos_infancia_lima,
       "adolescencia": fallecidos_adolescencia_lima,
       "juventud": fallecidos_juventud_lima,
       "adultez": fallecidos_adultez_lima,
       "persona_mayor": fallecidos_persona_mayor_lima
      },
      "url": "lima",
      "provincias": [
          {"name": "Lima", "positivos": positivos_lima_lima,"poblacion": poblacion_lima_lima , "hombres_infectados": positivos_hombres_lima_lima,"mujeres_infectados": positivos_mujeres_lima_lima, "fallecidos": fallecidos_lima_lima, "hombres_fallecidos": fallecidos_hombres_lima_lima, "mujeres_fallecidos": fallecidos_mujeres_lima_lima, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_lima,
       "infancia": fallecidos_infancia_lima_lima,
       "adolescencia": fallecidos_adolescencia_lima_lima,
       "juventud": fallecidos_juventud_lima_lima,
       "adultez": fallecidos_adultez_lima_lima,
       "persona_mayor": fallecidos_persona_mayor_lima_lima
      }},

          {"name": "Barranca", "positivos": positivos_lima_barranca,"poblacion": poblacion_lima_barranca , "hombres_infectados": positivos_hombres_lima_barranca,"mujeres_infectados": positivos_mujeres_lima_barranca, "fallecidos": fallecidos_lima_barranca, "hombres_fallecidos": fallecidos_hombres_lima_barranca, "mujeres_fallecidos": fallecidos_mujeres_lima_barranca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_barranca,
       "infancia": fallecidos_infancia_lima_barranca,
       "adolescencia": fallecidos_adolescencia_lima_barranca,
       "juventud": fallecidos_juventud_lima_barranca,
       "adultez": fallecidos_adultez_lima_barranca,
       "persona_mayor": fallecidos_persona_mayor_lima_barranca
      }},

          {"name": "Cajatambo", "positivos": positivos_lima_cajatambo,"poblacion": poblacion_lima_cajatambo , "hombres_infectados": positivos_hombres_lima_cajatambo,"mujeres_infectados": positivos_mujeres_lima_cajatambo, "fallecidos": fallecidos_lima_cajatambo, "hombres_fallecidos": fallecidos_hombres_lima_cajatambo, "mujeres_fallecidos": fallecidos_mujeres_lima_cajatambo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_cajatambo,
       "infancia": fallecidos_infancia_lima_cajatambo,
       "adolescencia": fallecidos_adolescencia_lima_cajatambo,
       "juventud": fallecidos_juventud_lima_cajatambo,
       "adultez": fallecidos_adultez_lima_cajatambo,
       "persona_mayor": fallecidos_persona_mayor_lima_cajatambo
      }},

          {"name": "Canta", "positivos": positivos_lima_canta,"poblacion": poblacion_lima_canta , "hombres_infectados": positivos_hombres_lima_canta,"mujeres_infectados": positivos_mujeres_lima_canta, "fallecidos": fallecidos_lima_canta, "hombres_fallecidos": fallecidos_hombres_lima_canta, "mujeres_fallecidos": fallecidos_mujeres_lima_canta, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_canta,
       "infancia": fallecidos_infancia_lima_canta,
       "adolescencia": fallecidos_adolescencia_lima_canta,
       "juventud": fallecidos_juventud_lima_canta,
       "adultez": fallecidos_adultez_lima_canta,
       "persona_mayor": fallecidos_persona_mayor_lima_canta
      }},

          {"name": "Cañete", "positivos": positivos_lima_canete,"poblacion": poblacion_lima_canete , "hombres_infectados": positivos_hombres_lima_canete,"mujeres_infectados": positivos_mujeres_lima_canete, "fallecidos": fallecidos_lima_canete, "hombres_fallecidos": fallecidos_hombres_lima_canete, "mujeres_fallecidos": fallecidos_mujeres_lima_canete, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_canete,
       "infancia": fallecidos_infancia_lima_canete,
       "adolescencia": fallecidos_adolescencia_lima_canete,
       "juventud": fallecidos_juventud_lima_canete,
       "adultez": fallecidos_adultez_lima_canete,
       "persona_mayor": fallecidos_persona_mayor_lima_canete
      }},

          {"name": "Huaral", "positivos": positivos_lima_huaral,"poblacion": poblacion_lima_huaral , "hombres_infectados": positivos_hombres_lima_huaral,"mujeres_infectados": positivos_mujeres_lima_huaral, "fallecidos": fallecidos_lima_huaral, "hombres_fallecidos": fallecidos_hombres_lima_huaral, "mujeres_fallecidos": fallecidos_mujeres_lima_huaral, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_huaral,
       "infancia": fallecidos_infancia_lima_huaral,
       "adolescencia": fallecidos_adolescencia_lima_huaral,
       "juventud": fallecidos_juventud_lima_huaral,
       "adultez": fallecidos_adultez_lima_huaral,
       "persona_mayor": fallecidos_persona_mayor_lima_huaral
      }},

          {"name": "Huarochiri", "positivos": positivos_lima_huarochiri,"poblacion": poblacion_lima_huarochiri , "hombres_infectados": positivos_hombres_lima_huarochiri,"mujeres_infectados": positivos_mujeres_lima_huarochiri, "fallecidos": fallecidos_lima_huarochiri, "hombres_fallecidos": fallecidos_hombres_lima_huarochiri, "mujeres_fallecidos": fallecidos_mujeres_lima_huarochiri, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_huarochiri,
       "infancia": fallecidos_infancia_lima_huarochiri,
       "adolescencia": fallecidos_adolescencia_lima_huarochiri,
       "juventud": fallecidos_juventud_lima_huarochiri,
       "adultez": fallecidos_adultez_lima_huarochiri,
       "persona_mayor": fallecidos_persona_mayor_lima_huarochiri
      }},

          {"name": "Huaura", "positivos": positivos_lima_huaura,"poblacion": poblacion_lima_huaura , "hombres_infectados": positivos_hombres_lima_huaura,"mujeres_infectados": positivos_mujeres_lima_huaura, "fallecidos": fallecidos_lima_huaura, "hombres_fallecidos": fallecidos_hombres_lima_huaura, "mujeres_fallecidos": fallecidos_mujeres_lima_huaura, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_huaura,
       "infancia": fallecidos_infancia_lima_huaura,
       "adolescencia": fallecidos_adolescencia_lima_huaura,
       "juventud": fallecidos_juventud_lima_huaura,
       "adultez": fallecidos_adultez_lima_huaura,
       "persona_mayor": fallecidos_persona_mayor_lima_huaura
      }},

          {"name": "Oyon", "positivos": positivos_lima_oyon,"poblacion": poblacion_lima_oyon , "hombres_infectados": positivos_hombres_lima_oyon,"mujeres_infectados": positivos_mujeres_lima_oyon, "fallecidos": fallecidos_lima_oyon, "hombres_fallecidos": fallecidos_hombres_lima_oyon, "mujeres_fallecidos": fallecidos_mujeres_lima_oyon, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_oyon,
       "infancia": fallecidos_infancia_lima_oyon,
       "adolescencia": fallecidos_adolescencia_lima_oyon,
       "juventud": fallecidos_juventud_lima_oyon,
       "adultez": fallecidos_adultez_lima_oyon,
       "persona_mayor": fallecidos_persona_mayor_lima_oyon
      }},

          {"name": "Yauyos", "positivos": positivos_lima_yauyos,"poblacion": poblacion_lima_yauyos , "hombres_infectados": positivos_hombres_lima_yauyos,"mujeres_infectados": positivos_mujeres_lima_yauyos, "fallecidos": fallecidos_lima_yauyos, "hombres_fallecidos": fallecidos_hombres_lima_yauyos, "mujeres_fallecidos": fallecidos_mujeres_lima_yauyos, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_yauyos,
       "infancia": fallecidos_infancia_lima_yauyos,
       "adolescencia": fallecidos_adolescencia_lima_yauyos,
       "juventud": fallecidos_juventud_lima_yauyos,
       "adultez": fallecidos_adultez_lima_yauyos,
       "persona_mayor": fallecidos_persona_mayor_lima_yauyos
      }}
      ]
    }

print(json.dumps(lima));
sys.stdout.flush();
