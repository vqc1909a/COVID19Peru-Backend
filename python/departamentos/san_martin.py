import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_sanmartin = 906777
positivos_sanmartin = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "SAN MARTIN"].shape)[0]
positivos_hombres_sanmartin = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "SAN MARTIN") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_sanmartin = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "SAN MARTIN") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_sanmartin = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "SAN MARTIN"].shape)[0]
fallecidos_hombres_sanmartin  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "SAN MARTIN") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_sanmartin  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "SAN MARTIN") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento San Martin - Etapa de vida
fallecidos_preinfancia_sanmartin = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_sanmartin = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_sanmartin = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_sanmartin = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_sanmartin = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_sanmartin = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias San Martin
#!San Martin-Moyobamba
poblacion_san_martin_moyobamba = 157062
positivos_san_martin_moyobamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "MOYOBAMBA"].shape)[0]
positivos_hombres_san_martin_moyobamba = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "MOYOBAMBA")].shape)[0]
positivos_mujeres_san_martin_moyobamba = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "MOYOBAMBA")].shape)[0]
fallecidos_san_martin_moyobamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MOYOBAMBA"].shape)[0]
fallecidos_hombres_san_martin_moyobamba  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOYOBAMBA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_san_martin_moyobamba  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOYOBAMBA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Moyobamba - Etapa de vida
fallecidos_preinfancia_san_martin_moyobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOYOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_san_martin_moyobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOYOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_san_martin_moyobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOYOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_san_martin_moyobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOYOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_san_martin_moyobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOYOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_san_martin_moyobamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MOYOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!San Martin-Bellavista
poblacion_san_martin_bellavista = 62904
positivos_san_martin_bellavista = list(casos_positivos[casos_positivos['PROVINCIA'] == "BELLAVISTA"].shape)[0]
positivos_hombres_san_martin_bellavista = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "BELLAVISTA")].shape)[0]
positivos_mujeres_san_martin_bellavista = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "BELLAVISTA")].shape)[0]
fallecidos_san_martin_bellavista = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "BELLAVISTA"].shape)[0]
fallecidos_hombres_san_martin_bellavista  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BELLAVISTA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_san_martin_bellavista  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BELLAVISTA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Bellavista - Etapa de vida
fallecidos_preinfancia_san_martin_bellavista = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BELLAVISTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_san_martin_bellavista = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BELLAVISTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_san_martin_bellavista = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BELLAVISTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_san_martin_bellavista = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BELLAVISTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_san_martin_bellavista = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BELLAVISTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_san_martin_bellavista = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BELLAVISTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!San Martin-Dorado
poblacion_san_martin_dorado = 42819
positivos_san_martin_dorado = list(casos_positivos[casos_positivos['PROVINCIA'] == "EL DORADO"].shape)[0]
positivos_hombres_san_martin_dorado = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "EL DORADO")].shape)[0]
positivos_mujeres_san_martin_dorado = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "EL DORADO")].shape)[0]
fallecidos_san_martin_dorado = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "EL DORADO"].shape)[0]
fallecidos_hombres_san_martin_dorado  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL DORADO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_san_martin_dorado  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL DORADO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Dorado - Etapa de vida
fallecidos_preinfancia_san_martin_dorado = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL DORADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_san_martin_dorado = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL DORADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_san_martin_dorado = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL DORADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_san_martin_dorado = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL DORADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_san_martin_dorado = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL DORADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_san_martin_dorado = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "EL DORADO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!San Martin-Huallaga
poblacion_san_martin_huallaga = 27229
positivos_san_martin_huallaga = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUALLAGA"].shape)[0]
positivos_hombres_san_martin_huallaga = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUALLAGA")].shape)[0]
positivos_mujeres_san_martin_huallaga = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUALLAGA")].shape)[0]
fallecidos_san_martin_huallaga = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUALLAGA"].shape)[0]
fallecidos_hombres_san_martin_huallaga = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "HUALLAGA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_san_martin_huallaga = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "HUALLAGA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Huallaga - Etapa de vida
fallecidos_preinfancia_san_martin_huallaga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALLAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_san_martin_huallaga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALLAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_san_martin_huallaga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALLAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_san_martin_huallaga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALLAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_san_martin_huallaga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALLAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_san_martin_huallaga = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUALLAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!San Martin - Lamas
poblacion_san_martin_lamas = 90993
positivos_san_martin_lamas = list(casos_positivos[casos_positivos['PROVINCIA'] == "LAMAS"].shape)[0]
positivos_hombres_san_martin_lamas = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "LAMAS")].shape)[0]
positivos_mujeres_san_martin_lamas = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "LAMAS")].shape)[0]
fallecidos_san_martin_lamas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LAMAS"].shape)[0]
fallecidos_hombres_san_martin_lamas = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "LAMAS") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_san_martin_lamas = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "LAMAS") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Huallaga - Etapa de vida
fallecidos_preinfancia_san_martin_lamas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_san_martin_lamas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_san_martin_lamas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_san_martin_lamas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_san_martin_lamas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_san_martin_lamas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!San Martin-Mariscal Caceres
poblacion_san_martin_mariscal_caceres = 56563
positivos_san_martin_mariscal_caceres = list(casos_positivos[casos_positivos['PROVINCIA'] == "MARISCAL CACERES"].shape)[0]
positivos_hombres_san_martin_mariscal_caceres = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "MARISCAL CACERES")].shape)[0]
positivos_mujeres_san_martin_mariscal_caceres = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "MARISCAL CACERES")].shape)[0]
fallecidos_san_martin_mariscal_caceres = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MARISCAL CACERES"].shape)[0]
fallecidos_hombres_san_martin_mariscal_caceres = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "MARISCAL CACERES") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_san_martin_mariscal_caceres = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "MARISCAL CACERES") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Mariscal Caceres - Etapa de vida
fallecidos_preinfancia_san_martin_mariscal_caceres = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL CACERES") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_san_martin_mariscal_caceres = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL CACERES") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_san_martin_mariscal_caceres = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL CACERES") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_san_martin_mariscal_caceres = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL CACERES") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_san_martin_mariscal_caceres = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL CACERES") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_san_martin_mariscal_caceres = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL CACERES") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!San Martin-Provincia Picota
poblacion_san_martin_picota = 47178
positivos_san_martin_picota = list(casos_positivos[casos_positivos['PROVINCIA'] == "PICOTA"].shape)[0]
positivos_hombres_san_martin_picota = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PICOTA")].shape)[0]
positivos_mujeres_san_martin_picota = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PICOTA")].shape)[0]
fallecidos_san_martin_picota = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PICOTA"].shape)[0]
fallecidos_hombres_san_martin_picota = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "PICOTA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_san_martin_picota = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "PICOTA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Picota - Etapa de vida
fallecidos_preinfancia_san_martin_picota = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PICOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_san_martin_picota = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PICOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_san_martin_picota = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PICOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_san_martin_picota = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PICOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_san_martin_picota = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PICOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_san_martin_picota = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PICOTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Rioja
poblacion_san_martin_rioja = 138990
positivos_san_martin_rioja = list(casos_positivos[casos_positivos['PROVINCIA'] == "RIOJA"].shape)[0]
positivos_hombres_san_martin_rioja = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "RIOJA")].shape)[0]
positivos_mujeres_san_martin_rioja = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "RIOJA")].shape)[0]
fallecidos_san_martin_rioja = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "RIOJA"].shape)[0]
fallecidos_hombres_san_martin_rioja = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "RIOJA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_san_martin_rioja = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "RIOJA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Rioja - Etapa de vida
fallecidos_preinfancia_san_martin_rioja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RIOJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_san_martin_rioja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RIOJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_san_martin_rioja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RIOJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_san_martin_rioja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RIOJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_san_martin_rioja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RIOJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_san_martin_rioja = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RIOJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!San Martin-San Martin
poblacion_san_martin_san_martin = 203728
positivos_san_martin_san_martin = list(casos_positivos[casos_positivos['PROVINCIA'] == "SAN MARTIN"].shape)[0]
positivos_hombres_san_martin_san_martin = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SAN MARTIN")].shape)[0]
positivos_mujeres_san_martin_san_martin = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SAN MARTIN")].shape)[0]
fallecidos_san_martin_san_martin = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SAN MARTIN"].shape)[0]
fallecidos_hombres_san_martin_san_martin = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "SAN MARTIN") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_san_martin_san_martin = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "SAN MARTIN") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia San Martin - Etapa de vida
fallecidos_preinfancia_san_martin_san_martin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_san_martin_san_martin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_san_martin_san_martin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_san_martin_san_martin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_san_martin_san_martin = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_san_martin_san_martin = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SAN MARTIN") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!San Martin-Tocache
poblacion_san_martin_tocache = 79311
positivos_san_martin_tocache = list(casos_positivos[casos_positivos['PROVINCIA'] == "TOCACHE"].shape)[0]
positivos_hombres_san_martin_tocache = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "TOCACHE")].shape)[0]
positivos_mujeres_san_martin_tocache = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "TOCACHE")].shape)[0]
fallecidos_san_martin_tocache = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TOCACHE"].shape)[0]
fallecidos_hombres_san_martin_tocache = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "TOCACHE") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_san_martin_tocache = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "TOCACHE") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Tocache - Etapa de vida
fallecidos_preinfancia_san_martin_tocache = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TOCACHE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_san_martin_tocache = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TOCACHE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_san_martin_tocache = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TOCACHE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_san_martin_tocache = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TOCACHE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_san_martin_tocache = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TOCACHE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_san_martin_tocache = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TOCACHE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

