import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_ancash = 1175871
positivos_ancash = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "ANCASH"].shape)[0]
positivos_hombres_ancash = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "ANCASH") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ancash = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "ANCASH") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ancash = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "ANCASH"].shape)[0]
fallecidos_hombres_ancash = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ANCASH") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ANCASH") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Ancash - Etapa de vida
fallecidos_preinfancia_ancash = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ANCASH") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ANCASH") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ANCASH") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ANCASH") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ANCASH") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ANCASH") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Ancash
#!Ancash-Huaraz
poblacion_ancash_huaraz = 172878
positivos_ancash_huaraz = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUARAZ"].shape)[0]
positivos_hombres_ancash_huaraz = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUARAZ")].shape)[0]
positivos_mujeres_ancash_huaraz = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUARAZ")].shape)[0]
fallecidos_ancash_huaraz = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUARAZ"].shape)[0]
fallecidos_hombres_ancash_huaraz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAZ") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_huaraz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAZ") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Huaraz - Etapa de vida
fallecidos_preinfancia_ancash_huaraz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_huaraz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_huaraz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_huaraz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_huaraz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_huaraz = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Ancash-Aija
poblacion_ancash_aija = 7674
positivos_ancash_aija = list(casos_positivos[casos_positivos['PROVINCIA'] == "AIJA"].shape)[0]
positivos_hombres_ancash_aija = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "AIJA")].shape)[0]
positivos_mujeres_ancash_aija = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "AIJA")].shape)[0]
fallecidos_ancash_aija = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "AIJA"].shape)[0]
fallecidos_hombres_ancash_aija = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AIJA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_aija = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AIJA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Aija - Etapa de vida
fallecidos_preinfancia_ancash_aija = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AIJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_aija = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AIJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_aija = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AIJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_aija = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AIJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_aija = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AIJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_aija = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AIJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Antonio Raimondi
poblacion_ancash_antonio_raimondi = 16232
positivos_ancash_antonio_raimondi = list(casos_positivos[casos_positivos['PROVINCIA'] == "ANTONIO RAIMONDI"].shape)[0]
positivos_hombres_ancash_antonio_raimondi = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "ANTONIO RAIMONDI")].shape)[0]
positivos_mujeres_ancash_antonio_raimondi = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "ANTONIO RAIMONDI")].shape)[0]
fallecidos_ancash_antonio_raimondi = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ANTONIO RAIMONDI"].shape)[0]
fallecidos_hombres_ancash_antonio_raimondi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTONIO RAIMONDI") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_antonio_raimondi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTONIO RAIMONDI") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Antonio Raimondi - Etapa de vida
fallecidos_preinfancia_ancash_antonio_raimondi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTONIO RAIMONDI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_antonio_raimondi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTONIO RAIMONDI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_antonio_raimondi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTONIO RAIMONDI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_antonio_raimondi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTONIO RAIMONDI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_antonio_raimondi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTONIO RAIMONDI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_antonio_raimondi = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTONIO RAIMONDI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Asuncion
poblacion_ancash_asuncion = 8735
positivos_ancash_asuncion = list(casos_positivos[casos_positivos['PROVINCIA'] == "ASUNCION"].shape)[0]
positivos_hombres_ancash_asuncion = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "ASUNCION")].shape)[0]
positivos_mujeres_ancash_asuncion = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "ASUNCION")].shape)[0]
fallecidos_ancash_asuncion = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ASUNCION"].shape)[0]
fallecidos_hombres_ancash_asuncion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASUNCION") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_asuncion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASUNCION") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Asuncion - Etapa de vida
fallecidos_preinfancia_ancash_asuncion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASUNCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_asuncion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASUNCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_asuncion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASUNCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_asuncion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASUNCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_asuncion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASUNCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_asuncion = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ASUNCION") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Bolognesi
poblacion_ancash_bolognesi = 32871
positivos_ancash_bolognesi = list(casos_positivos[casos_positivos['PROVINCIA'] == "BOLOGNESI"].shape)[0]
positivos_hombres_ancash_bolognesi = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "BOLOGNESI")].shape)[0]
positivos_mujeres_ancash_bolognesi = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "BOLOGNESI")].shape)[0]
fallecidos_ancash_bolognesi = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "BOLOGNESI"].shape)[0]
fallecidos_hombres_ancash_bolognesi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLOGNESI") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_bolognesi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLOGNESI") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Bolognesi - Etapa de vida
fallecidos_preinfancia_ancash_bolognesi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLOGNESI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_bolognesi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLOGNESI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_bolognesi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLOGNESI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_bolognesi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLOGNESI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_bolognesi = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLOGNESI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_bolognesi = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BOLOGNESI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Carhuaz
poblacion_ancash_carhuaz = 48419
positivos_ancash_carhuaz = list(casos_positivos[casos_positivos['PROVINCIA'] == "CARHUAZ"].shape)[0]
positivos_hombres_ancash_carhuaz = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CARHUAZ")].shape)[0]
positivos_mujeres_ancash_carhuaz = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CARHUAZ")].shape)[0]
fallecidos_ancash_carhuaz = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CARHUAZ"].shape)[0]
fallecidos_hombres_ancash_carhuaz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARHUAZ") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_carhuaz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARHUAZ") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Carhuaz - Etapa de vida
fallecidos_preinfancia_ancash_carhuaz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARHUAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_carhuaz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARHUAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_carhuaz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARHUAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_carhuaz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARHUAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_carhuaz = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARHUAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_carhuaz = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARHUAZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Ancash-Carlos Fermin
poblacion_ancash_carlos_fermin_fitzcarrald = 21209
positivos_ancash_carlos_fermin_fitzcarrald = list(casos_positivos[casos_positivos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD"].shape)[0]
positivos_hombres_ancash_carlos_fermin_fitzcarrald = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD")].shape)[0]
positivos_mujeres_ancash_carlos_fermin_fitzcarrald = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD")].shape)[0]
fallecidos_ancash_carlos_fermin_fitzcarrald = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD"].shape)[0]
fallecidos_hombres_ancash_carlos_fermin_fitzcarrald = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_carlos_fermin_fitzcarrald = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Carlos Fermin - Etapa de vida
fallecidos_preinfancia_ancash_carlos_fermin_fitzcarrald = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_carlos_fermin_fitzcarrald = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_carlos_fermin_fitzcarrald = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_carlos_fermin_fitzcarrald = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_carlos_fermin_fitzcarrald = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_carlos_fermin_fitzcarrald = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CARLOS FERMIN FITZCARRALD") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Casma
poblacion_ancash_casma = 49540
positivos_ancash_casma = list(casos_positivos[casos_positivos['PROVINCIA'] == "CASMA"].shape)[0]
positivos_hombres_ancash_casma = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CASMA")].shape)[0]
positivos_mujeres_ancash_casma = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CASMA")].shape)[0]
fallecidos_ancash_casma = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CASMA"].shape)[0]
fallecidos_hombres_ancash_casma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASMA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_casma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASMA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Casma - Etapa de vida
fallecidos_preinfancia_ancash_casma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_casma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_casma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_casma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_casma = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_casma = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Corongo
poblacion_ancash_corongo = 8362
positivos_ancash_corongo = list(casos_positivos[casos_positivos['PROVINCIA'] == "CORONGO"].shape)[0]
positivos_hombres_ancash_corongo = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CORONGO")].shape)[0]
positivos_mujeres_ancash_corongo = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CORONGO")].shape)[0]
fallecidos_ancash_corongo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CORONGO"].shape)[0]
fallecidos_hombres_ancash_corongo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONGO") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_corongo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONGO") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Corongo - Etapa de vida
fallecidos_preinfancia_ancash_corongo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONGO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_corongo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONGO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_corongo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONGO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_corongo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONGO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_corongo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONGO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_corongo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONGO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Huari
poblacion_ancash_huari = 64417
positivos_ancash_huari = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUARI"].shape)[0]
positivos_hombres_ancash_huari = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUARI")].shape)[0]
positivos_mujeres_ancash_huari = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUARI")].shape)[0]
fallecidos_ancash_huari = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUARI"].shape)[0]
fallecidos_hombres_ancash_huari = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARI") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_huari = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARI") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Huari - Etapa de vida
fallecidos_preinfancia_ancash_huari = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_huari = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_huari = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_huari = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_huari = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_huari = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Huarmey
poblacion_ancash_huarmey = 32068
positivos_ancash_huarmey = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUARMEY"].shape)[0]
positivos_hombres_ancash_huarmey = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUARMEY")].shape)[0]
positivos_mujeres_ancash_huarmey = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUARMEY")].shape)[0]
fallecidos_ancash_huarmey = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUARMEY"].shape)[0]
fallecidos_hombres_ancash_huarmey = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARMEY") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_huarmey = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARMEY") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Huarmey - Etapa de vida
fallecidos_preinfancia_ancash_huarmey = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARMEY") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_huarmey = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARMEY") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_huarmey = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARMEY") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_huarmey = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARMEY") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_huarmey = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARMEY") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_huarmey = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUARMEY") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Huaylas
poblacion_ancash_huaylas = 57265
positivos_ancash_huaylas = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUAYLAS"].shape)[0]
positivos_hombres_ancash_huaylas = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUAYLAS")].shape)[0]
positivos_mujeres_ancash_huaylas = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUAYLAS")].shape)[0]
fallecidos_ancash_huaylas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUAYLAS"].shape)[0]
fallecidos_hombres_ancash_huaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYLAS") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_huaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYLAS") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Huaylas - Etapa de vida
fallecidos_preinfancia_ancash_huaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_huaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_huaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_huaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_huaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_huaylas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Ancash-Mariscal Luzuriaga
poblacion_ancash_mariscal_luzuriaga = 23091
positivos_ancash_mariscal_luzuriaga = list(casos_positivos[casos_positivos['PROVINCIA'] == "MARISCAL LUZURIAGA"].shape)[0]
positivos_hombres_ancash_mariscal_luzuriaga = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "MARISCAL LUZURIAGA")].shape)[0]
positivos_mujeres_ancash_mariscal_luzuriaga = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "MARISCAL LUZURIAGA")].shape)[0]
fallecidos_ancash_mariscal_luzuriaga = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MARISCAL LUZURIAGA"].shape)[0]
fallecidos_hombres_ancash_mariscal_luzuriaga = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "MARISCAL LUZURIAGA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_mariscal_luzuriaga = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "MARISCAL LUZURIAGA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Mariscal Luzuriaga - Etapa de vida
fallecidos_preinfancia_ancash_mariscal_luzuriaga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL LUZURIAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_mariscal_luzuriaga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL LUZURIAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_mariscal_luzuriaga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL LUZURIAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_mariscal_luzuriaga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL LUZURIAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_mariscal_luzuriaga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL LUZURIAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_mariscal_luzuriaga = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL LUZURIAGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Ocros
poblacion_ancash_ocros = 10694
positivos_ancash_ocros = list(casos_positivos[casos_positivos['PROVINCIA'] == "OCROS"].shape)[0]
positivos_hombres_ancash_ocros = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "OCROS")].shape)[0]
positivos_mujeres_ancash_ocros = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "OCROS")].shape)[0]
fallecidos_ancash_ocros = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "OCROS"].shape)[0]
fallecidos_hombres_ancash_ocros = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "OCROS") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_ocros = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "OCROS") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Ocros - Etapa de vida
fallecidos_preinfancia_ancash_ocros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OCROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_ocros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OCROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_ocros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OCROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_ocros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OCROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_ocros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OCROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_ocros = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OCROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Pallasca
poblacion_ancash_pallasca = 30063
positivos_ancash_pallasca = list(casos_positivos[casos_positivos['PROVINCIA'] == "PALLASCA"].shape)[0]
positivos_hombres_ancash_pallasca = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PALLASCA")].shape)[0]
positivos_mujeres_ancash_pallasca = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PALLASCA")].shape)[0]
fallecidos_ancash_pallasca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PALLASCA"].shape)[0]
fallecidos_hombres_ancash_pallasca = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "PALLASCA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_pallasca = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "PALLASCA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Pallasca - Etapa de vida
fallecidos_preinfancia_ancash_pallasca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALLASCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_pallasca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALLASCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_pallasca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALLASCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_pallasca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALLASCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_pallasca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALLASCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_pallasca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALLASCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Ancash-Pomabamba
poblacion_ancash_pomabamba = 29071
positivos_ancash_pomabamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "POMABAMBA"].shape)[0]
positivos_hombres_ancash_pomabamba = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "POMABAMBA")].shape)[0]
positivos_mujeres_ancash_pomabamba = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "POMABAMBA")].shape)[0]
fallecidos_ancash_pomabamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "POMABAMBA"].shape)[0]
fallecidos_hombres_ancash_pomabamba = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "POMABAMBA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_pomabamba = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "POMABAMBA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Pomabamba - Etapa de vida
fallecidos_preinfancia_ancash_pomabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "POMABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_pomabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "POMABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_pomabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "POMABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_pomabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "POMABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_pomabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "POMABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_pomabamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "POMABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Recuay
poblacion_ancash_recuay = 19836
positivos_ancash_recuay = list(casos_positivos[casos_positivos['PROVINCIA'] == "RECUAY"].shape)[0]
positivos_hombres_ancash_recuay = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "RECUAY")].shape)[0]
positivos_mujeres_ancash_recuay = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "RECUAY")].shape)[0]
fallecidos_ancash_recuay = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "RECUAY"].shape)[0]
fallecidos_hombres_ancash_recuay = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "RECUAY") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_recuay = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "RECUAY") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


