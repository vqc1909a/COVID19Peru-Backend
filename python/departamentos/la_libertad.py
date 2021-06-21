import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_libertad = 2031503
positivos_libertad = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "LA LIBERTAD"].shape)[0]
positivos_hombres_libertad = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LA LIBERTAD") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_libertad = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LA LIBERTAD") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_libertad = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "LA LIBERTAD"].shape)[0]
fallecidos_hombres_libertad  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LA LIBERTAD") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LA LIBERTAD") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Libertad - Etapa de vida
fallecidos_preinfancia_libertad = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LA LIBERTAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LA LIBERTAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LA LIBERTAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LA LIBERTAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LA LIBERTAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LA LIBERTAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Libertad
#!Libertad-Trujillo
poblacion_libertad_trujillo = 1061068
positivos_libertad_trujillo = list(casos_positivos[casos_positivos['PROVINCIA'] == "TRUJILLO"].shape)[0]
positivos_hombres_libertad_trujillo = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "TRUJILLO")].shape)[0]
positivos_mujeres_libertad_trujillo = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "TRUJILLO")].shape)[0]
fallecidos_libertad_trujillo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TRUJILLO"].shape)[0]
fallecidos_hombres_libertad_trujillo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TRUJILLO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_trujillo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TRUJILLO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Trujillo - Etapa de vida
fallecidos_preinfancia_libertad_trujillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TRUJILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_trujillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TRUJILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_trujillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TRUJILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_trujillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TRUJILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_trujillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TRUJILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_trujillo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TRUJILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Libertad-Ascope
poblacion_libertad_ascope = 131740
positivos_libertad_ascope = list(casos_positivos[casos_positivos['PROVINCIA'] == "ASCOPE"].shape)[0]
positivos_hombres_libertad_ascope = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "ASCOPE")].shape)[0]
positivos_mujeres_libertad_ascope = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "ASCOPE")].shape)[0]
fallecidos_libertad_ascope = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ASCOPE"].shape)[0]
fallecidos_hombres_libertad_ascope  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASCOPE") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_ascope  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASCOPE") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Ascope - Etapa de vida
fallecidos_preinfancia_libertad_ascope = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASCOPE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_ascope = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASCOPE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_ascope = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASCOPE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_ascope = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASCOPE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_ascope = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASCOPE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_ascope = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASCOPE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Libertad-Bolivar
poblacion_libertad_bolivar = 18073
positivos_libertad_bolivar = list(casos_positivos[casos_positivos['PROVINCIA'] == "BOLIVAR"].shape)[0]
positivos_hombres_libertad_bolivar = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "BOLIVAR")].shape)[0]
positivos_mujeres_libertad_bolivar = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "BOLIVAR")].shape)[0]
fallecidos_libertad_bolivar = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "BOLIVAR"].shape)[0]
fallecidos_hombres_libertad_bolivar  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLIVAR") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_bolivar  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLIVAR") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Bolivar - Etapa de vida
fallecidos_preinfancia_libertad_bolivar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLIVAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_bolivar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLIVAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_bolivar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLIVAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_bolivar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLIVAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_bolivar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLIVAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_bolivar = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLIVAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Libertad-Chepen
poblacion_libertad_chepen = 94412
positivos_libertad_chepen = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHEPEN"].shape)[0]
positivos_hombres_libertad_chepen = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CHEPEN")].shape)[0]
positivos_mujeres_libertad_chepen = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CHEPEN")].shape)[0]
fallecidos_libertad_chepen = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHEPEN"].shape)[0]
fallecidos_hombres_libertad_chepen  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHEPEN") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_chepen  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHEPEN") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Chepen - Etapa de vida
fallecidos_preinfancia_libertad_chepen = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHEPEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_chepen = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHEPEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_chepen = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHEPEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_chepen = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHEPEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_chepen = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHEPEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_chepen = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHEPEN") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Libertad-Julcan
poblacion_libertad_julcan = 32490
positivos_libertad_julcan = list(casos_positivos[casos_positivos['PROVINCIA'] == "JULCAN"].shape)[0]
positivos_hombres_libertad_julcan = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "JULCAN")].shape)[0]
positivos_mujeres_libertad_julcan = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "JULCAN")].shape)[0]
fallecidos_libertad_julcan = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "JULCAN"].shape)[0]
fallecidos_hombres_libertad_julcan  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JULCAN") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_julcan  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JULCAN") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Julcan - Etapa de vida
fallecidos_preinfancia_libertad_julcan = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JULCAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_julcan = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JULCAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_julcan = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JULCAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_julcan = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JULCAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_julcan = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JULCAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_julcan = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "JULCAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Libertad-Otuzco
poblacion_libertad_otuzco = 97826
positivos_libertad_otuzco = list(casos_positivos[casos_positivos['PROVINCIA'] == "OTUZCO"].shape)[0]
positivos_hombres_libertad_otuzco = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "OTUZCO")].shape)[0]
positivos_mujeres_libertad_otuzco = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "OTUZCO")].shape)[0]
fallecidos_libertad_otuzco = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "OTUZCO"].shape)[0]
fallecidos_hombres_libertad_otuzco  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OTUZCO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_otuzco  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OTUZCO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Otuzco - Etapa de vida
fallecidos_preinfancia_libertad_otuzco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OTUZCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_otuzco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OTUZCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_otuzco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OTUZCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_otuzco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OTUZCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_otuzco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OTUZCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_otuzco = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OTUZCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


    
#!Libertad-Pacasmayo
poblacion_libertad_pacasmayo = 112674
positivos_libertad_pacasmayo = list(casos_positivos[casos_positivos['PROVINCIA'] == "PACASMAYO"].shape)[0]
positivos_hombres_libertad_pacasmayo = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PACASMAYO")].shape)[0]
positivos_mujeres_libertad_pacasmayo = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PACASMAYO")].shape)[0]
fallecidos_libertad_pacasmayo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PACASMAYO"].shape)[0]
fallecidos_hombres_libertad_pacasmayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACASMAYO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_pacasmayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACASMAYO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Pacasmayo - Etapa de vida
fallecidos_preinfancia_libertad_pacasmayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACASMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_pacasmayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACASMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_pacasmayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACASMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_pacasmayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACASMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_pacasmayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACASMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_pacasmayo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PACASMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Libertad-Pataz
poblacion_libertad_pataz = 98138
positivos_libertad_pataz = list(casos_positivos[casos_positivos['PROVINCIA'] == "PATAZ"].shape)[0]
positivos_hombres_libertad_pataz = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PATAZ")].shape)[0]
positivos_mujeres_libertad_pataz = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PATAZ")].shape)[0]
fallecidos_libertad_pataz = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PATAZ"].shape)[0]
fallecidos_hombres_libertad_pataz   = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PATAZ") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_pataz   = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PATAZ") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Pataz - Etapa de vida
fallecidos_preinfancia_libertad_pataz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PATAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_pataz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PATAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_pataz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PATAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_pataz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PATAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_pataz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PATAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_pataz = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PATAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Sanchez Carrion
poblacion_libertad_sanchez_carrion = 167620
positivos_libertad_sanchez_carrion = list(casos_positivos[casos_positivos['PROVINCIA'] == "SANCHEZ CARRION"].shape)[0]
positivos_hombres_libertad_sanchez_carrion = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SANCHEZ CARRION")].shape)[0]
positivos_mujeres_libertad_sanchez_carrion = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SANCHEZ CARRION")].shape)[0]
fallecidos_libertad_sanchez_carrion = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SANCHEZ CARRION"].shape)[0]
fallecidos_hombres_libertad_sanchez_carrion   = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANCHEZ CARRION") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_sanchez_carrion   = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANCHEZ CARRION") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Sanchez Carrion - Etapa de vida
fallecidos_preinfancia_libertad_sanchez_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANCHEZ CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_sanchez_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANCHEZ CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_sanchez_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANCHEZ CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_sanchez_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANCHEZ CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_sanchez_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANCHEZ CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_sanchez_carrion = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANCHEZ CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Santiago de Chuco
poblacion_libertad_santiago_de_chuco = 65704
positivos_libertad_santiago_de_chuco = list(casos_positivos[casos_positivos['PROVINCIA'] == "SANTIAGO DE CHUCO"].shape)[0]
positivos_hombres_libertad_santiago_de_chuco = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SANTIAGO DE CHUCO")].shape)[0]
positivos_mujeres_libertad_santiago_de_chuco = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SANTIAGO DE CHUCO")].shape)[0]
fallecidos_libertad_santiago_de_chuco = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SANTIAGO DE CHUCO"].shape)[0]
fallecidos_hombres_libertad_santiago_de_chuco   = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTIAGO DE CHUCO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_santiago_de_chuco   = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTIAGO DE CHUCO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Santiago de Chuco - Etapa de vida
fallecidos_preinfancia_libertad_santiago_de_chuco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTIAGO DE CHUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_santiago_de_chuco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTIAGO DE CHUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_santiago_de_chuco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTIAGO DE CHUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_santiago_de_chuco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTIAGO DE CHUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_santiago_de_chuco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTIAGO DE CHUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_santiago_de_chuco = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTIAGO DE CHUCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Libertad-Gran Chimu
poblacion_libertad_gran_chimu = 32419
positivos_libertad_gran_chimu = list(casos_positivos[casos_positivos['PROVINCIA'] == "GRAN CHIMU"].shape)[0]
positivos_hombres_libertad_gran_chimu = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "GRAN CHIMU")].shape)[0]
positivos_mujeres_libertad_gran_chimu = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "GRAN CHIMU")].shape)[0]
fallecidos_libertad_gran_chimu = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "GRAN CHIMU"].shape)[0]
fallecidos_hombres_libertad_gran_chimu   = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAN CHIMU") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_gran_chimu   = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAN CHIMU") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Gran Chimu - Etapa de vida
fallecidos_preinfancia_libertad_gran_chimu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAN CHIMU") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_gran_chimu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAN CHIMU") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_gran_chimu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAN CHIMU") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_gran_chimu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAN CHIMU") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_gran_chimu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAN CHIMU") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_gran_chimu = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAN CHIMU") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Libertad-Viru
poblacion_libertad_viru = 119339
positivos_libertad_viru = list(casos_positivos[casos_positivos['PROVINCIA'] == "VIRU"].shape)[0]
positivos_hombres_libertad_viru = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "VIRU")].shape)[0]
positivos_mujeres_libertad_viru = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "VIRU")].shape)[0]
fallecidos_libertad_viru = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "VIRU"].shape)[0]
fallecidos_hombres_libertad_viru   = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VIRU") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_libertad_viru   = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VIRU") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Viru - Etapa de vida
fallecidos_preinfancia_libertad_viru = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VIRU") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_libertad_viru = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VIRU") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_libertad_viru = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VIRU") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_libertad_viru = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VIRU") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_libertad_viru = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VIRU") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_libertad_viru = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VIRU") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



