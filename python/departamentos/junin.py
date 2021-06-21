import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_junin = 1357263
positivos_junin = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "JUNIN"].shape)[0]
positivos_hombres_junin = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "JUNIN") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "JUNIN") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "JUNIN"].shape)[0]
fallecidos_hombres_junin  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "JUNIN") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_junin  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "JUNIN") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Departamento Junin - Etapa de vida
fallecidos_preinfancia_junin = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Junin
#!Junin-Huancayo
poblacion_junin_huancayo = 520516
positivos_junin_huancayo = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUANCAYO"].shape)[0]
positivos_hombres_junin_huancayo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANCAYO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin_huancayo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANCAYO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin_huancayo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUANCAYO"].shape)[0]
fallecidos_hombres_junin_huancayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAYO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_junin_huancayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAYO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Huancayo - Etapa de vida
fallecidos_preinfancia_junin_huancayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin_huancayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin_huancayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin_huancayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin_huancayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin_huancayo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Concepcion
poblacion_junin_concepcion = 57399
positivos_junin_concepcion = list(casos_positivos[casos_positivos['PROVINCIA'] == "CONCEPCION"].shape)[0]
positivos_hombres_junin_concepcion = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CONCEPCION") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin_concepcion = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CONCEPCION") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin_concepcion = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CONCEPCION"].shape)[0]
fallecidos_hombres_junin_concepcion  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONCEPCION") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_junin_concepcion  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONCEPCION") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Concepcion - Etapa de vida
fallecidos_preinfancia_junin_concepcion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONCEPCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin_concepcion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONCEPCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin_concepcion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONCEPCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin_concepcion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONCEPCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin_concepcion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONCEPCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin_concepcion = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONCEPCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Chanchamayo
poblacion_junin_chanchamayo = 199070
positivos_junin_chanchamayo = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHANCHAMAYO"].shape)[0]
positivos_hombres_junin_chanchamayo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHANCHAMAYO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin_chanchamayo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHANCHAMAYO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin_chanchamayo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHANCHAMAYO"].shape)[0]
fallecidos_hombres_junin_chanchamayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHANCHAMAYO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_junin_chanchamayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHANCHAMAYO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Chanchamayo - Etapa de vida
fallecidos_preinfancia_junin_chanchamayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHANCHAMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin_chanchamayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHANCHAMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin_chanchamayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHANCHAMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin_chanchamayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHANCHAMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin_chanchamayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHANCHAMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin_chanchamayo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHANCHAMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Junin-Jauja
poblacion_junin_jauja = 84924
positivos_junin_jauja = list(casos_positivos[casos_positivos['PROVINCIA'] == "JAUJA"].shape)[0]
positivos_hombres_junin_jauja = list(casos_positivos[(casos_positivos['PROVINCIA'] == "JAUJA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin_jauja = list(casos_positivos[(casos_positivos['PROVINCIA'] == "JAUJA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin_jauja = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "JAUJA"].shape)[0]
fallecidos_hombres_junin_jauja  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAUJA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_junin_jauja  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAUJA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Jauja - Etapa de vida
fallecidos_preinfancia_junin_jauja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAUJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin_jauja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAUJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin_jauja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAUJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin_jauja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAUJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin_jauja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAUJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin_jauja = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JAUJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]
    