#!Provincia Recuay - Etapa de vida
fallecidos_preinfancia_ancash_recuay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RECUAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_recuay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RECUAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_recuay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RECUAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_recuay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RECUAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_recuay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RECUAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_recuay = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RECUAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Santa
poblacion_ancash_santa = 454242
positivos_ancash_santa = list(casos_positivos[casos_positivos['PROVINCIA'] == "SANTA"].shape)[0]
positivos_hombres_ancash_santa = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SANTA")].shape)[0]
positivos_mujeres_ancash_santa = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SANTA")].shape)[0]
fallecidos_ancash_santa = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SANTA"].shape)[0]
fallecidos_hombres_ancash_santa = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "SANTA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_santa = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "SANTA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Santa - Etapa de vida
fallecidos_preinfancia_ancash_santa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_santa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_santa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_santa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_santa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_santa = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Sihuas
poblacion_ancash_sihuas = 30415
positivos_ancash_sihuas = list(casos_positivos[casos_positivos['PROVINCIA'] == "SIHUAS"].shape)[0]
positivos_hombres_ancash_sihuas = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SIHUAS")].shape)[0]
positivos_mujeres_ancash_sihuas = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SIHUAS")].shape)[0]
fallecidos_ancash_sihuas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SIHUAS"].shape)[0]
fallecidos_hombres_ancash_sihuas = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "SIHUAS") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_sihuas = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "SIHUAS") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Santa - Etapa de vida
fallecidos_preinfancia_ancash_sihuas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SIHUAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_sihuas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SIHUAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_sihuas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SIHUAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_sihuas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SIHUAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_sihuas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SIHUAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_sihuas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SIHUAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ancash-Yungay
poblacion_ancash_yungay = 58789
positivos_ancash_yungay = list(casos_positivos[casos_positivos['PROVINCIA'] == "YUNGAY"].shape)[0]
positivos_hombres_ancash_yungay = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "YUNGAY")].shape)[0]
positivos_mujeres_ancash_yungay = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "YUNGAY")].shape)[0]
fallecidos_ancash_yungay = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "YUNGAY"].shape)[0]
fallecidos_hombres_ancash_yungay = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "YUNGAY") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ancash_yungay = list(casos_fallecidos[(
    casos_fallecidos['PROVINCIA'] == "YUNGAY") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Provincia Santa - Etapa de vida
fallecidos_preinfancia_ancash_yungay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ancash_yungay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ancash_yungay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ancash_yungay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ancash_yungay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ancash_yungay = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "YUNGAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

ancash =  {
      "name": "Ancash",
      "poblacion": poblacion_ancash,
      "positivos": positivos_ancash,
      "hombres_infectados": positivos_hombres_ancash,
      "mujeres_infectados": positivos_mujeres_ancash,
      "fallecidos": fallecidos_ancash,
      "hombres_fallecidos": fallecidos_hombres_ancash,
      "mujeres_fallecidos": fallecidos_mujeres_ancash,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash,
       "infancia": fallecidos_infancia_ancash,
       "adolescencia": fallecidos_adolescencia_ancash,
       "juventud": fallecidos_juventud_ancash,
       "adultez": fallecidos_adultez_ancash,
       "persona_mayor": fallecidos_persona_mayor_ancash
      },
      "url": "ancash",
      "provincias": [
          {"name": "Huaraz", "positivos": positivos_ancash_huaraz, "poblacion": poblacion_ancash_huaraz , "hombres_infectados": positivos_hombres_ancash_huaraz,"mujeres_infectados": positivos_mujeres_ancash_huaraz, "fallecidos": fallecidos_ancash_huaraz, "hombres_fallecidos": fallecidos_hombres_ancash_huaraz,
      "mujeres_fallecidos": fallecidos_mujeres_ancash_huaraz, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_huaraz,
       "infancia": fallecidos_infancia_ancash_huaraz,
       "adolescencia": fallecidos_adolescencia_ancash_huaraz,
       "juventud": fallecidos_juventud_ancash_huaraz,
       "adultez": fallecidos_adultez_ancash_huaraz,
       "persona_mayor": fallecidos_persona_mayor_ancash_huaraz
      }},

          {"name": "Aija", "positivos": positivos_ancash_aija, "poblacion": poblacion_ancash_aija, "hombres_infectados": positivos_hombres_ancash_aija, "mujeres_infectados": positivos_mujeres_ancash_aija, "fallecidos": fallecidos_ancash_aija, "hombres_fallecidos": fallecidos_hombres_ancash_aija,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_aija, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_aija,
       "infancia": fallecidos_infancia_ancash_aija,
       "adolescencia": fallecidos_adolescencia_ancash_aija,
       "juventud": fallecidos_juventud_ancash_aija,
       "adultez": fallecidos_adultez_ancash_aija,
       "persona_mayor": fallecidos_persona_mayor_ancash_aija
      }},

          {"name": "Antonio Raymondi", "positivos": positivos_ancash_antonio_raimondi, "poblacion": poblacion_ancash_antonio_raimondi , "hombres_infectados": positivos_hombres_ancash_antonio_raimondi,"mujeres_infectados": positivos_mujeres_ancash_antonio_raimondi, "fallecidos": fallecidos_ancash_antonio_raimondi, "hombres_fallecidos": fallecidos_hombres_ancash_antonio_raimondi,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_antonio_raimondi, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_antonio_raimondi,
       "infancia": fallecidos_infancia_ancash_antonio_raimondi,
       "adolescencia": fallecidos_adolescencia_ancash_antonio_raimondi,
       "juventud": fallecidos_juventud_ancash_antonio_raimondi,
       "adultez": fallecidos_adultez_ancash_antonio_raimondi,
       "persona_mayor": fallecidos_persona_mayor_ancash_antonio_raimondi
      }},

          {"name": "Asuncion", "positivos": positivos_ancash_asuncion, "poblacion": poblacion_ancash_asuncion , "hombres_infectados": positivos_hombres_ancash_asuncion,"mujeres_infectados": positivos_mujeres_ancash_asuncion, "fallecidos": fallecidos_ancash_asuncion, "hombres_fallecidos": fallecidos_hombres_ancash_asuncion,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_asuncion, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_asuncion,
       "infancia": fallecidos_infancia_ancash_asuncion,
       "adolescencia": fallecidos_adolescencia_ancash_asuncion,
       "juventud": fallecidos_juventud_ancash_asuncion,
       "adultez": fallecidos_adultez_ancash_asuncion,
       "persona_mayor": fallecidos_persona_mayor_ancash_asuncion
      }},

          {"name": "Bolognesi", "positivos": positivos_ancash_bolognesi, "poblacion": poblacion_ancash_bolognesi , "hombres_infectados": positivos_hombres_ancash_bolognesi,"mujeres_infectados": positivos_mujeres_ancash_bolognesi, "fallecidos": fallecidos_ancash_bolognesi, "hombres_fallecidos": fallecidos_hombres_ancash_bolognesi,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_bolognesi, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_bolognesi,
       "infancia": fallecidos_infancia_ancash_bolognesi,
       "adolescencia": fallecidos_adolescencia_ancash_bolognesi,
       "juventud": fallecidos_juventud_ancash_bolognesi,
       "adultez": fallecidos_adultez_ancash_bolognesi,
       "persona_mayor": fallecidos_persona_mayor_ancash_bolognesi
      }},

          {"name": "Carhuaz", "positivos": positivos_ancash_carhuaz, "poblacion": poblacion_ancash_carhuaz , "hombres_infectados": positivos_hombres_ancash_carhuaz,"mujeres_infectados": positivos_mujeres_ancash_carhuaz, "fallecidos": fallecidos_ancash_carhuaz, "hombres_fallecidos": fallecidos_hombres_ancash_carhuaz,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_carhuaz, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_carhuaz,
       "infancia": fallecidos_infancia_ancash_carhuaz,
       "adolescencia": fallecidos_adolescencia_ancash_carhuaz,
       "juventud": fallecidos_juventud_ancash_carhuaz,
       "adultez": fallecidos_adultez_ancash_carhuaz,
       "persona_mayor": fallecidos_persona_mayor_ancash_carhuaz
      }},

          {"name": "Carlos Fermin Fitzcarrald", "positivos": positivos_ancash_carlos_fermin_fitzcarrald, "poblacion": poblacion_ancash_carlos_fermin_fitzcarrald , "hombres_infectados": positivos_hombres_ancash_carlos_fermin_fitzcarrald,"mujeres_infectados": positivos_mujeres_ancash_carlos_fermin_fitzcarrald, "fallecidos": fallecidos_ancash_carlos_fermin_fitzcarrald, "hombres_fallecidos": fallecidos_hombres_ancash_carlos_fermin_fitzcarrald,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_carlos_fermin_fitzcarrald, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_carlos_fermin_fitzcarrald,
       "infancia": fallecidos_infancia_ancash_carlos_fermin_fitzcarrald,
       "adolescencia": fallecidos_adolescencia_ancash_carlos_fermin_fitzcarrald,
       "juventud": fallecidos_juventud_ancash_carlos_fermin_fitzcarrald,
       "adultez": fallecidos_adultez_ancash_carlos_fermin_fitzcarrald,
       "persona_mayor": fallecidos_persona_mayor_ancash_carlos_fermin_fitzcarrald
      }},

          {"name": "Casma", "positivos": positivos_ancash_casma, "poblacion": poblacion_ancash_casma , "hombres_infectados": positivos_hombres_ancash_casma,"mujeres_infectados": positivos_mujeres_ancash_casma, "fallecidos": fallecidos_ancash_casma, "hombres_fallecidos": fallecidos_hombres_ancash_casma, "mujeres_fallecidos": fallecidos_mujeres_ancash_casma, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_casma,
       "infancia": fallecidos_infancia_ancash_casma,
       "adolescencia": fallecidos_adolescencia_ancash_casma,
       "juventud": fallecidos_juventud_ancash_casma,
       "adultez": fallecidos_adultez_ancash_casma,
       "persona_mayor": fallecidos_persona_mayor_ancash_casma
      }},

          {"name": "Corongo", "positivos": positivos_ancash_corongo, "poblacion": poblacion_ancash_corongo , "hombres_infectados": positivos_hombres_ancash_corongo,"mujeres_infectados": positivos_mujeres_ancash_corongo, "fallecidos": fallecidos_ancash_corongo, "hombres_fallecidos": fallecidos_hombres_ancash_corongo,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_corongo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_corongo,
       "infancia": fallecidos_infancia_ancash_corongo,
       "adolescencia": fallecidos_adolescencia_ancash_corongo,
       "juventud": fallecidos_juventud_ancash_corongo,
       "adultez": fallecidos_adultez_ancash_corongo,
       "persona_mayor": fallecidos_persona_mayor_ancash_corongo
      }},

          {"name": "Huari", "positivos": positivos_ancash_huari, "poblacion": poblacion_ancash_huari , "hombres_infectados": positivos_hombres_ancash_huari,"mujeres_infectados": positivos_mujeres_ancash_huari, "fallecidos": fallecidos_ancash_huari, "hombres_fallecidos": fallecidos_hombres_ancash_huari,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_huari, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_huari,
       "infancia": fallecidos_infancia_ancash_huari,
       "adolescencia": fallecidos_adolescencia_ancash_huari,
       "juventud": fallecidos_juventud_ancash_huari,
       "adultez": fallecidos_adultez_ancash_huari,
       "persona_mayor": fallecidos_persona_mayor_ancash_huari
      }},

          {"name": "Huarmey", "positivos": positivos_ancash_huarmey, "poblacion": poblacion_ancash_huarmey , "hombres_infectados": positivos_hombres_ancash_huarmey,"mujeres_infectados": positivos_mujeres_ancash_huarmey, "fallecidos": fallecidos_ancash_huarmey, "hombres_fallecidos": fallecidos_hombres_ancash_huarmey,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_huarmey, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_huarmey,
       "infancia": fallecidos_infancia_ancash_huarmey,
       "adolescencia": fallecidos_adolescencia_ancash_huarmey,
       "juventud": fallecidos_juventud_ancash_huarmey,
       "adultez": fallecidos_adultez_ancash_huarmey,
       "persona_mayor": fallecidos_persona_mayor_ancash_huarmey
      }},

          {"name": "Huaylas", "positivos": positivos_ancash_huaylas, "poblacion": poblacion_ancash_huaylas , "hombres_infectados": positivos_hombres_ancash_huaylas,"mujeres_infectados": positivos_mujeres_ancash_huaylas, "fallecidos": fallecidos_ancash_huaylas, "hombres_fallecidos": fallecidos_hombres_ancash_huaylas,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_huaylas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_huaylas,
       "infancia": fallecidos_infancia_ancash_huaylas,
       "adolescencia": fallecidos_adolescencia_ancash_huaylas,
       "juventud": fallecidos_juventud_ancash_huaylas,
       "adultez": fallecidos_adultez_ancash_huaylas,
       "persona_mayor": fallecidos_persona_mayor_ancash_huaylas
      }},

          {"name": "Mariscal Luzuriaga", "positivos": positivos_ancash_mariscal_luzuriaga, "poblacion": poblacion_ancash_mariscal_luzuriaga , "hombres_infectados": positivos_hombres_ancash_mariscal_luzuriaga,"mujeres_infectados": positivos_mujeres_ancash_mariscal_luzuriaga, "fallecidos": fallecidos_ancash_mariscal_luzuriaga, "hombres_fallecidos": fallecidos_hombres_ancash_mariscal_luzuriaga,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_mariscal_luzuriaga, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_mariscal_luzuriaga,
       "infancia": fallecidos_infancia_ancash_mariscal_luzuriaga,
       "adolescencia": fallecidos_adolescencia_ancash_mariscal_luzuriaga,
       "juventud": fallecidos_juventud_ancash_mariscal_luzuriaga,
       "adultez": fallecidos_adultez_ancash_mariscal_luzuriaga,
       "persona_mayor": fallecidos_persona_mayor_ancash_mariscal_luzuriaga
      }},

          {"name": "Ocros", "positivos": positivos_ancash_ocros, "poblacion": poblacion_ancash_ocros , "hombres_infectados": positivos_hombres_ancash_ocros,"mujeres_infectados": positivos_mujeres_ancash_ocros, "fallecidos": fallecidos_ancash_ocros, "hombres_fallecidos": fallecidos_hombres_ancash_ocros, "mujeres_fallecidos": fallecidos_mujeres_ancash_ocros, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_ocros,
       "infancia": fallecidos_infancia_ancash_ocros,
       "adolescencia": fallecidos_adolescencia_ancash_ocros,
       "juventud": fallecidos_juventud_ancash_ocros,
       "adultez": fallecidos_adultez_ancash_ocros,
       "persona_mayor": fallecidos_persona_mayor_ancash_ocros
      }},

          {"name": "Pallasca", "positivos": positivos_ancash_pallasca, "poblacion": poblacion_ancash_pallasca , "hombres_infectados": positivos_hombres_ancash_pallasca,"mujeres_infectados": positivos_mujeres_ancash_pallasca, "fallecidos": fallecidos_ancash_pallasca, "hombres_fallecidos": fallecidos_hombres_ancash_pallasca,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_pallasca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_pallasca,
       "infancia": fallecidos_infancia_ancash_pallasca,
       "adolescencia": fallecidos_adolescencia_ancash_pallasca,
       "juventud": fallecidos_juventud_ancash_pallasca,
       "adultez": fallecidos_adultez_ancash_pallasca,
       "persona_mayor": fallecidos_persona_mayor_ancash_pallasca
      }},

          {"name": "Pomabamba", "positivos": positivos_ancash_pomabamba, "poblacion": poblacion_ancash_pomabamba , "hombres_infectados": positivos_hombres_ancash_pomabamba,"mujeres_infectados": positivos_mujeres_ancash_pomabamba, "fallecidos": fallecidos_ancash_pomabamba, "hombres_fallecidos": fallecidos_hombres_ancash_pomabamba,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_pomabamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_pomabamba,
       "infancia": fallecidos_infancia_ancash_pomabamba,
       "adolescencia": fallecidos_adolescencia_ancash_pomabamba,
       "juventud": fallecidos_juventud_ancash_pomabamba,
       "adultez": fallecidos_adultez_ancash_pomabamba,
       "persona_mayor": fallecidos_persona_mayor_ancash_pomabamba
      }},

          {"name": "Recuay", "positivos": positivos_ancash_recuay, "poblacion": poblacion_ancash_recuay , "hombres_infectados": positivos_hombres_ancash_recuay,"mujeres_infectados": positivos_mujeres_ancash_recuay, "fallecidos": fallecidos_ancash_recuay, "hombres_fallecidos": fallecidos_hombres_ancash_recuay, "mujeres_fallecidos": fallecidos_mujeres_ancash_recuay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_recuay,
       "infancia": fallecidos_infancia_ancash_recuay,
       "adolescencia": fallecidos_adolescencia_ancash_recuay,
       "juventud": fallecidos_juventud_ancash_recuay,
       "adultez": fallecidos_adultez_ancash_recuay,
       "persona_mayor": fallecidos_persona_mayor_ancash_recuay
      }},

          {"name": "Santa", "positivos": positivos_ancash_santa, "poblacion": poblacion_ancash_santa , "hombres_infectados": positivos_hombres_ancash_santa,"mujeres_infectados": positivos_mujeres_ancash_santa, "fallecidos": fallecidos_ancash_santa, "hombres_fallecidos": fallecidos_hombres_ancash_santa,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_santa, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_santa,
       "infancia": fallecidos_infancia_ancash_santa,
       "adolescencia": fallecidos_adolescencia_ancash_santa,
       "juventud": fallecidos_juventud_ancash_santa,
       "adultez": fallecidos_adultez_ancash_santa,
       "persona_mayor": fallecidos_persona_mayor_ancash_santa
      }},

          {"name": "Sihuas", "positivos": positivos_ancash_sihuas, "poblacion": poblacion_ancash_sihuas , "hombres_infectados": positivos_hombres_ancash_sihuas,"mujeres_infectados": positivos_mujeres_ancash_sihuas, "fallecidos": fallecidos_ancash_sihuas, "hombres_fallecidos": fallecidos_hombres_ancash_sihuas,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_sihuas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_sihuas,
       "infancia": fallecidos_infancia_ancash_sihuas,
       "adolescencia": fallecidos_adolescencia_ancash_sihuas,
       "juventud": fallecidos_juventud_ancash_sihuas,
       "adultez": fallecidos_adultez_ancash_sihuas,
       "persona_mayor": fallecidos_persona_mayor_ancash_sihuas
      }},

          {"name": "Yungay", "positivos": positivos_ancash_yungay, "poblacion": poblacion_ancash_yungay , "hombres_infectados": positivos_hombres_ancash_yungay,"mujeres_infectados": positivos_mujeres_ancash_yungay, "fallecidos": fallecidos_ancash_yungay, "hombres_fallecidos": fallecidos_hombres_ancash_yungay,
           "mujeres_fallecidos": fallecidos_mujeres_ancash_yungay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_yungay,
       "infancia": fallecidos_infancia_ancash_yungay,
       "adolescencia": fallecidos_adolescencia_ancash_yungay,
       "juventud": fallecidos_juventud_ancash_yungay,
       "adultez": fallecidos_adultez_ancash_yungay,
       "persona_mayor": fallecidos_persona_mayor_ancash_yungay
      }}
      ]
    }
print(json.dumps(ancash))
sys.stdout.flush();