lalibertad = {
      "name": "La Libertad",
      "poblacion": poblacion_libertad,
      "positivos": positivos_libertad,
      "hombres_infectados": positivos_hombres_libertad,
      "mujeres_infectados": positivos_mujeres_libertad,
      "fallecidos": fallecidos_libertad,
      "hombres_fallecidos": fallecidos_hombres_libertad,
      "mujeres_fallecidos": fallecidos_mujeres_libertad,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad,
       "infancia": fallecidos_infancia_libertad,
       "adolescencia": fallecidos_adolescencia_libertad,
       "juventud": fallecidos_juventud_libertad,
       "adultez": fallecidos_adultez_libertad,
       "persona_mayor": fallecidos_persona_mayor_libertad
      },
      "url": "la-libertad",
      "provincias": [
          {"name": "Trujillo", "positivos": positivos_libertad_trujillo, "poblacion": poblacion_libertad_trujillo,"hombres_infectados": positivos_hombres_libertad_trujillo,"mujeres_infectados": positivos_mujeres_libertad_trujillo, "fallecidos": fallecidos_libertad_trujillo, "hombres_fallecidos": fallecidos_hombres_libertad_trujillo,
      "mujeres_fallecidos": fallecidos_mujeres_libertad_trujillo, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_trujillo,
       "infancia": fallecidos_infancia_libertad_trujillo,
       "adolescencia": fallecidos_adolescencia_libertad_trujillo,
       "juventud": fallecidos_juventud_libertad_trujillo,
       "adultez": fallecidos_adultez_libertad_trujillo,
       "persona_mayor": fallecidos_persona_mayor_libertad_trujillo
      }},

          {"name": "Ascope", "positivos": positivos_libertad_ascope, "poblacion": poblacion_libertad_ascope,"hombres_infectados": positivos_hombres_libertad_ascope,"mujeres_infectados": positivos_mujeres_libertad_ascope, "fallecidos": fallecidos_libertad_ascope, "hombres_fallecidos": fallecidos_hombres_libertad_ascope,
      "mujeres_fallecidos": fallecidos_mujeres_libertad_ascope, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_ascope,
       "infancia": fallecidos_infancia_libertad_ascope,
       "adolescencia": fallecidos_adolescencia_libertad_ascope,
       "juventud": fallecidos_juventud_libertad_ascope,
       "adultez": fallecidos_adultez_libertad_ascope,
       "persona_mayor": fallecidos_persona_mayor_libertad_ascope
      }},

          {"name": "Bolivar", "positivos": positivos_libertad_bolivar, "poblacion": poblacion_libertad_bolivar,"hombres_infectados": positivos_hombres_libertad_bolivar,"mujeres_infectados": positivos_mujeres_libertad_bolivar, "fallecidos": fallecidos_libertad_bolivar, "hombres_fallecidos": fallecidos_hombres_libertad_bolivar,
      "mujeres_fallecidos": fallecidos_mujeres_libertad_bolivar, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_bolivar,
       "infancia": fallecidos_infancia_libertad_bolivar,
       "adolescencia": fallecidos_adolescencia_libertad_bolivar,
       "juventud": fallecidos_juventud_libertad_bolivar,
       "adultez": fallecidos_adultez_libertad_bolivar,
       "persona_mayor": fallecidos_persona_mayor_libertad_bolivar
      }},

          {"name": "Chepen", "positivos": positivos_libertad_chepen, "poblacion": poblacion_libertad_chepen,"hombres_infectados": positivos_hombres_libertad_chepen,"mujeres_infectados": positivos_mujeres_libertad_chepen, "fallecidos": fallecidos_libertad_chepen, "hombres_fallecidos": fallecidos_hombres_libertad_chepen,
      "mujeres_fallecidos": fallecidos_mujeres_libertad_chepen, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_chepen,
       "infancia": fallecidos_infancia_libertad_chepen,
       "adolescencia": fallecidos_adolescencia_libertad_chepen,
       "juventud": fallecidos_juventud_libertad_chepen,
       "adultez": fallecidos_adultez_libertad_chepen,
       "persona_mayor": fallecidos_persona_mayor_libertad_chepen
      }},

          {"name": "Julcan", "positivos": positivos_libertad_julcan, "poblacion": poblacion_libertad_julcan,"hombres_infectados": positivos_hombres_libertad_julcan,"mujeres_infectados": positivos_mujeres_libertad_julcan, "fallecidos": fallecidos_libertad_julcan, "hombres_fallecidos": fallecidos_hombres_libertad_julcan,
      "mujeres_fallecidos": fallecidos_mujeres_libertad_julcan, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_julcan,
       "infancia": fallecidos_infancia_libertad_julcan,
       "adolescencia": fallecidos_adolescencia_libertad_julcan,
       "juventud": fallecidos_juventud_libertad_julcan,
       "adultez": fallecidos_adultez_libertad_julcan,
       "persona_mayor": fallecidos_persona_mayor_libertad_julcan
      }},

          {"name": "Otuzco", "positivos": positivos_libertad_otuzco, "poblacion": poblacion_libertad_otuzco,"hombres_infectados": positivos_hombres_libertad_otuzco,"mujeres_infectados": positivos_mujeres_libertad_otuzco, "fallecidos": fallecidos_libertad_otuzco, "hombres_fallecidos": fallecidos_hombres_libertad_otuzco,
      "mujeres_fallecidos": fallecidos_mujeres_libertad_otuzco, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_otuzco,
       "infancia": fallecidos_infancia_libertad_otuzco,
       "adolescencia": fallecidos_adolescencia_libertad_otuzco,
       "juventud": fallecidos_juventud_libertad_otuzco,
       "adultez": fallecidos_adultez_libertad_otuzco,
       "persona_mayor": fallecidos_persona_mayor_libertad_otuzco
      }},

          {"name": "Pacasmayo", "positivos": positivos_libertad_pacasmayo, "poblacion": poblacion_libertad_pacasmayo,"hombres_infectados": positivos_hombres_libertad_pacasmayo,"mujeres_infectados": positivos_mujeres_libertad_pacasmayo, "fallecidos": fallecidos_libertad_pacasmayo, "hombres_fallecidos": fallecidos_hombres_libertad_pacasmayo,
      "mujeres_fallecidos": fallecidos_mujeres_libertad_pacasmayo, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_pacasmayo,
       "infancia": fallecidos_infancia_libertad_pacasmayo,
       "adolescencia": fallecidos_adolescencia_libertad_pacasmayo,
       "juventud": fallecidos_juventud_libertad_pacasmayo,
       "adultez": fallecidos_adultez_libertad_pacasmayo,
       "persona_mayor": fallecidos_persona_mayor_libertad_pacasmayo
      }},

          {"name": "Pataz", "positivos": positivos_libertad_pataz, "poblacion": poblacion_libertad_pataz,"hombres_infectados": positivos_hombres_libertad_pataz,"mujeres_infectados": positivos_mujeres_libertad_pataz, "fallecidos": fallecidos_libertad_pataz, "hombres_fallecidos": fallecidos_hombres_libertad_pataz, "mujeres_fallecidos": fallecidos_mujeres_libertad_pataz, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_pataz,
       "infancia": fallecidos_infancia_libertad_pataz,
       "adolescencia": fallecidos_adolescencia_libertad_pataz,
       "juventud": fallecidos_juventud_libertad_pataz,
       "adultez": fallecidos_adultez_libertad_pataz,
       "persona_mayor": fallecidos_persona_mayor_libertad_pataz
      }},

          {"name": "Sanchez Carrion", "positivos": positivos_libertad_sanchez_carrion, "poblacion": poblacion_libertad_sanchez_carrion, "hombres_infectados": positivos_hombres_libertad_sanchez_carrion, "mujeres_infectados": positivos_mujeres_libertad_sanchez_carrion, "fallecidos": fallecidos_libertad_sanchez_carrion, "hombres_fallecidos": fallecidos_hombres_libertad_sanchez_carrion, "mujeres_fallecidos": fallecidos_mujeres_libertad_sanchez_carrion, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_sanchez_carrion,
       "infancia": fallecidos_infancia_libertad_sanchez_carrion,
       "adolescencia": fallecidos_adolescencia_libertad_sanchez_carrion,
       "juventud": fallecidos_juventud_libertad_sanchez_carrion,
       "adultez": fallecidos_adultez_libertad_sanchez_carrion,
       "persona_mayor": fallecidos_persona_mayor_libertad_sanchez_carrion
      }},

          {"name": "Santiago de Chuco", "positivos": positivos_libertad_santiago_de_chuco, "poblacion": poblacion_libertad_santiago_de_chuco,"hombres_infectados": positivos_hombres_libertad_santiago_de_chuco,"mujeres_infectados": positivos_mujeres_libertad_santiago_de_chuco, "fallecidos": fallecidos_libertad_santiago_de_chuco, "hombres_fallecidos": fallecidos_hombres_libertad_santiago_de_chuco, "mujeres_fallecidos": fallecidos_mujeres_libertad_santiago_de_chuco, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_santiago_de_chuco,
       "infancia": fallecidos_infancia_libertad_santiago_de_chuco,
       "adolescencia": fallecidos_adolescencia_libertad_santiago_de_chuco,
       "juventud": fallecidos_juventud_libertad_santiago_de_chuco,
       "adultez": fallecidos_adultez_libertad_santiago_de_chuco,
       "persona_mayor": fallecidos_persona_mayor_libertad_santiago_de_chuco
      }},

          {"name": "Gran Chimu", "positivos": positivos_libertad_gran_chimu, "poblacion": poblacion_libertad_gran_chimu,"hombres_infectados": positivos_hombres_libertad_gran_chimu,"mujeres_infectados": positivos_mujeres_libertad_gran_chimu, "fallecidos": fallecidos_libertad_gran_chimu, "hombres_fallecidos": fallecidos_hombres_libertad_gran_chimu, "mujeres_fallecidos": fallecidos_mujeres_libertad_gran_chimu, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_gran_chimu,
       "infancia": fallecidos_infancia_libertad_gran_chimu,
       "adolescencia": fallecidos_adolescencia_libertad_gran_chimu,
       "juventud": fallecidos_juventud_libertad_gran_chimu,
       "adultez": fallecidos_adultez_libertad_gran_chimu,
       "persona_mayor": fallecidos_persona_mayor_libertad_gran_chimu
      }},

          {"name": "Viru", "positivos": positivos_libertad_viru, "poblacion": poblacion_libertad_viru,"hombres_infectados": positivos_hombres_libertad_viru,"mujeres_infectados": positivos_mujeres_libertad_viru, "fallecidos": fallecidos_libertad_viru, "hombres_fallecidos": fallecidos_hombres_libertad_viru, "mujeres_fallecidos": fallecidos_mujeres_libertad_viru, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_viru,
       "infancia": fallecidos_infancia_libertad_viru,
       "adolescencia": fallecidos_adolescencia_libertad_viru,
       "juventud": fallecidos_juventud_libertad_viru,
       "adultez": fallecidos_adultez_libertad_viru,
       "persona_mayor": fallecidos_persona_mayor_libertad_viru
      }},
      ]
    }

print(json.dumps(lalibertad));
sys.stdout.flush();