#!Junin-Junin
poblacion_junin_junin = 26127
positivos_junin_junin = list(casos_positivos[casos_positivos['PROVINCIA'] == "JUNIN"].shape)[0]
positivos_hombres_junin_junin = list(casos_positivos[(casos_positivos['PROVINCIA'] == "JUNIN") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin_junin = list(casos_positivos[(casos_positivos['PROVINCIA'] == "JUNIN") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin_junin = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "JUNIN"].shape)[0]
fallecidos_hombres_junin_junin  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JUNIN") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_junin_junin  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA']   == "JUNIN") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Junin - Etapa de vida
fallecidos_preinfancia_junin_junin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin_junin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin_junin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin_junin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin_junin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin_junin = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JUNIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Satipo
poblacion_junin_satipo = 263330
positivos_junin_satipo = list(casos_positivos[casos_positivos['PROVINCIA'] == "SATIPO"].shape)[0]
positivos_hombres_junin_satipo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "SATIPO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin_satipo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "SATIPO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin_satipo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SATIPO"].shape)[0]
fallecidos_hombres_junin_satipo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_junin_satipo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA']   == "SATIPO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Satipo - Etapa de vida
fallecidos_preinfancia_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Tarma
poblacion_junin_tarma = 109330
positivos_junin_tarma = list(casos_positivos[casos_positivos['PROVINCIA'] == "TARMA"].shape)[0]
positivos_hombres_junin_tarma = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TARMA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin_tarma = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TARMA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin_tarma = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TARMA"].shape)[0]
fallecidos_hombres_junin_tarma  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TARMA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_junin_tarma  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TARMA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Tarma - Etapa de vida
fallecidos_preinfancia_junin_tarma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TARMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin_tarma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TARMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin_tarma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TARMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin_tarma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TARMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin_tarma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TARMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin_tarma = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TARMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Yauli
poblacion_junin_yauli = 41412
positivos_junin_yauli = list(casos_positivos[casos_positivos['PROVINCIA'] == "YAULI"].shape)[0]
positivos_hombres_junin_yauli = list(casos_positivos[(casos_positivos['PROVINCIA'] == "YAULI") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin_yauli = list(casos_positivos[(casos_positivos['PROVINCIA'] == "YAULI") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin_yauli = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "YAULI"].shape)[0]
fallecidos_hombres_junin_yauli  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAULI") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_junin_yauli  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAULI") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Yauli - Etapa de vida
fallecidos_preinfancia_junin_yauli = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAULI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin_yauli = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAULI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin_yauli = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAULI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin_yauli = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAULI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin_yauli = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAULI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin_yauli = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YAULI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Chupaca
poblacion_junin_chupaca = 55152
positivos_junin_chupaca = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHUPACA"].shape)[0]
positivos_hombres_junin_chupaca = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHUPACA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin_chupaca = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHUPACA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin_chupaca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHUPACA"].shape)[0]
fallecidos_hombres_junin_chupaca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUPACA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_junin_chupaca  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUPACA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Chupaca - Etapa de vida
fallecidos_preinfancia_junin_chupaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUPACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin_chupaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUPACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin_chupaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUPACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin_chupaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUPACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin_chupaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUPACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin_chupaca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHUPACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

junin =  {
      "name": "Junin",
      "poblacion": poblacion_junin,
      "positivos": positivos_junin,
      "hombres_infectados": positivos_hombres_junin,
      "mujeres_infectados": positivos_mujeres_junin,
      "fallecidos": fallecidos_junin,
      "hombres_fallecidos": fallecidos_hombres_junin,
      "mujeres_fallecidos": fallecidos_mujeres_junin,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin,
       "infancia": fallecidos_infancia_junin,
       "adolescencia": fallecidos_adolescencia_junin,
       "juventud": fallecidos_juventud_junin,
       "adultez": fallecidos_adultez_junin,
       "persona_mayor": fallecidos_persona_mayor_junin
      },
      "url": "junin",
      "provincias": [
          {"name": "Huancayo", "positivos": positivos_junin_huancayo,"poblacion": poblacion_junin_huancayo , "hombres_infectados": positivos_hombres_junin_huancayo,"mujeres_infectados": positivos_mujeres_junin_huancayo, "fallecidos": fallecidos_junin_huancayo,  "hombres_fallecidos": fallecidos_hombres_junin_huancayo, "mujeres_fallecidos": fallecidos_mujeres_junin_huancayo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_huancayo,
       "infancia": fallecidos_infancia_junin_huancayo,
       "adolescencia": fallecidos_adolescencia_junin_huancayo,
       "juventud": fallecidos_juventud_junin_huancayo,
       "adultez": fallecidos_adultez_junin_huancayo,
       "persona_mayor": fallecidos_persona_mayor_junin_huancayo
      }},

          {"name": "Concepcion", "positivos": positivos_junin_concepcion,"poblacion": poblacion_junin_concepcion , "hombres_infectados": positivos_hombres_junin_concepcion,"mujeres_infectados": positivos_mujeres_junin_concepcion, "fallecidos": fallecidos_junin_concepcion, "hombres_fallecidos": fallecidos_hombres_junin_concepcion, "mujeres_fallecidos": fallecidos_mujeres_junin_concepcion, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_concepcion,
       "infancia": fallecidos_infancia_junin_concepcion,
       "adolescencia": fallecidos_adolescencia_junin_concepcion,
       "juventud": fallecidos_juventud_junin_concepcion,
       "adultez": fallecidos_adultez_junin_concepcion,
       "persona_mayor": fallecidos_persona_mayor_junin_concepcion
      }},

          {"name": "Chanchamayo", "positivos": positivos_junin_chanchamayo,"poblacion": poblacion_junin_chanchamayo , "hombres_infectados": positivos_hombres_junin_chanchamayo,"mujeres_infectados": positivos_mujeres_junin_chanchamayo, "fallecidos": fallecidos_junin_chanchamayo, "hombres_fallecidos": fallecidos_hombres_junin_chanchamayo, "mujeres_fallecidos": fallecidos_mujeres_junin_chanchamayo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_chanchamayo,
       "infancia": fallecidos_infancia_junin_chanchamayo,
       "adolescencia": fallecidos_adolescencia_junin_chanchamayo,
       "juventud": fallecidos_juventud_junin_chanchamayo,
       "adultez": fallecidos_adultez_junin_chanchamayo,
       "persona_mayor": fallecidos_persona_mayor_junin_chanchamayo
      }},

          {"name": "Jauja", "positivos": positivos_junin_jauja,"poblacion": poblacion_junin_jauja , "hombres_infectados": positivos_hombres_junin_jauja,"mujeres_infectados": positivos_mujeres_junin_jauja, "fallecidos": fallecidos_junin_jauja, "hombres_fallecidos": fallecidos_hombres_junin_jauja, "mujeres_fallecidos": fallecidos_mujeres_junin_jauja, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_jauja,
       "infancia": fallecidos_infancia_junin_jauja,
       "adolescencia": fallecidos_adolescencia_junin_jauja,
       "juventud": fallecidos_juventud_junin_jauja,
       "adultez": fallecidos_adultez_junin_jauja,
       "persona_mayor": fallecidos_persona_mayor_junin_jauja
      }},

          {"name": "Junin", "positivos": positivos_junin_junin,"poblacion": poblacion_junin_junin , "hombres_infectados": positivos_hombres_junin_junin,"mujeres_infectados": positivos_mujeres_junin_junin, "fallecidos": fallecidos_junin_junin, "hombres_fallecidos": fallecidos_hombres_junin_junin, "mujeres_fallecidos": fallecidos_mujeres_junin_junin, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_junin,
       "infancia": fallecidos_infancia_junin_junin,
       "adolescencia": fallecidos_adolescencia_junin_junin,
       "juventud": fallecidos_juventud_junin_junin,
       "adultez": fallecidos_adultez_junin_junin,
       "persona_mayor": fallecidos_persona_mayor_junin_junin
      }},

          {"name": "Satipo", "positivos": positivos_junin_satipo,"poblacion": poblacion_junin_satipo , "hombres_infectados": positivos_hombres_junin_satipo,"mujeres_infectados": positivos_mujeres_junin_satipo, "fallecidos": fallecidos_junin_satipo, "hombres_fallecidos": fallecidos_hombres_junin_satipo, "mujeres_fallecidos": fallecidos_mujeres_junin_satipo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_satipo,
       "infancia": fallecidos_infancia_junin_satipo,
       "adolescencia": fallecidos_adolescencia_junin_satipo,
       "juventud": fallecidos_juventud_junin_satipo,
       "adultez": fallecidos_adultez_junin_satipo,
       "persona_mayor": fallecidos_persona_mayor_junin_satipo
      }},

          {"name": "Tarma", "positivos": positivos_junin_tarma,"poblacion": poblacion_junin_tarma , "hombres_infectados": positivos_hombres_junin_tarma,"mujeres_infectados": positivos_mujeres_junin_tarma, "fallecidos": fallecidos_junin_tarma, "hombres_fallecidos": fallecidos_hombres_junin_tarma, "mujeres_fallecidos": fallecidos_mujeres_junin_tarma, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_tarma,
       "infancia": fallecidos_infancia_junin_tarma,
       "adolescencia": fallecidos_adolescencia_junin_tarma,
       "juventud": fallecidos_juventud_junin_tarma,
       "adultez": fallecidos_adultez_junin_tarma,
       "persona_mayor": fallecidos_persona_mayor_junin_tarma
      }},

          {"name": "Yauli", "positivos": positivos_junin_yauli,"poblacion": poblacion_junin_yauli , "hombres_infectados": positivos_hombres_junin_yauli,"mujeres_infectados": positivos_mujeres_junin_yauli, "fallecidos": fallecidos_junin_yauli, "hombres_fallecidos": fallecidos_hombres_junin_yauli, "mujeres_fallecidos": fallecidos_mujeres_junin_yauli, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_yauli,
       "infancia": fallecidos_infancia_junin_yauli,
       "adolescencia": fallecidos_adolescencia_junin_yauli,
       "juventud": fallecidos_juventud_junin_yauli,
       "adultez": fallecidos_adultez_junin_yauli,
       "persona_mayor": fallecidos_persona_mayor_junin_yauli
      }},

          {"name": "Chupaca", "positivos": positivos_junin_chupaca,"poblacion": poblacion_junin_chupaca , "hombres_infectados": positivos_hombres_junin_chupaca,"mujeres_infectados": positivos_mujeres_junin_chupaca, "fallecidos": fallecidos_junin_chupaca, "hombres_fallecidos": fallecidos_hombres_junin_chupaca, "mujeres_fallecidos": fallecidos_mujeres_junin_chupaca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_chupaca,
       "infancia": fallecidos_infancia_junin_chupaca,
       "adolescencia": fallecidos_adolescencia_junin_chupaca,
       "juventud": fallecidos_juventud_junin_chupaca,
       "adultez": fallecidos_adultez_junin_chupaca,
       "persona_mayor": fallecidos_persona_mayor_junin_chupaca
      }}
      ]
    }

print(json.dumps(junin))
sys.stdout.flush();