sanmartin =  {
      "name": "San Martin",
      "poblacion": poblacion_sanmartin,
      "positivos": positivos_sanmartin,
      "hombres_infectados": positivos_hombres_sanmartin,
      "mujeres_infectados": positivos_mujeres_sanmartin,
      "fallecidos": fallecidos_sanmartin,
      "hombres_fallecidos": fallecidos_hombres_sanmartin,
      "mujeres_fallecidos": fallecidos_mujeres_sanmartin,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_sanmartin,
       "infancia": fallecidos_infancia_sanmartin,
       "adolescencia": fallecidos_adolescencia_sanmartin,
       "juventud": fallecidos_juventud_sanmartin,
       "adultez": fallecidos_adultez_sanmartin,
       "persona_mayor": fallecidos_persona_mayor_sanmartin
      },
      "url": "san-martin",
      "provincias": [
          {"name": "Moyobamba", "positivos": positivos_san_martin_moyobamba,"poblacion": poblacion_san_martin_moyobamba , "hombres_infectados": positivos_hombres_san_martin_moyobamba,"mujeres_infectados": positivos_mujeres_san_martin_moyobamba, "fallecidos": fallecidos_san_martin_moyobamba, "hombres_fallecidos": fallecidos_hombres_san_martin_moyobamba,
      "mujeres_fallecidos": fallecidos_mujeres_san_martin_moyobamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_moyobamba,
       "infancia": fallecidos_infancia_san_martin_moyobamba,
       "adolescencia": fallecidos_adolescencia_san_martin_moyobamba,
       "juventud": fallecidos_juventud_san_martin_moyobamba,
       "adultez": fallecidos_adultez_san_martin_moyobamba,
       "persona_mayor": fallecidos_persona_mayor_san_martin_moyobamba
      }},

          {"name": "Bellavista", "positivos": positivos_san_martin_bellavista,"poblacion": poblacion_san_martin_bellavista , "hombres_infectados": positivos_hombres_san_martin_bellavista,"mujeres_infectados": positivos_mujeres_san_martin_bellavista, "fallecidos": fallecidos_san_martin_bellavista, "hombres_fallecidos": fallecidos_hombres_san_martin_bellavista,
      "mujeres_fallecidos": fallecidos_mujeres_san_martin_bellavista, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_bellavista,
       "infancia": fallecidos_infancia_san_martin_bellavista,
       "adolescencia": fallecidos_adolescencia_san_martin_bellavista,
       "juventud": fallecidos_juventud_san_martin_bellavista,
       "adultez": fallecidos_adultez_san_martin_bellavista,
       "persona_mayor": fallecidos_persona_mayor_san_martin_bellavista
      }},

          {"name": "El Dorado", "positivos": positivos_san_martin_dorado,"poblacion": poblacion_san_martin_dorado , "hombres_infectados": positivos_hombres_san_martin_dorado,"mujeres_infectados": positivos_mujeres_san_martin_dorado, "fallecidos": fallecidos_san_martin_dorado, "hombres_fallecidos": fallecidos_hombres_san_martin_dorado,
      "mujeres_fallecidos": fallecidos_mujeres_san_martin_dorado, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_dorado,
       "infancia": fallecidos_infancia_san_martin_dorado,
       "adolescencia": fallecidos_adolescencia_san_martin_dorado,
       "juventud": fallecidos_juventud_san_martin_dorado,
       "adultez": fallecidos_adultez_san_martin_dorado,
       "persona_mayor": fallecidos_persona_mayor_san_martin_dorado
      }},

          {"name": "Huallaga", "positivos": positivos_san_martin_huallaga,"poblacion": poblacion_san_martin_huallaga , "hombres_infectados": positivos_hombres_san_martin_huallaga,"mujeres_infectados": positivos_mujeres_san_martin_huallaga, "fallecidos": fallecidos_san_martin_huallaga, "hombres_fallecidos": fallecidos_hombres_san_martin_huallaga,
      "mujeres_fallecidos": fallecidos_mujeres_san_martin_huallaga, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_huallaga,
       "infancia": fallecidos_infancia_san_martin_huallaga,
       "adolescencia": fallecidos_adolescencia_san_martin_huallaga,
       "juventud": fallecidos_juventud_san_martin_huallaga,
       "adultez": fallecidos_adultez_san_martin_huallaga,
       "persona_mayor": fallecidos_persona_mayor_san_martin_huallaga
      }},

          {"name": "Lamas", "positivos": positivos_san_martin_lamas,"poblacion": poblacion_san_martin_lamas , "hombres_infectados": positivos_hombres_san_martin_lamas,"mujeres_infectados": positivos_mujeres_san_martin_lamas, "fallecidos": fallecidos_san_martin_lamas, "hombres_fallecidos": fallecidos_hombres_san_martin_lamas,
      "mujeres_fallecidos": fallecidos_mujeres_san_martin_lamas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_lamas,
       "infancia": fallecidos_infancia_san_martin_lamas,
       "adolescencia": fallecidos_adolescencia_san_martin_lamas,
       "juventud": fallecidos_juventud_san_martin_lamas,
       "adultez": fallecidos_adultez_san_martin_lamas,
       "persona_mayor": fallecidos_persona_mayor_san_martin_lamas
      }},

          {"name": "Mariscal Caceres", "positivos": positivos_san_martin_mariscal_caceres,"poblacion": poblacion_san_martin_mariscal_caceres , "hombres_infectados": positivos_hombres_san_martin_mariscal_caceres,"mujeres_infectados": positivos_mujeres_san_martin_mariscal_caceres, "fallecidos": fallecidos_san_martin_mariscal_caceres, "hombres_fallecidos": fallecidos_hombres_san_martin_mariscal_caceres, "mujeres_fallecidos": fallecidos_mujeres_san_martin_mariscal_caceres, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_mariscal_caceres,
       "infancia": fallecidos_infancia_san_martin_mariscal_caceres,
       "adolescencia": fallecidos_adolescencia_san_martin_mariscal_caceres,
       "juventud": fallecidos_juventud_san_martin_mariscal_caceres,
       "adultez": fallecidos_adultez_san_martin_mariscal_caceres,
       "persona_mayor": fallecidos_persona_mayor_san_martin_mariscal_caceres
      }},

          {"name": "Picota", "positivos": positivos_san_martin_picota, "poblacion": poblacion_san_martin_picota, "hombres_infectados": positivos_hombres_san_martin_picota, "mujeres_infectados": positivos_mujeres_san_martin_picota, "fallecidos": fallecidos_san_martin_picota, "hombres_fallecidos": fallecidos_hombres_san_martin_picota, "mujeres_fallecidos": fallecidos_mujeres_san_martin_picota, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_picota,
       "infancia": fallecidos_infancia_san_martin_picota,
       "adolescencia": fallecidos_adolescencia_san_martin_picota,
       "juventud": fallecidos_juventud_san_martin_picota,
       "adultez": fallecidos_adultez_san_martin_picota,
       "persona_mayor": fallecidos_persona_mayor_san_martin_picota
      }},

          {"name": "Rioja", "positivos": positivos_san_martin_rioja,"poblacion": poblacion_san_martin_rioja , "hombres_infectados": positivos_hombres_san_martin_rioja,"mujeres_infectados": positivos_mujeres_san_martin_rioja, "fallecidos": fallecidos_san_martin_rioja, "hombres_fallecidos": fallecidos_hombres_san_martin_rioja, "mujeres_fallecidos": fallecidos_mujeres_san_martin_rioja, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_rioja,
       "infancia": fallecidos_infancia_san_martin_rioja,
       "adolescencia": fallecidos_adolescencia_san_martin_rioja,
       "juventud": fallecidos_juventud_san_martin_rioja,
       "adultez": fallecidos_adultez_san_martin_rioja,
       "persona_mayor": fallecidos_persona_mayor_san_martin_rioja
      }},

          {"name": "San Martin", "positivos": positivos_san_martin_san_martin,"poblacion": poblacion_san_martin_san_martin , "hombres_infectados": positivos_hombres_san_martin_san_martin,"mujeres_infectados": positivos_mujeres_san_martin_san_martin, "fallecidos": fallecidos_san_martin_san_martin, "hombres_fallecidos": fallecidos_hombres_san_martin_san_martin, "mujeres_fallecidos": fallecidos_mujeres_san_martin_san_martin, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_san_martin,
       "infancia": fallecidos_infancia_san_martin_san_martin,
       "adolescencia": fallecidos_adolescencia_san_martin_san_martin,
       "juventud": fallecidos_juventud_san_martin_san_martin,
       "adultez": fallecidos_adultez_san_martin_san_martin,
       "persona_mayor": fallecidos_persona_mayor_san_martin_san_martin
      }},

          {"name": "Tocache", "positivos": positivos_san_martin_tocache,"poblacion": poblacion_san_martin_tocache , "hombres_infectados": positivos_hombres_san_martin_tocache,"mujeres_infectados": positivos_mujeres_san_martin_tocache, "fallecidos": fallecidos_san_martin_tocache, "hombres_fallecidos": fallecidos_hombres_san_martin_tocache, "mujeres_fallecidos": fallecidos_mujeres_san_martin_tocache, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_tocache,
       "infancia": fallecidos_infancia_san_martin_tocache,
       "adolescencia": fallecidos_adolescencia_san_martin_tocache,
       "juventud": fallecidos_juventud_san_martin_tocache,
       "adultez": fallecidos_adultez_san_martin_tocache,
       "persona_mayor": fallecidos_persona_mayor_san_martin_tocache
      }}
      ]
    }


print(json.dumps(sanmartin));
sys.stdout.flush();
