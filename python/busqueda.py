import pandas as pd
import json
import sys

casos_positivos = pd.read_csv("https://cloud.minsa.gob.pe/s/Y8w3wHsEdYQSZRp/download", sep=";")

casos_fallecidos = pd.read_csv("https://cloud.minsa.gob.pe/s/Md37cjXmjT9qYSa/download", encoding = "ISO-8859-1", sep=";")

#!Datos Departamentos
#!Departamento Loreto
poblacion_loreto = 1041482
positivos_loreto = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "LORETO"].shape)[0]
positivos_hombres_loreto = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LORETO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_loreto = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LORETO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_loreto = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "LORETO"].shape)[0]

#!Departamento Loreto - Etapa de vida
fallecidos_preinfancia_loreto = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_loreto = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_loreto = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_loreto = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_loreto = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_loreto = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Loreto
#!Provincia Maynas
poblacion_loreto_maynas = 549701
positivos_loreto_maynas = list(casos_positivos[casos_positivos['PROVINCIA'] == "MAYNAS"].shape)[0]
positivos_hombres_loreto_maynas = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "MAYNAS")].shape)[0]
positivos_mujeres_loreto_maynas = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "MAYNAS")].shape)[0]
fallecidos_loreto_maynas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MAYNAS"].shape)[0]

#!Provincia Maynas - Etapa de vida
fallecidos_preinfancia_loreto_maynas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MAYNAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_loreto_maynas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MAYNAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_loreto_maynas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MAYNAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_loreto_maynas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MAYNAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_loreto_maynas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MAYNAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_loreto_maynas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MAYNAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Alto Amazonas
poblacion_loreto_alto_amazonas = 125745
positivos_loreto_alto_amazonas = list(casos_positivos[casos_positivos['PROVINCIA'] == "ALTO AMAZONAS"].shape)[0]
positivos_hombres_loreto_alto_amazonas = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "ALTO AMAZONAS")].shape)[0]
positivos_mujeres_loreto_alto_amazonas = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "ALTO AMAZONAS")].shape)[0]
fallecidos_loreto_alto_amazonas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ALTO AMAZONAS"].shape)[0]

#!Provincia Alto Amazonas - Etapa de vida
fallecidos_preinfancia_loreto_alto_amazonas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ALTO AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_loreto_alto_amazonas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ALTO AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_loreto_alto_amazonas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ALTO AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_loreto_alto_amazonas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ALTO AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_loreto_alto_amazonas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ALTO AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_loreto_alto_amazonas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ALTO AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Loreto
poblacion_loreto_loreto = 71164
positivos_loreto_loreto = list(casos_positivos[casos_positivos['PROVINCIA'] == "LORETO"].shape)[0]
positivos_hombres_loreto_loreto = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "LORETO")].shape)[0]
positivos_mujeres_loreto_loreto = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "LORETO")].shape)[0]
fallecidos_loreto_loreto = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LORETO"].shape)[0]

#!Provincia Loreto - Etapa de vida
fallecidos_preinfancia_loreto_loreto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_loreto_loreto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_loreto_loreto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_loreto_loreto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_loreto_loreto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_loreto_loreto = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LORETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Mariscal Castilla
poblacion_loreto_mariscal_ramon_castilla= 72192 
positivos_loreto_mariscal_ramon_castilla = list(casos_positivos[casos_positivos['PROVINCIA'] == "MARISCAL RAMON CASTILLA"].shape)[0]
positivos_hombres_loreto_mariscal_ramon_castilla = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "MARISCAL RAMON CASTILLA")].shape)[0]
positivos_mujeres_loreto_mariscal_ramon_castilla = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "MARISCAL RAMON CASTILLA")].shape)[0]
fallecidos_loreto_mariscal_ramon_castilla = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MARISCAL RAMON CASTILLA"].shape)[0]

#!Provincia Mariscal Castilla - Etapa de vida
fallecidos_preinfancia_loreto_mariscal_ramon_castilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL RAMON CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_loreto_mariscal_ramon_castilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL RAMON CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_loreto_mariscal_ramon_castilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL RAMON CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_loreto_mariscal_ramon_castilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL RAMON CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_loreto_mariscal_ramon_castilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL RAMON CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_loreto_mariscal_ramon_castilla = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL RAMON CASTILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Requena
poblacion_loreto_requena= 72031 
positivos_loreto_requena = list(casos_positivos[casos_positivos['PROVINCIA'] == "REQUENA"].shape)[0]
positivos_hombres_loreto_requena = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "REQUENA")].shape)[0]
positivos_mujeres_loreto_requena = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "REQUENA")].shape)[0]
fallecidos_loreto_requena = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "REQUENA"].shape)[0]

#!Provincia Requena - Etapa de vida
fallecidos_preinfancia_loreto_requena = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "REQUENA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_loreto_requena = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "REQUENA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_loreto_requena = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "REQUENA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_loreto_requena = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "REQUENA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_loreto_requena = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "REQUENA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_loreto_requena = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "REQUENA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Ucayali
poblacion_loreto_ucayali= 71361 
positivos_loreto_ucayali = list(casos_positivos[casos_positivos['PROVINCIA'] == "UCAYALI"].shape)[0]
positivos_hombres_loreto_ucayali = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "UCAYALI")].shape)[0]
positivos_mujeres_loreto_ucayali = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "UCAYALI")].shape)[0]
fallecidos_loreto_ucayali = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "UCAYALI"].shape)[0]

#!Provincia Ucayali - Etapa de vida
fallecidos_preinfancia_loreto_ucayali = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_loreto_ucayali = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_loreto_ucayali = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_loreto_ucayali = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_loreto_ucayali = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_loreto_ucayali = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Datem del Marañón
poblacion_loreto_datem_del_maranon= 67974 
positivos_loreto_datem_del_maranon = list(casos_positivos[casos_positivos['PROVINCIA'] == "DATEM DEL MARAÑON"].shape)[0]
positivos_hombres_loreto_datem_del_maranon = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "DATEM DEL MARAÑON")].shape)[0]
positivos_mujeres_loreto_datem_del_maranon = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "DATEM DEL MARAÑON")].shape)[0]
fallecidos_loreto_datem_del_maranon = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "DATEM DEL MARAÑON"].shape)[0]

#!Provincia Datem del Marañón - Etapa de vida
fallecidos_preinfancia_loreto_datem_del_maranon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DATEM DEL MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_loreto_datem_del_maranon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DATEM DEL MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_loreto_datem_del_maranon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DATEM DEL MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_loreto_datem_del_maranon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DATEM DEL MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_loreto_datem_del_maranon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DATEM DEL MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_loreto_datem_del_maranon = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DATEM DEL MARAÑON") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Putumayo
poblacion_loreto_putumayo= 11314 
positivos_loreto_putumayo = list(casos_positivos[casos_positivos['PROVINCIA'] == "PUTUMAYO"].shape)[0]
positivos_hombres_loreto_putumayo = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PUTUMAYO")].shape)[0]
positivos_mujeres_loreto_putumayo = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PUTUMAYO")].shape)[0]
fallecidos_loreto_putumayo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PUTUMAYO"].shape)[0]

#!Provincia Putumayo - Etapa de vida
fallecidos_preinfancia_loreto_putumayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUTUMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_loreto_putumayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUTUMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_loreto_putumayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUTUMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_loreto_putumayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUTUMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_loreto_putumayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUTUMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_loreto_putumayo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUTUMAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Departamento Amazonas
poblacion_amazonas = 433907
positivos_amazonas = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "AMAZONAS"].shape)[0]
positivos_hombres_amazonas = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AMAZONAS") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_amazonas = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AMAZONAS") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_amazonas = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "AMAZONAS"].shape)[0]

#!Departamento Amazonas - Etapa de vida
fallecidos_preinfancia_amazonas = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_amazonas = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_amazonas = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_amazonas = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_amazonas = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_amazonas = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AMAZONAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Amazonas
#!Provincia Chachapoyas
poblacion_amazonas_chachapoyas = 56307
positivos_amazonas_chachapoyas = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHACHAPOYAS"].shape)[0]
positivos_hombres_amazonas_chachapoyas = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CHACHAPOYAS")].shape)[0]
positivos_mujeres_amazonas_chachapoyas = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CHACHAPOYAS")].shape)[0]
fallecidos_amazonas_chachapoyas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHACHAPOYAS"].shape)[0]

#!Provincia Chachapoyas - Etapa de vida
fallecidos_preinfancia_amazonas_chachapoyas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHACHAPOYAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_amazonas_chachapoyas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHACHAPOYAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_amazonas_chachapoyas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHACHAPOYAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_amazonas_chachapoyas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHACHAPOYAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_amazonas_chachapoyas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHACHAPOYAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_amazonas_chachapoyas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHACHAPOYAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Amazonas-Bagua
poblacion_amazonas_bagua = 81640
positivos_amazonas_bagua = list(casos_positivos[casos_positivos['PROVINCIA'] == "BAGUA"].shape)[0]
positivos_hombres_amazonas_bagua = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "BAGUA")].shape)[0]
positivos_mujeres_amazonas_bagua = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "BAGUA")].shape)[0]
fallecidos_amazonas_bagua = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "BAGUA"].shape)[0]

#!Provincia Bagua - Etapa de vida
fallecidos_preinfancia_amazonas_bagua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BAGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_amazonas_bagua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BAGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_amazonas_bagua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BAGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_amazonas_bagua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BAGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_amazonas_bagua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BAGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_amazonas_bagua = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BAGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Amazonas-Bongara
poblacion_amazonas_bongara = 32935
positivos_amazonas_bongara = list(casos_positivos[casos_positivos['PROVINCIA'] == "BONGARA"].shape)[0]
positivos_hombres_amazonas_bongara = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "BONGARA")].shape)[0]
positivos_mujeres_amazonas_bongara = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "BONGARA")].shape)[0]
fallecidos_amazonas_bongara = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "BONGARA"].shape)[0]

#!Provincia Bongara - Etapa de vida
fallecidos_preinfancia_amazonas_bongara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BONGARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_amazonas_bongara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BONGARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_amazonas_bongara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BONGARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_amazonas_bongara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BONGARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_amazonas_bongara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BONGARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_amazonas_bongara = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BONGARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Amazonas-Condorcanqui
poblacion_amazonas_condorcanqui = 62439
positivos_amazonas_condorcanqui = list(casos_positivos[casos_positivos['PROVINCIA'] == "CONDORCANQUI"].shape)[0]
positivos_hombres_amazonas_condorcanqui = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CONDORCANQUI")].shape)[0]
positivos_mujeres_amazonas_condorcanqui = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CONDORCANQUI")].shape)[0]
fallecidos_amazonas_condorcanqui = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CONDORCANQUI"].shape)[0]

#!Provincia Condorcanqui - Etapa de vida
fallecidos_preinfancia_amazonas_condorcanqui = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONDORCANQUI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_amazonas_condorcanqui = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONDORCANQUI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_amazonas_condorcanqui = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONDORCANQUI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_amazonas_condorcanqui = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONDORCANQUI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_amazonas_condorcanqui = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONDORCANQUI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_amazonas_condorcanqui = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONDORCANQUI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Amazonas-Luya
poblacion_amazonas_luya = 50544
positivos_amazonas_luya = list(casos_positivos[casos_positivos['PROVINCIA'] == "LUYA"].shape)[0]
positivos_hombres_amazonas_luya = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "LUYA")].shape)[0]
positivos_mujeres_amazonas_luya = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "LUYA")].shape)[0]
fallecidos_amazonas_luya = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LUYA"].shape)[0]

#!Provincia Luya - Etapa de vida
fallecidos_preinfancia_amazonas_luya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_amazonas_luya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_amazonas_luya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_amazonas_luya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_amazonas_luya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_amazonas_luya = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Amazonas-Rodriguez de Mendoza
poblacion_amazonas_rodriguez_de_mendoza = 31169
positivos_amazonas_rodriguez_de_mendoza = list(casos_positivos[casos_positivos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA"].shape)[0]
positivos_hombres_amazonas_rodriguez_de_mendoza = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA")].shape)[0]
positivos_mujeres_amazonas_rodriguez_de_mendoza = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA")].shape)[0]
fallecidos_amazonas_rodriguez_de_mendoza = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA"].shape)[0]

#!Provincia Rodriguez de Mendoza - Etapa de vida
fallecidos_preinfancia_amazonas_rodriguez_de_mendoza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_amazonas_rodriguez_de_mendoza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_amazonas_rodriguez_de_mendoza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_amazonas_rodriguez_de_mendoza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_amazonas_rodriguez_de_mendoza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_amazonas_rodriguez_de_mendoza = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Utcubamba
poblacion_amazonas_utcubamba = 118873
positivos_amazonas_utcubamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "UTCUBAMBA"].shape)[0]
positivos_hombres_amazonas_utcubamba = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "UTCUBAMBA")].shape)[0]
positivos_mujeres_amazonas_utcubamba = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "UTCUBAMBA")].shape)[0]
fallecidos_amazonas_utcubamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "UTCUBAMBA"].shape)[0]

#!Provincia Utcubamba - Etapa de vida
fallecidos_preinfancia_amazonas_utcubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UTCUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_amazonas_utcubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UTCUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_amazonas_utcubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UTCUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_amazonas_utcubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UTCUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_amazonas_utcubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UTCUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_amazonas_utcubamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UTCUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Departamento Tumbes
poblacion_tumbes = 256423
positivos_tumbes = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "TUMBES"].shape)[0]
positivos_hombres_tumbes = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "TUMBES") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tumbes = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "TUMBES") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tumbes = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "TUMBES"].shape)[0]

#!Departamento Tumbes - Etapa de vida
fallecidos_preinfancia_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tumbes = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tumbes = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Tumbes
#!Tumbes-Tumbes
poblacion_tumbes_tumbes = 177707
positivos_tumbes_tumbes = list(casos_positivos[casos_positivos['PROVINCIA'] == "TUMBES"].shape)[0]
positivos_hombres_tumbes_tumbes = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "TUMBES")].shape)[0]
positivos_mujeres_tumbes_tumbes = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "TUMBES")].shape)[0]
fallecidos_tumbes_tumbes = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TUMBES"].shape)[0]

#!Provincia Tumbes - Etapa de vida
fallecidos_preinfancia_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tumbes_tumbes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tumbes_tumbes = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TUMBES") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Tumbes-Contralmirante Villar
poblacion_tumbes_contralmirante_villar = 21684
positivos_tumbes_contralmirante_villar = list(casos_positivos[casos_positivos['PROVINCIA'] == "CONTRALMIRANTE VILLAR"].shape)[0]
positivos_hombres_tumbes_contralmirante_villar = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CONTRALMIRANTE VILLAR")].shape)[0]
positivos_mujeres_tumbes_contralmirante_villar = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CONTRALMIRANTE VILLAR")].shape)[0]
fallecidos_tumbes_contralmirante_villar = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR"].shape)[0]

#!Provincia Contralmirante Villar - Etapa de vida
fallecidos_preinfancia_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tumbes_contralmirante_villar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tumbes_contralmirante_villar = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONTRALMIRANTE VILLAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Provincia Zarumilla
poblacion_tumbes_zarumilla = 57032
positivos_tumbes_zarumilla = list(casos_positivos[casos_positivos['PROVINCIA'] == "ZARUMILLA"].shape)[0]
positivos_hombres_tumbes_zarumilla = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "ZARUMILLA")].shape)[0]
positivos_mujeres_tumbes_zarumilla = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "ZARUMILLA")].shape)[0]
fallecidos_tumbes_zarumilla = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ZARUMILLA"].shape)[0]

#!Provincia Contralmirante Villar - Etapa de vida
fallecidos_preinfancia_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tumbes_zarumilla = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tumbes_zarumilla = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ZARUMILLA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Departamento Piura
poblacion_piura = 2085441
positivos_piura = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "PIURA"].shape)[0]
positivos_hombres_piura = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PIURA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_piura = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PIURA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_piura = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "PIURA"].shape)[0]

#!Departamento Piura - Etapa de vida
fallecidos_preinfancia_piura = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Piura
#!Piura-Piura
poblacion_piura_piura = 870137
positivos_piura_piura = list(casos_positivos[casos_positivos['PROVINCIA'] == "PIURA"].shape)[0]
positivos_hombres_piura_piura = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PIURA")].shape)[0]
positivos_mujeres_piura_piura = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PIURA")].shape)[0]
fallecidos_piura_piura = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PIURA"].shape)[0]


#!Provincia Piura - Etapa de vida
fallecidos_preinfancia_piura_piura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_piura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_piura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_piura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_piura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_piura = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PIURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Piura-Ayabaca
poblacion_piura_ayabaca = 154083
positivos_piura_ayabaca = list(casos_positivos[casos_positivos['PROVINCIA'] == "AYABACA"].shape)[0]
positivos_hombres_piura_ayabaca = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "AYABACA")].shape)[0]
positivos_mujeres_piura_ayabaca = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "AYABACA")].shape)[0]
fallecidos_piura_ayabaca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "AYABACA"].shape)[0]

#!Provincia Ayabaca - Etapa de vida
fallecidos_preinfancia_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_ayabaca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_ayabaca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYABACA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Piura-Huancambamba
poblacion_piura_huancabamba = 140066
positivos_piura_huancabamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUANCABAMBA"].shape)[0]
positivos_hombres_piura_huancabamba = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "HUANCABAMBA")].shape)[0]
positivos_mujeres_piura_huancabamba = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "HUANCABAMBA")].shape)[0]
fallecidos_piura_huancabamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUANCABAMBA"].shape)[0]

#!Provincia Huancambamba - Etapa de vida
fallecidos_preinfancia_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_huancabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_huancabamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Piura-Morropon
poblacion_piura_morropon = 178381
positivos_piura_morropon = list(casos_positivos[casos_positivos['PROVINCIA'] == "MORROPON"].shape)[0]
positivos_hombres_piura_morropon = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "MORROPON")].shape)[0]
positivos_mujeres_piura_morropon = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "MORROPON")].shape)[0]
fallecidos_piura_morropon = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MORROPON"].shape)[0]

#!Provincia Morropon - Etapa de vida
fallecidos_preinfancia_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_morropon = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_morropon = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MORROPON") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Piura-Paita
poblacion_piura_paita = 145085
positivos_piura_paita = list(casos_positivos[casos_positivos['PROVINCIA'] == "PAITA"].shape)[0]
positivos_hombres_piura_paita = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "PAITA")].shape)[0]
positivos_mujeres_piura_paita = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "PAITA")].shape)[0]
fallecidos_piura_paita = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PAITA"].shape)[0]

#!Provincia Morropon - Etapa de vida
fallecidos_preinfancia_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_paita = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_paita = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAITA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Piura-Sullana
poblacion_piura_sullana = 358893
positivos_piura_sullana = list(casos_positivos[casos_positivos['PROVINCIA'] == "SULLANA"].shape)[0]
positivos_hombres_piura_sullana = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SULLANA")].shape)[0]
positivos_mujeres_piura_sullana = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SULLANA")].shape)[0]
fallecidos_piura_sullana = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SULLANA"].shape)[0]

#!Provincia Sullana - Etapa de vida
fallecidos_preinfancia_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_sullana = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_sullana = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SULLANA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Piura-Talara
poblacion_piura_talara = 153209
positivos_piura_talara = list(casos_positivos[casos_positivos['PROVINCIA'] == "TALARA"].shape)[0]
positivos_hombres_piura_talara = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "TALARA")].shape)[0]
positivos_mujeres_piura_talara = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "TALARA")].shape)[0]
fallecidos_piura_talara = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TALARA"].shape)[0]

#!Provincia Talara - Etapa de vida
fallecidos_preinfancia_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_talara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_talara = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TALARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Sechura
poblacion_piura_sechura = 85587
positivos_piura_sechura = list(casos_positivos[casos_positivos['PROVINCIA'] == "SECHURA"].shape)[0]
positivos_hombres_piura_sechura = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "SECHURA")].shape)[0]
positivos_mujeres_piura_sechura = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "SECHURA")].shape)[0]
fallecidos_piura_sechura = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SECHURA"].shape)[0]

#!Provincia Sechura - Etapa de vida
fallecidos_preinfancia_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_piura_sechura = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_piura_sechura = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SECHURA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Departamento Lambayeque
poblacion_lambayeque = 1327433
positivos_lambayeque = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "LAMBAYEQUE"].shape)[0]
positivos_hombres_lambayeque = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LAMBAYEQUE") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lambayeque = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LAMBAYEQUE") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lambayeque = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE"].shape)[0]

#!Departamento Lambayeque - Etapa de vida
fallecidos_preinfancia_lambayeque = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lambayeque = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lambayeque = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lambayeque = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lambayeque = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lambayeque = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Lambayeque
#!Lambayeque-Chiclayo
poblacion_lambayeque_chiclayo = 902375
positivos_lambayeque_chiclayo = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHICLAYO"].shape)[0]
positivos_hombres_lambayeque_chiclayo = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "CHICLAYO")].shape)[0]
positivos_mujeres_lambayeque_chiclayo = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "CHICLAYO")].shape)[0]
fallecidos_lambayeque_chiclayo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHICLAYO"].shape)[0]

#!Provincia Chiclayo - Etapa de vida
fallecidos_preinfancia_lambayeque_chiclayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lambayeque_chiclayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lambayeque_chiclayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lambayeque_chiclayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lambayeque_chiclayo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lambayeque_chiclayo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHICLAYO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Lambayeque-Ferreñafe
poblacion_lambayeque_ferrenafe = 110750
positivos_lambayeque_ferrenafe = list(casos_positivos[casos_positivos['PROVINCIA'] == "FERREÑAFE"].shape)[0]
positivos_hombres_lambayeque_ferrenafe = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "FERREÑAFE")].shape)[0]
positivos_mujeres_lambayeque_ferrenafe = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "FERREÑAFE")].shape)[0]
fallecidos_lambayeque_ferrenafe = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "FERREÑAFE"].shape)[0]

#!Provincia Ferreñafe - Etapa de vida
fallecidos_preinfancia_lambayeque_ferrenafe = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lambayeque_ferrenafe = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lambayeque_ferrenafe = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lambayeque_ferrenafe = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lambayeque_ferrenafe = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lambayeque_ferrenafe = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "FERREÑAFE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Lambayeque-Lambayeque
poblacion_lambayeque_lambayeque = 314308
positivos_lambayeque_lambayeque = list(casos_positivos[casos_positivos['PROVINCIA'] == "LAMBAYEQUE"].shape)[0]
positivos_hombres_lambayeque_lambayeque = list(casos_positivos[(casos_positivos['SEXO'] == "MASCULINO") & (casos_positivos['PROVINCIA'] == "LAMBAYEQUE")].shape)[0]
positivos_mujeres_lambayeque_lambayeque = list(casos_positivos[(casos_positivos['SEXO'] == "FEMENINO") & (casos_positivos['PROVINCIA'] == "LAMBAYEQUE")].shape)[0]
fallecidos_lambayeque_lambayeque = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE"].shape)[0]

#!Provincia Lambayeque - Etapa de vida
fallecidos_preinfancia_lambayeque_lambayeque = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_lambayeque_lambayeque = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_lambayeque_lambayeque = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_lambayeque_lambayeque = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_lambayeque_lambayeque = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_lambayeque_lambayeque = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LAMBAYEQUE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Departamento Cajamarca
poblacion_cajamarca = 1446823
positivos_cajamarca = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "CAJAMARCA"].shape)[0]
positivos_hombres_cajamarca = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CAJAMARCA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cajamarca = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CAJAMARCA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cajamarca = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "CAJAMARCA"].shape)[0]

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
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SANTA CRUZ") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Departamento Libertad
poblacion_libertad = 2031503
positivos_libertad = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "LA LIBERTAD"].shape)[0]
positivos_hombres_libertad = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LA LIBERTAD") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_libertad = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LA LIBERTAD") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_libertad = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "LA LIBERTAD"].shape)[0]

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

#!Departamento Ancash
poblacion_ancash = 1175871
positivos_ancash = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "ANCASH"].shape)[0]
positivos_hombres_ancash = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "ANCASH") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ancash = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "ANCASH") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ancash = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "ANCASH"].shape)[0]

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



#!Departamento San Martin
poblacion_sanmartin = 906777
positivos_sanmartin = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "SAN MARTIN"].shape)[0]
positivos_hombres_sanmartin = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "SAN MARTIN") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_sanmartin = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "SAN MARTIN") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_sanmartin = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "SAN MARTIN"].shape)[0]

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


#!Departamento Huanuco
poblacion_huanuco = 756847
positivos_huanuco = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "HUANUCO"].shape)[0]
positivos_hombres_huanuco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "HUANUCO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huanuco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "HUANUCO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huanuco = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "HUANUCO"].shape)[0]

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



#!Departamento Ucayali
poblacion_ucayali = 606081
positivos_ucayali = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "UCAYALI"].shape)[0]
positivos_hombres_ucayali = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "UCAYALI") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ucayali = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "UCAYALI") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ucayali = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "UCAYALI"].shape)[0]

#!Departamento Ucayali - Etapa de vida
fallecidos_preinfancia_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ucayali = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ucayali = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "UCAYALI") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Ucayali
#!Ucayali-Coronel Portillo
poblacion_ucayali_coronel_portillo = 460293
positivos_ucayali_coronel_portillo = list(casos_positivos[casos_positivos['PROVINCIA'] == "CORONEL PORTILLO"].shape)[0]
positivos_hombres_ucayali_coronel_portillo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ucayali_coronel_portillo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ucayali_coronel_portillo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO"].shape)[0]

#!Provincia Coronel Portillo - Etapa de vida
fallecidos_preinfancia_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ucayali_coronel_portillo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ucayali_coronel_portillo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CORONEL PORTILLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Atalaya
poblacion_ucayali_atalaya = 66950
positivos_ucayali_atalaya = list(casos_positivos[casos_positivos['PROVINCIA'] == "ATALAYA"].shape)[0]
positivos_hombres_ucayali_atalaya = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ATALAYA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ucayali_atalaya = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ATALAYA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ucayali_atalaya = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ATALAYA"].shape)[0]

#!Provincia Coronel Portillo - Etapa de vida
fallecidos_preinfancia_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ucayali_atalaya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ucayali_atalaya = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ATALAYA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Padre Abad
poblacion_ucayali_padre_abad = 73662
positivos_ucayali_padre_abad = list(casos_positivos[casos_positivos['PROVINCIA'] == "PADRE ABAD"].shape)[0]
positivos_hombres_ucayali_padre_abad = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PADRE ABAD") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ucayali_padre_abad = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PADRE ABAD") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ucayali_padre_abad = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PADRE ABAD"].shape)[0]

#!Provincia Padre Abad - Etapa de vida
fallecidos_preinfancia_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ucayali_padre_abad = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ucayali_padre_abad = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PADRE ABAD") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Purus
poblacion_ucayali_purus = 5176
positivos_ucayali_purus = list(casos_positivos[casos_positivos['PROVINCIA'] == "PURUS"].shape)[0]
positivos_hombres_ucayali_purus = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PURUS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ucayali_purus = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PURUS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ucayali_purus = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PURUS"].shape)[0]

#!Provincia Purus - Etapa de vida
fallecidos_preinfancia_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ucayali_purus = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ucayali_purus = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PURUS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Departamento Pasco
poblacion_pasco = 270575
positivos_pasco = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "PASCO"].shape)[0]
positivos_hombres_pasco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PASCO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_pasco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PASCO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_pasco = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "PASCO"].shape)[0]

#!Departamento Pasco - Etapa de vida
fallecidos_preinfancia_pasco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_pasco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_pasco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_pasco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_pasco = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_pasco = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias
#!Provincia Pasco
poblacion_pasco_pasco = 138810
positivos_pasco_pasco = list(casos_positivos[casos_positivos['PROVINCIA'] == "PASCO"].shape)[0]
positivos_hombres_pasco_pasco = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PASCO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_pasco_pasco = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PASCO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_pasco_pasco = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PASCO"].shape)[0]

#!Provincia Pasco - Etapa de vida
fallecidos_preinfancia_pasco_pasco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_pasco_pasco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_pasco_pasco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_pasco_pasco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_pasco_pasco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_pasco_pasco = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PASCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincia Daniel Alcides Carrion
poblacion_pasco_daniel_alcide_carrion = 46771
positivos_pasco_daniel_alcide_carrion = list(casos_positivos[casos_positivos['PROVINCIA'] == "DANIEL ALCIDES CARRION"].shape)[0]
positivos_hombres_pasco_daniel_alcide_carrion = list(casos_positivos[(casos_positivos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_pasco_daniel_alcide_carrion = list(casos_positivos[(casos_positivos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_pasco_daniel_alcide_carrion = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION"].shape)[0]

#!Provincia Daniel Alcides Carrion - Etapa de vida
fallecidos_preinfancia_pasco_daniel_alcide_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_pasco_daniel_alcide_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_pasco_daniel_alcide_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_pasco_daniel_alcide_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_pasco_daniel_alcide_carrion = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_pasco_daniel_alcide_carrion = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DANIEL ALCIDES CARRION") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia de Oxapampa
poblacion_pasco_oxapampa = 84994
positivos_pasco_oxapampa = list(casos_positivos[casos_positivos['PROVINCIA'] == "OXAPAMPA"].shape)[0]
positivos_hombres_pasco_oxapampa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "OXAPAMPA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_pasco_oxapampa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "OXAPAMPA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_pasco_oxapampa = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "OXAPAMPA"].shape)[0]

#!Provincia Oxapampa - Etapa de vida
fallecidos_preinfancia_pasco_oxapampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_pasco_oxapampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_pasco_oxapampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_pasco_oxapampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_pasco_oxapampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_pasco_oxapampa = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "OXAPAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Departamento Lima
poblacion_lima = 10907764
positivos_lima = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LIMA") | (casos_positivos['DEPARTAMENTO'] == "LIMA REGION")].shape)[0]
positivos_hombres_lima = list(casos_positivos[((casos_positivos['DEPARTAMENTO'] == "LIMA") | (casos_positivos['DEPARTAMENTO'] == "LIMA REGION")) & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_lima = list(casos_positivos[((casos_positivos['DEPARTAMENTO'] == "LIMA") | (casos_positivos['DEPARTAMENTO'] == "LIMA REGION")) & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_lima = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LIMA") | (casos_fallecidos['DEPARTAMENTO'] == "LIMA REGION")].shape)[0]

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


#!Departamento Junin
poblacion_junin = 1357263
positivos_junin = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "JUNIN"].shape)[0]
positivos_hombres_junin = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "JUNIN") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "JUNIN") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "JUNIN"].shape)[0]

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

#!Provincia Satipo - Etapa de vida
fallecidos_preinfancia_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_junin_satipo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_junin_satipo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SATIPO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincia Tarma
poblacion_junin_tarma = 109330
positivos_junin_tarma = list(casos_positivos[casos_positivos['PROVINCIA'] == "TARMA"].shape)[0]
positivos_hombres_junin_tarma = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TARMA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_junin_tarma = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TARMA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_junin_tarma = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TARMA"].shape)[0]

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




#!Departamento Huancavelica
poblacion_huancavelica = 353645
positivos_huancavelica = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "HUANCAVELICA"].shape)[0]
positivos_hombres_huancavelica = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA"].shape)[0]

#!Departamento Huancavelica - Etapa de vida
fallecidos_preinfancia_huancavelica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincias Huancavelica
#!Huancavelica-Huancavelica
poblacion_huancavelica_huancavelica = 113706
positivos_huancavelica_huancavelica = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUANCAVELICA"].shape)[0]
positivos_hombres_huancavelica_huancavelica = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANCAVELICA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_huancavelica = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANCAVELICA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_huancavelica = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUANCAVELICA"].shape)[0]

#!Provincia Huancavelica - Etapa de vida
fallecidos_preinfancia_huancavelica_huancavelica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_huancavelica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_huancavelica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_huancavelica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_huancavelica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_huancavelica = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCAVELICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huancavelica-Acobamba
poblacion_huancavelica_acobamba = 54275
positivos_huancavelica_acobamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "ACOBAMBA"].shape)[0]
positivos_hombres_huancavelica_acobamba = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ACOBAMBA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_acobamba = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ACOBAMBA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_acobamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ACOBAMBA"].shape)[0]

#!Provincia Acobamba - Etapa de vida
fallecidos_preinfancia_huancavelica_acobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_acobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_acobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_acobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_acobamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_acobamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ACOBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huancavelica-Angaraes
poblacion_huancavelica_angaraes = 45385
positivos_huancavelica_angaraes = list(casos_positivos[casos_positivos['PROVINCIA'] == "ANGARAES"].shape)[0]
positivos_hombres_huancavelica_angaraes = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ANGARAES") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_angaraes = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ANGARAES") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_angaraes = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ANGARAES"].shape)[0]

#!Provincia Angaraes - Etapa de vida
fallecidos_preinfancia_huancavelica_angaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_angaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_angaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_angaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_angaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_angaraes = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANGARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huancavelica-Castrovirreyna
poblacion_huancavelica_castrovirreyna = 14030
positivos_huancavelica_castrovirreyna = list(casos_positivos[casos_positivos['PROVINCIA'] == "CASTROVIRREYNA"].shape)[0]
positivos_hombres_huancavelica_castrovirreyna = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_castrovirreyna = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_castrovirreyna = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA"].shape)[0]

#!Provincia Castrovirreyna - Etapa de vida
fallecidos_preinfancia_huancavelica_castrovirreyna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_castrovirreyna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_castrovirreyna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_castrovirreyna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_castrovirreyna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_castrovirreyna = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CASTROVIRREYNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huancavelica-Churcampa
poblacion_huancavelica_churcampa = 31887
positivos_huancavelica_churcampa = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHURCAMPA"].shape)[0]
positivos_hombres_huancavelica_churcampa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHURCAMPA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_churcampa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHURCAMPA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_churcampa = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHURCAMPA"].shape)[0]

#!Provincia Churcampa - Etapa de vida
fallecidos_preinfancia_huancavelica_churcampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_churcampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_churcampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_churcampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_churcampa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_churcampa = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHURCAMPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Huancavelica-Huaytara
poblacion_huancavelica_huaytara = 17016
positivos_huancavelica_huaytara = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUAYTARA"].shape)[0]
positivos_hombres_huancavelica_huaytara = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUAYTARA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_huaytara = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUAYTARA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_huaytara = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUAYTARA"].shape)[0]

#!Provincia Huaytara - Etapa de vida
fallecidos_preinfancia_huancavelica_huaytara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_huaytara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_huaytara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_huaytara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_huaytara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_huaytara = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAYTARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Huancavelica-Tayacaja
poblacion_huancavelica_tayacaja = 77346
positivos_huancavelica_tayacaja = list(casos_positivos[casos_positivos['PROVINCIA'] == "TAYACAJA"].shape)[0]
positivos_hombres_huancavelica_tayacaja = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAYACAJA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_huancavelica_tayacaja = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAYACAJA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_huancavelica_tayacaja = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TAYACAJA"].shape)[0]

#!Provincia Tayacaja - Etapa de vida
fallecidos_preinfancia_huancavelica_tayacaja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_huancavelica_tayacaja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_huancavelica_tayacaja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_huancavelica_tayacaja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_huancavelica_tayacaja = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_huancavelica_tayacaja = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAYACAJA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Departamento Ica
poblacion_ica = 983511
positivos_ica = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "ICA"].shape)[0]
positivos_hombres_ica = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "ICA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "ICA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "ICA"].shape)[0]

#!Departamento Ica - Etapa de vida
fallecidos_preinfancia_ica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincias Ica
#!Ica-Ica
poblacion_ica_ica = 451473
positivos_ica_ica = list(casos_positivos[casos_positivos['PROVINCIA'] == "ICA"].shape)[0]
positivos_hombres_ica_ica = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ICA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica_ica = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ICA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica_ica = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ICA"].shape)[0]

#!Provincia ICA - Etapa de vida
fallecidos_preinfancia_ica_ica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica_ica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica_ica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica_ica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica_ica = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica_ica = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ICA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ica-Chincha
poblacion_ica_chincha = 271793
positivos_ica_chincha = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHINCHA"].shape)[0]
positivos_hombres_ica_chincha = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHINCHA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica_chincha = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHINCHA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica_chincha = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHINCHA"].shape)[0]

#!Provincia Chincha - Etapa de vida
fallecidos_preinfancia_ica_chincha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica_chincha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica_chincha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica_chincha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica_chincha = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica_chincha = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ica-Nazca
poblacion_ica_nazca = 74828
positivos_ica_nazca = list(casos_positivos[casos_positivos['PROVINCIA'] == "NAZCA"].shape)[0]
positivos_hombres_ica_nazca = list(casos_positivos[(casos_positivos['PROVINCIA'] == "NAZCA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica_nazca = list(casos_positivos[(casos_positivos['PROVINCIA'] == "NAZCA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica_nazca = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "NAZCA"].shape)[0]

#!Provincia Nazca - Etapa de vida
fallecidos_preinfancia_ica_nazca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica_nazca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica_nazca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica_nazca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica_nazca = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica_nazca = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "NAZCA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ica-Palpa
poblacion_ica_palpa = 15331
positivos_ica_palpa = list(casos_positivos[casos_positivos['PROVINCIA'] == "PALPA"].shape)[0]
positivos_hombres_ica_palpa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PALPA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica_palpa = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PALPA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica_palpa = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PALPA"].shape)[0]

#!Provincia Palpa - Etapa de vida
fallecidos_preinfancia_ica_palpa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica_palpa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica_palpa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica_palpa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica_palpa = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica_palpa = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PALPA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ica-Pisco
poblacion_ica_pisco = 170086
positivos_ica_pisco = list(casos_positivos[casos_positivos['PROVINCIA'] == "PISCO"].shape)[0]
positivos_hombres_ica_pisco = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PISCO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ica_pisco = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PISCO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ica_pisco = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PISCO"].shape)[0]

#!Provincia Pisco - Etapa de vida
fallecidos_preinfancia_ica_pisco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ica_pisco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ica_pisco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ica_pisco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ica_pisco = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ica_pisco = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PISCO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Departamento Ayacucho
poblacion_ayacucho = 658300
positivos_ayacucho = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "AYACUCHO"].shape)[0]
positivos_hombres_ayacucho = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AYACUCHO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AYACUCHO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "AYACUCHO"].shape)[0]

#!Departamento Ayacucho - Etapa de vida
fallecidos_preinfancia_ayacucho = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AYACUCHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AYACUCHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AYACUCHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AYACUCHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AYACUCHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AYACUCHO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Provincias Ayacucho
#!Ayacucho-Huamanga
poblacion_ayacucho_huamanga = 271447
positivos_ayacucho_huamanga = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUAMANGA"].shape)[0]
positivos_hombres_ayacucho_huamanga = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUAMANGA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_huamanga = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUAMANGA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_huamanga = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUAMANGA"].shape)[0]

#!Provincia Huamanga - Etapa de vida
fallecidos_preinfancia_ayacucho_huamanga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMANGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_huamanga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMANGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_huamanga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMANGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_huamanga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMANGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_huamanga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMANGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_huamanga = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMANGA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ayacucho-Cangallo
poblacion_ayacucho_cangallo = 31890
positivos_ayacucho_cangallo = list(casos_positivos[casos_positivos['PROVINCIA'] == "CANGALLO"].shape)[0]
positivos_hombres_ayacucho_cangallo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANGALLO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_cangallo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANGALLO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_cangallo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CANGALLO"].shape)[0]

#!Provincia Cangallo - Etapa de vida
fallecidos_preinfancia_ayacucho_cangallo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANGALLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_cangallo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANGALLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_cangallo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANGALLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_cangallo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANGALLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_cangallo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANGALLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_cangallo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANGALLO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ayacucho-Huanca Sancos
poblacion_ayacucho_huanca_sancos = 9634
positivos_ayacucho_huanca_sancos = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUANCA SANCOS"].shape)[0]
positivos_hombres_ayacucho_huanca_sancos = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANCA SANCOS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_huanca_sancos = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANCA SANCOS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_huanca_sancos = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUANCA SANCOS"].shape)[0]

#!Provincia Huanca Sancos - Etapa de vida
fallecidos_preinfancia_ayacucho_huanca_sancos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCA SANCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_huanca_sancos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCA SANCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_huanca_sancos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCA SANCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_huanca_sancos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCA SANCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_huanca_sancos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCA SANCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_huanca_sancos = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCA SANCOS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ayacucho-Huanta
poblacion_ayacucho_huanta = 102208
positivos_ayacucho_huanta = list(casos_positivos[casos_positivos['PROVINCIA'] == "HUANTA"].shape)[0]
positivos_hombres_ayacucho_huanta = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANTA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_huanta = list(casos_positivos[(casos_positivos['PROVINCIA'] == "HUANTA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_huanta = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "HUANTA"].shape)[0]

#!Provincia Huanta - Etapa de vida
fallecidos_preinfancia_ayacucho_huanta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_huanta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_huanta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_huanta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_huanta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_huanta = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANTA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Ayacucho-Mar
poblacion_ayacucho_mar = 82593
positivos_ayacucho_mar = list(casos_positivos[casos_positivos['PROVINCIA'] == "LA MAR"].shape)[0]
positivos_hombres_ayacucho_mar = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LA MAR") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_mar = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LA MAR") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_mar = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LA MAR"].shape)[0]

#!Provincia Mar - Etapa de vida
fallecidos_preinfancia_ayacucho_mar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA MAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_mar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA MAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_mar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA MAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_mar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA MAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_mar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA MAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_mar = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA MAR") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Ayacucho-Lucanas
poblacion_ayacucho_lucanas = 63948
positivos_ayacucho_lucanas = list(casos_positivos[casos_positivos['PROVINCIA'] == "LUCANAS"].shape)[0]
positivos_hombres_ayacucho_lucanas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LUCANAS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_lucanas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "LUCANAS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_lucanas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "LUCANAS"].shape)[0]

#!Provincia Lucanas - Etapa de vida
fallecidos_preinfancia_ayacucho_lucanas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUCANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_lucanas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUCANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_lucanas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUCANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_lucanas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUCANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_lucanas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUCANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_lucanas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUCANAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ayacucho-Parinacochas
poblacion_ayacucho_parinacochas = 31282
positivos_ayacucho_parinacochas = list(casos_positivos[casos_positivos['PROVINCIA'] == "PARINACOCHAS"].shape)[0]
positivos_hombres_ayacucho_parinacochas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PARINACOCHAS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_parinacochas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PARINACOCHAS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_parinacochas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PARINACOCHAS"].shape)[0]

#!Provincia Parinacochas - Etapa de vida
fallecidos_preinfancia_ayacucho_parinacochas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARINACOCHAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_parinacochas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARINACOCHAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_parinacochas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARINACOCHAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_parinacochas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARINACOCHAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_parinacochas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARINACOCHAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_parinacochas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARINACOCHAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ayacucho-Paucar
poblacion_ayacucho_paucar = 10463
positivos_ayacucho_paucar = list(casos_positivos[casos_positivos['PROVINCIA'] == "PAUCAR DEL SARA SARA"].shape)[0]
positivos_hombres_ayacucho_paucar = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PAUCAR DEL SARA SARA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_paucar = list(casos_positivos[(casos_positivos['PROVINCIA'] == "PAUCAR DEL SARA SARA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_paucar = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "PAUCAR DEL SARA SARA"].shape)[0]

#!Provincia Paucar - Etapa de vida
fallecidos_preinfancia_ayacucho_paucar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCAR DEL SARA SARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_paucar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCAR DEL SARA SARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_paucar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCAR DEL SARA SARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_paucar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCAR DEL SARA SARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_paucar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCAR DEL SARA SARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_paucar = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCAR DEL SARA SARA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ayacucho-Sucre
poblacion_ayacucho_sucre = 11149
positivos_ayacucho_sucre = list(casos_positivos[casos_positivos['PROVINCIA'] == "SUCRE"].shape)[0]
positivos_hombres_ayacucho_sucre = list(casos_positivos[(casos_positivos['PROVINCIA'] == "SUCRE") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_sucre = list(casos_positivos[(casos_positivos['PROVINCIA'] == "SUCRE") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_sucre = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "SUCRE"].shape)[0]

#!Provincia Paucar - Etapa de vida
fallecidos_preinfancia_ayacucho_sucre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SUCRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_sucre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SUCRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_sucre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SUCRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_sucre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SUCRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_sucre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SUCRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_sucre = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SUCRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Ayacucho-Victor Fajardo
poblacion_ayacucho_victor_fajardo = 22024
positivos_ayacucho_victor_fajardo = list(casos_positivos[casos_positivos['PROVINCIA'] == "VICTOR FAJARDO"].shape)[0]  
positivos_hombres_ayacucho_victor_fajardo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "VICTOR FAJARDO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_victor_fajardo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "VICTOR FAJARDO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_victor_fajardo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "VICTOR FAJARDO"].shape)[0]

#!Provincia Victor Fajardo - Etapa de vida
fallecidos_preinfancia_ayacucho_victor_fajardo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VICTOR FAJARDO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_victor_fajardo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VICTOR FAJARDO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_victor_fajardo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VICTOR FAJARDO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_victor_fajardo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VICTOR FAJARDO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_victor_fajardo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VICTOR FAJARDO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_victor_fajardo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VICTOR FAJARDO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Ayacucho-Vilcas Huaman
poblacion_ayacucho_vilcas_huaman = 21662
positivos_ayacucho_vilcas_huaman = list(casos_positivos[casos_positivos['PROVINCIA'] == "VILCAS HUAMAN"].shape)[0]
positivos_hombres_ayacucho_vilcas_huaman = list(casos_positivos[(casos_positivos['PROVINCIA'] == "VILCAS HUAMAN") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho_vilcas_huaman = list(casos_positivos[(casos_positivos['PROVINCIA'] == "VILCAS HUAMAN") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho_vilcas_huaman = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "VILCAS HUAMAN"].shape)[0]

#!Provincia Vilcas Huaman - Etapa de vida
fallecidos_preinfancia_ayacucho_vilcas_huaman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VILCAS HUAMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_ayacucho_vilcas_huaman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VILCAS HUAMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_ayacucho_vilcas_huaman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VILCAS HUAMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_ayacucho_vilcas_huaman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VILCAS HUAMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_ayacucho_vilcas_huaman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VILCAS HUAMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_ayacucho_vilcas_huaman = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VILCAS HUAMAN") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Departamento Apurimac
poblacion_apurimac = 424272
positivos_apurimac = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "APURIMAC"].shape)[0]
positivos_hombres_apurimac = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "APURIMAC") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_apurimac = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "APURIMAC") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_apurimac = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "APURIMAC"].shape)[0]

#!Departamento Apurimac - Etapa de vida
fallecidos_preinfancia_apurimac = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "APURIMAC") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_apurimac = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "APURIMAC") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_apurimac = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "APURIMAC") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_apurimac = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "APURIMAC") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_apurimac = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "APURIMAC") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_apurimac = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "APURIMAC") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias de Apurimac
#!Apurimac-Abancay
poblacion_apurimac_abancay = 102090
positivos_apurimac_abancay = list(casos_positivos[casos_positivos['PROVINCIA'] == "ABANCAY"].shape)[0]
positivos_hombres_apurimac_abancay = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ABANCAY") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_apurimac_abancay = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ABANCAY") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_apurimac_abancay = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ABANCAY"].shape)[0]

#!Provincia Abancay - Etapa de vida
fallecidos_preinfancia_apurimac_abancay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ABANCAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_apurimac_abancay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ABANCAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_apurimac_abancay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ABANCAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_apurimac_abancay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ABANCAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_apurimac_abancay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ABANCAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_apurimac_abancay = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ABANCAY") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Apurimac-Andahuaylas
poblacion_apurimac_andahuaylas = 155016
positivos_apurimac_andahuaylas = list(casos_positivos[casos_positivos['PROVINCIA'] == "ANDAHUAYLAS"].shape)[0]
positivos_hombres_apurimac_andahuaylas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ANDAHUAYLAS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_apurimac_andahuaylas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ANDAHUAYLAS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_apurimac_andahuaylas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ANDAHUAYLAS"].shape)[0]

#!Provincia Andahuaylas - Etapa de vida
fallecidos_preinfancia_apurimac_andahuaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANDAHUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_apurimac_andahuaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANDAHUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_apurimac_andahuaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANDAHUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_apurimac_andahuaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANDAHUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_apurimac_andahuaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANDAHUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_apurimac_andahuaylas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANDAHUAYLAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Apurimac-Antabamba
poblacion_apurimac_antabamba = 11897
positivos_apurimac_antabamba = list(casos_positivos[casos_positivos['PROVINCIA'] == "ANTABAMBA"].shape)[0]
positivos_hombres_apurimac_antabamba = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ANTABAMBA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_apurimac_antabamba = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ANTABAMBA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_apurimac_antabamba = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ANTABAMBA"].shape)[0]

#!Provincia Antabamba - Etapa de vida
fallecidos_preinfancia_apurimac_antabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_apurimac_antabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_apurimac_antabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_apurimac_antabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_apurimac_antabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_apurimac_antabamba = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTABAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Apurimac-Aymaraes
poblacion_apurimac_aymaraes = 29559
positivos_apurimac_aymaraes = list(casos_positivos[casos_positivos['PROVINCIA'] == "AYMARAES"].shape)[0]
positivos_hombres_apurimac_aymaraes = list(casos_positivos[(casos_positivos['PROVINCIA'] == "AYMARAES") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_apurimac_aymaraes = list(casos_positivos[(casos_positivos['PROVINCIA'] == "AYMARAES") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_apurimac_aymaraes = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "AYMARAES"].shape)[0]

#!Provincia Aymaraes - Etapa de vida
fallecidos_preinfancia_apurimac_aymaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYMARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_apurimac_aymaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYMARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_apurimac_aymaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYMARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_apurimac_aymaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYMARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_apurimac_aymaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYMARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_apurimac_aymaraes = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYMARAES") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Apurimac-Cotabambas
poblacion_apurimac_cotabambas = 48314
positivos_apurimac_cotabambas = list(casos_positivos[casos_positivos['PROVINCIA'] == "COTABAMBAS"].shape)[0]
positivos_hombres_apurimac_cotabambas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "COTABAMBAS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_apurimac_cotabambas = list(casos_positivos[(casos_positivos['PROVINCIA'] == "COTABAMBAS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_apurimac_cotabambas = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "COTABAMBAS"].shape)[0]

#!Provincia Cotabambas - Etapa de vida
fallecidos_preinfancia_apurimac_cotabambas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "COTABAMBAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_apurimac_cotabambas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "COTABAMBAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_apurimac_cotabambas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "COTABAMBAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_apurimac_cotabambas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "COTABAMBAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_apurimac_cotabambas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "COTABAMBAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_apurimac_cotabambas = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "COTABAMBAS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Apurimac-Chincheros
poblacion_apurimac_chincheros = 53567
positivos_apurimac_chincheros = list(casos_positivos[casos_positivos['PROVINCIA'] == "CHINCHEROS"].shape)[0]
positivos_hombres_apurimac_chincheros = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHINCHEROS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_apurimac_chincheros = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CHINCHEROS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_apurimac_chincheros = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CHINCHEROS"].shape)[0]

#!Provincia Chincheros - Etapa de vida
fallecidos_preinfancia_apurimac_chincheros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHEROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_apurimac_chincheros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHEROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_apurimac_chincheros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHEROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_apurimac_chincheros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHEROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_apurimac_chincheros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHEROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_apurimac_chincheros = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHEROS") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Apurimac-Grau
poblacion_apurimac_grau = 23829
positivos_apurimac_grau = list(casos_positivos[casos_positivos['PROVINCIA'] == "GRAU"].shape)[0]
positivos_hombres_apurimac_grau = list(casos_positivos[(casos_positivos['PROVINCIA'] == "GRAU") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_apurimac_grau = list(casos_positivos[(casos_positivos['PROVINCIA'] == "GRAU") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_apurimac_grau = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "GRAU"].shape)[0]

#!Provincia Grau - Etapa de vida
fallecidos_preinfancia_apurimac_grau = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAU") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_apurimac_grau = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAU") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_apurimac_grau = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAU") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_apurimac_grau = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAU") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_apurimac_grau = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAU") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_apurimac_grau = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAU") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Departamento Cusco
poblacion_cusco = 1360013
positivos_cusco = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "CUSCO"].shape)[0]
positivos_hombres_cusco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CUSCO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_cusco = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CUSCO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_cusco = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "CUSCO"].shape)[0]

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



#!Departamento Madrededios
poblacion_madrededios = 183162
positivos_madrededios = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "MADRE DE DIOS"].shape)[0]
positivos_hombres_madrededios = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "MADRE DE DIOS") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_madrededios = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "MADRE DE DIOS") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_madrededios = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "MADRE DE DIOS"].shape)[0]

#!Departamento Madrededios - Etapa de vida
fallecidos_preinfancia_madrededios = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_madrededios = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_madrededios = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_madrededios = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_madrededios = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_madrededios = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "URUBAMBA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Madre de Dios  
#!Madrededios-tambopata
poblacion_madre_de_dios_tambopata = 135259
positivos_madre_de_dios_tambopata = list(casos_positivos[casos_positivos['PROVINCIA'] == "TAMBOPATA"].shape)[0]
positivos_hombres_madre_de_dios_tambopata = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAMBOPATA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_madre_de_dios_tambopata = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAMBOPATA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_madre_de_dios_tambopata = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TAMBOPATA"].shape)[0]

#!Provincia Tambopata - Etapa de vida
fallecidos_preinfancia_madre_de_dios_tambopata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_madre_de_dios_tambopata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_madre_de_dios_tambopata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_madre_de_dios_tambopata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_madre_de_dios_tambopata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_madre_de_dios_tambopata = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAMBOPATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Madrededios-manu
poblacion_madre_de_dios_manu = 29878
positivos_madre_de_dios_manu = list(casos_positivos[casos_positivos['PROVINCIA'] == "MANU"].shape)[0]
positivos_hombres_madre_de_dios_manu = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MANU") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_madre_de_dios_manu = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MANU") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_madre_de_dios_manu = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MANU"].shape)[0]

#!Provincia Manu - Etapa de vida
fallecidos_preinfancia_madre_de_dios_manu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_madre_de_dios_manu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_madre_de_dios_manu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_madre_de_dios_manu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_madre_de_dios_manu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_madre_de_dios_manu = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Madrededios-tahuamanu
poblacion_madre_de_dios_tahuamanu = 18025
positivos_madre_de_dios_tahuamanu = list(casos_positivos[casos_positivos['PROVINCIA'] == "TAHUAMANU"].shape)[0]
positivos_hombres_madre_de_dios_tahuamanu = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAHUAMANU") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_madre_de_dios_tahuamanu = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TAHUAMANU") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_madre_de_dios_tahuamanu = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TAHUAMANU"].shape)[0]

#!Provincia Tahuamanu - Etapa de vida
fallecidos_preinfancia_madre_de_dios_tahuamanu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_madre_de_dios_tahuamanu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_madre_de_dios_tahuamanu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_madre_de_dios_tahuamanu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_madre_de_dios_tahuamanu = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_madre_de_dios_tahuamanu = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "TAHUAMANU") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Departamento Puno
poblacion_puno = 1214793
positivos_puno = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "PUNO"].shape)[0]
positivos_hombres_puno = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PUNO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_puno = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "PUNO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_puno = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "PUNO"].shape)[0]

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


#!Departamento Arequipa
poblacion_arequipa = 1526342
positivos_arequipa = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "AREQUIPA"].shape)[0]
positivos_hombres_arequipa = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AREQUIPA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AREQUIPA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "AREQUIPA"].shape)[0]

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

#!Arequipa-Cayllona
poblacion_arequipa_cayllona = 106801
positivos_arequipa_cayllona = list(casos_positivos[casos_positivos['PROVINCIA'] == "CAYLLOMA"].shape)[0]
positivos_hombres_arequipa_cayllona = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CAYLLOMA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa_cayllona = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CAYLLOMA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa_cayllona = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CAYLLOMA"].shape)[0]

#!Provincia Castilla  - Etapa de vida
fallecidos_preinfancia_arequipa_cayllona = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_arequipa_cayllona = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_arequipa_cayllona = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_arequipa_cayllona = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_arequipa_cayllona = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_arequipa_cayllona = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CAYLLOMA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Arequipa-Condesuyos
poblacion_arequipa_condesuyos = 24691
positivos_arequipa_condesuyos = list(casos_positivos[casos_positivos['PROVINCIA'] == "CONDESUYOS"].shape)[0]
positivos_hombres_arequipa_condesuyos = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CONDESUYOS") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_arequipa_condesuyos = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CONDESUYOS") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_arequipa_condesuyos = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CONDESUYOS"].shape)[0]

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

#!Departamento Moquegua
poblacion_moquegua = 194613
positivos_moquegua = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "MOQUEGUA"].shape)[0]
positivos_hombres_moquegua = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "MOQUEGUA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_moquegua = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "MOQUEGUA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_moquegua = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "MOQUEGUA"].shape)[0]

#!Departamento Moquegua - Etapa de vida
fallecidos_preinfancia_moquegua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_moquegua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_moquegua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_moquegua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_moquegua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_moquegua = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MOQUEGUA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Moquegua-Mariscal Nieto
poblacion_moquegua_mariscal_nieto = 88491
positivos_moquegua_mariscal_nieto = list(casos_positivos[casos_positivos['PROVINCIA'] == "MARISCAL NIETO"].shape)[0]
positivos_hombres_moquegua_mariscal_nieto = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MARISCAL NIETO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_moquegua_mariscal_nieto = list(casos_positivos[(casos_positivos['PROVINCIA'] == "MARISCAL NIETO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_moquegua_mariscal_nieto = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "MARISCAL NIETO"].shape)[0]

#!Provincia Mariscal Nieto - Etapa de vida
fallecidos_preinfancia_moquegua_mariscal_nieto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_moquegua_mariscal_nieto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_moquegua_mariscal_nieto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_moquegua_mariscal_nieto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_moquegua_mariscal_nieto = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_moquegua_mariscal_nieto = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="MARISCAL NIETO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Moquegua-General Sanchez Cerro
poblacion_moquegua_general_sanchez_cerro = 29333
positivos_moquegua_general_sanchez_cerro = list(casos_positivos[casos_positivos['PROVINCIA'] == "GENERAL SANCHEZ CERRO"].shape)[0]
positivos_hombres_moquegua_general_sanchez_cerro = list(casos_positivos[(casos_positivos['PROVINCIA'] == "GENERAL SANCHEZ CERRO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_moquegua_general_sanchez_cerro = list(casos_positivos[(casos_positivos['PROVINCIA'] == "GENERAL SANCHEZ CERRO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_moquegua_general_sanchez_cerro = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "GENERAL SANCHEZ CERRO"].shape)[0]

#!Provincia Sanchez Cerro - Etapa de vida
fallecidos_preinfancia_moquegua_general_sanchez_cerro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_moquegua_general_sanchez_cerro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_moquegua_general_sanchez_cerro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_moquegua_general_sanchez_cerro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_moquegua_general_sanchez_cerro = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_moquegua_general_sanchez_cerro = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="GENERAL SANCHEZ CERRO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Moquegua-Ilo
poblacion_moquegua_ilo = 76789
positivos_moquegua_ilo = list(casos_positivos[casos_positivos['PROVINCIA'] == "ILO"].shape)[0]
positivos_hombres_moquegua_ilo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ILO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_moquegua_ilo = list(casos_positivos[(casos_positivos['PROVINCIA'] == "ILO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_moquegua_ilo = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "ILO"].shape)[0]

#!Provincia Sanchez Cerro - Etapa de vida
fallecidos_preinfancia_moquegua_ilo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_moquegua_ilo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_moquegua_ilo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_moquegua_ilo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_moquegua_ilo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_moquegua_ilo = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="ILO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]



#!Departamento Tacna
poblacion_tacna = 378316
positivos_tacna = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "TACNA"].shape)[0]
positivos_hombres_tacna = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "TACNA") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tacna = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "TACNA") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tacna = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "TACNA"].shape)[0]

#!Departamento Tacna - Etapa de vida
fallecidos_preinfancia_tacna = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tacna = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tacna = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tacna = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tacna = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tacna = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Provincias Tacna
#!Tacna-Tacna
poblacion_tacna_tacna = 350222
positivos_tacna_tacna = list(casos_positivos[casos_positivos['PROVINCIA'] == "TACNA"].shape)[0]
positivos_hombres_tacna_tacna = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TACNA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tacna_tacna = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TACNA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tacna_tacna = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TACNA"].shape)[0]

#!Provincia Tacna - Etapa de vida
fallecidos_preinfancia_tacna_tacna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tacna_tacna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tacna_tacna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tacna_tacna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tacna_tacna = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tacna_tacna = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TACNA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Tacna-Candarave
poblacion_tacna_candarave = 9044
positivos_tacna_candarave = list(casos_positivos[casos_positivos['PROVINCIA'] == "CANDARAVE"].shape)[0]
positivos_hombres_tacna_candarave = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANDARAVE") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tacna_candarave = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CANDARAVE") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tacna_candarave = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CANDARAVE"].shape)[0]

#!Provincia Candarave - Etapa de vida
fallecidos_preinfancia_tacna_candarave = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tacna_candarave = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tacna_candarave = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tacna_candarave = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tacna_candarave = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tacna_candarave = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CANDARAVE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Tacna-Jorge Basadre
poblacion_tacna_jorge_basadre = 10110
positivos_tacna_jorge_basadre = list(casos_positivos[casos_positivos['PROVINCIA'] == "JORGE BASADRE"].shape)[0]
positivos_hombres_tacna_jorge_basadre = list(casos_positivos[(casos_positivos['PROVINCIA'] == "JORGE BASADRE") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tacna_jorge_basadre = list(casos_positivos[(casos_positivos['PROVINCIA'] == "JORGE BASADRE") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tacna_jorge_basadre = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "JORGE BASADRE"].shape)[0]

#!Provincia Candarave - Jorge Basadre
fallecidos_preinfancia_tacna_jorge_basadre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tacna_jorge_basadre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tacna_jorge_basadre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tacna_jorge_basadre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tacna_jorge_basadre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tacna_jorge_basadre = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="JORGE BASADRE") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

#!Tacna-Tarata
poblacion_tacna_tarata = 8940
positivos_tacna_tarata = list(casos_positivos[casos_positivos['PROVINCIA'] == "TARATA"].shape)[0]
positivos_hombres_tacna_tarata = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TARATA") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_tacna_tarata = list(casos_positivos[(casos_positivos['PROVINCIA'] == "TARATA") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_tacna_tarata = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "TARATA"].shape)[0]

#!Provincia Candarave - Tarata
fallecidos_preinfancia_tacna_tarata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_tacna_tarata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_tacna_tarata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_tacna_tarata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_tacna_tarata = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_tacna_tarata = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="TARATA") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]


#!Departamento Callao
poblacion_callao = 1147516
positivos_callao = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "CALLAO"].shape)[0]
positivos_hombres_callao = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CALLAO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_callao = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "CALLAO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_callao = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "CALLAO"].shape)[0]

#!Departamento Callao - Tarata
fallecidos_preinfancia_callao = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_callao = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_callao = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_callao = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_callao = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_callao = list(
    casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0] 

#!Provincias Callao
#!Callao-Callao
poblacion_callao_callao = 1147516   
positivos_callao_callao = list(casos_positivos[casos_positivos['PROVINCIA'] == "CALLAO"].shape)[0]
positivos_hombres_callao_callao = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CALLAO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_callao_callao = list(casos_positivos[(casos_positivos['PROVINCIA'] == "CALLAO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_callao_callao = list(casos_fallecidos[casos_fallecidos['PROVINCIA'] == "CALLAO"].shape)[0]

#!Provincia Candarave - Tarata
fallecidos_preinfancia_callao_callao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]
fallecidos_infancia_callao_callao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]
fallecidos_adolescencia_callao_callao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]
fallecidos_juventud_callao_callao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]
fallecidos_adultez_callao_callao = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]
fallecidos_persona_mayor_callao_callao = list(
    casos_fallecidos[(casos_fallecidos['PROVINCIA'] =="CALLAO") & (casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

busqueda = [
    {
      "name": "Loreto",
      "poblacion": poblacion_loreto,
      "positivos": positivos_loreto,
      "hombres_infectados": positivos_hombres_loreto,
      "mujeres_infectados": positivos_mujeres_loreto,
      "fallecidos": fallecidos_loreto,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_loreto,
       "infancia": fallecidos_infancia_loreto,
       "adolescencia": fallecidos_adolescencia_loreto,
       "juventud": fallecidos_juventud_loreto,
       "adultez": fallecidos_adultez_loreto,
       "persona_mayor": fallecidos_persona_mayor_loreto
      },
      "url": "loreto",
      "provincias": [
          {"name": "Maynas", "positivos": positivos_loreto_maynas  , "poblacion": poblacion_loreto_maynas , "hombres_infectados": positivos_hombres_loreto_maynas,"mujeres_infectados": positivos_mujeres_loreto_maynas, "fallecidos": fallecidos_loreto_maynas, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_maynas,
          "infancia": fallecidos_infancia_loreto_maynas,
          "adolescencia": fallecidos_adolescencia_loreto_maynas,
          "juventud": fallecidos_juventud_loreto_maynas,
          "adultez": fallecidos_adultez_loreto_maynas,
          "persona_mayor": fallecidos_persona_mayor_loreto_maynas
          }},

          {"name": "Alto Amazonas", "positivos": positivos_loreto_alto_amazonas, "poblacion": poblacion_loreto_alto_amazonas , "hombres_infectados": positivos_hombres_loreto_alto_amazonas,"mujeres_infectados": positivos_mujeres_loreto_alto_amazonas, "fallecidos": fallecidos_loreto_alto_amazonas, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_alto_amazonas,
          "infancia": fallecidos_infancia_loreto_alto_amazonas,
          "adolescencia": fallecidos_adolescencia_loreto_alto_amazonas,
          "juventud": fallecidos_juventud_loreto_alto_amazonas,
          "adultez": fallecidos_adultez_loreto_alto_amazonas,
          "persona_mayor": fallecidos_persona_mayor_loreto_alto_amazonas
          }},

          {"name": "Loreto", "positivos": positivos_loreto_loreto, "poblacion": poblacion_loreto_loreto , "hombres_infectados": positivos_hombres_loreto_loreto,"mujeres_infectados": positivos_mujeres_loreto_loreto, "fallecidos": fallecidos_loreto_loreto, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_loreto,
          "infancia": fallecidos_infancia_loreto_loreto,
          "adolescencia": fallecidos_adolescencia_loreto_loreto,
          "juventud": fallecidos_juventud_loreto_loreto,
          "adultez": fallecidos_adultez_loreto_loreto,
          "persona_mayor": fallecidos_persona_mayor_loreto_loreto
          }},

          {"name": "Mariscal Ramon Castilla", "positivos": positivos_loreto_mariscal_ramon_castilla, "poblacion": poblacion_loreto_mariscal_ramon_castilla , "hombres_infectados": positivos_hombres_loreto_mariscal_ramon_castilla,"mujeres_infectados": positivos_mujeres_loreto_mariscal_ramon_castilla, "fallecidos": fallecidos_loreto_mariscal_ramon_castilla, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_mariscal_ramon_castilla,
          "infancia": fallecidos_infancia_loreto_mariscal_ramon_castilla,
          "adolescencia": fallecidos_adolescencia_loreto_mariscal_ramon_castilla,
          "juventud": fallecidos_juventud_loreto_mariscal_ramon_castilla,
          "adultez": fallecidos_adultez_loreto_mariscal_ramon_castilla,
          "persona_mayor": fallecidos_persona_mayor_loreto_mariscal_ramon_castilla
          }},

          {"name": "Requena", "positivos": positivos_loreto_requena, "poblacion": poblacion_loreto_requena , "hombres_infectados": positivos_hombres_loreto_requena,"mujeres_infectados": positivos_mujeres_loreto_requena, "fallecidos": fallecidos_loreto_requena, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_requena,
          "infancia": fallecidos_infancia_loreto_requena,
          "adolescencia": fallecidos_adolescencia_loreto_requena,
          "juventud": fallecidos_juventud_loreto_requena,
          "adultez": fallecidos_adultez_loreto_requena,
          "persona_mayor": fallecidos_persona_mayor_loreto_requena
          }},

          {"name": "Ucayali", "positivos": positivos_loreto_ucayali, "poblacion": poblacion_loreto_ucayali , "hombres_infectados": positivos_hombres_loreto_ucayali,"mujeres_infectados": positivos_mujeres_loreto_ucayali, "fallecidos": fallecidos_loreto_ucayali, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_ucayali,
          "infancia": fallecidos_infancia_loreto_ucayali,
          "adolescencia": fallecidos_adolescencia_loreto_ucayali,
          "juventud": fallecidos_juventud_loreto_ucayali,
          "adultez": fallecidos_adultez_loreto_ucayali,
          "persona_mayor": fallecidos_persona_mayor_loreto_ucayali
          }},

          {"name": "Datem del Marañon", "positivos": positivos_loreto_datem_del_maranon, "poblacion": poblacion_loreto_datem_del_maranon , "hombres_infectados": positivos_hombres_loreto_datem_del_maranon,"mujeres_infectados": positivos_mujeres_loreto_datem_del_maranon, "fallecidos": fallecidos_loreto_datem_del_maranon, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_datem_del_maranon,
          "infancia": fallecidos_infancia_loreto_datem_del_maranon,
          "adolescencia": fallecidos_adolescencia_loreto_datem_del_maranon,
          "juventud": fallecidos_juventud_loreto_datem_del_maranon,
          "adultez": fallecidos_adultez_loreto_datem_del_maranon,
          "persona_mayor": fallecidos_persona_mayor_loreto_datem_del_maranon
          }},

          {"name": "Putumayo", "positivos": positivos_loreto_putumayo, "poblacion": poblacion_loreto_putumayo , "hombres_infectados": positivos_hombres_loreto_putumayo,"mujeres_infectados": positivos_mujeres_loreto_putumayo, "fallecidos": fallecidos_loreto_putumayo, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_putumayo,
          "infancia": fallecidos_infancia_loreto_putumayo,
          "adolescencia": fallecidos_adolescencia_loreto_putumayo,
          "juventud": fallecidos_juventud_loreto_putumayo,
          "adultez": fallecidos_adultez_loreto_putumayo,
          "persona_mayor": fallecidos_persona_mayor_loreto_putumayo
          }},
      ]
    },
    {
      "name": "Amazonas",
      "poblacion": poblacion_amazonas,
      "positivos": positivos_amazonas,
      "hombres_infectados": positivos_hombres_amazonas,
      "mujeres_infectados": positivos_mujeres_amazonas,
      "fallecidos": fallecidos_amazonas,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas,
       "infancia": fallecidos_infancia_amazonas,
       "adolescencia": fallecidos_adolescencia_amazonas,
       "juventud": fallecidos_juventud_amazonas,
       "adultez": fallecidos_adultez_amazonas,
       "persona_mayor": fallecidos_persona_mayor_amazonas
      },
      "url": "amazonas",
      "provincias": [
          {"name": "Chachapoyas", "positivos": positivos_amazonas_chachapoyas,"poblacion": poblacion_amazonas_chachapoyas,"hombres_infectados": positivos_hombres_amazonas_chachapoyas,"mujeres_infectados": positivos_mujeres_amazonas_chachapoyas, "fallecidos": fallecidos_amazonas_chachapoyas, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_chachapoyas,
       "infancia": fallecidos_infancia_amazonas_chachapoyas,
       "adolescencia": fallecidos_adolescencia_amazonas_chachapoyas,
       "juventud": fallecidos_juventud_amazonas_chachapoyas,
       "adultez": fallecidos_adultez_amazonas_chachapoyas,
       "persona_mayor": fallecidos_persona_mayor_amazonas_chachapoyas
      }},

          {"name": "Bagua", "positivos": positivos_amazonas_bagua,"poblacion": poblacion_amazonas_bagua,"hombres_infectados": positivos_hombres_amazonas_bagua,"mujeres_infectados": positivos_mujeres_amazonas_bagua, "fallecidos": fallecidos_amazonas_bagua, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_bagua,
       "infancia": fallecidos_infancia_amazonas_bagua,
       "adolescencia": fallecidos_adolescencia_amazonas_bagua,
       "juventud": fallecidos_juventud_amazonas_bagua,
       "adultez": fallecidos_adultez_amazonas_bagua,
       "persona_mayor": fallecidos_persona_mayor_amazonas_bagua
      }},

          {"name": "Bongara", "positivos": positivos_amazonas_bongara,"poblacion": poblacion_amazonas_bongara,"hombres_infectados": positivos_hombres_amazonas_bongara,"mujeres_infectados": positivos_mujeres_amazonas_bongara, "fallecidos": fallecidos_amazonas_bongara, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_bongara,
       "infancia": fallecidos_infancia_amazonas_bongara,
       "adolescencia": fallecidos_adolescencia_amazonas_bongara,
       "juventud": fallecidos_juventud_amazonas_bongara,
       "adultez": fallecidos_adultez_amazonas_bongara,
       "persona_mayor": fallecidos_persona_mayor_amazonas_bongara
      }},

          {"name": "Condorcanqui", "positivos": positivos_amazonas_condorcanqui,"poblacion": poblacion_amazonas_condorcanqui,"hombres_infectados": positivos_hombres_amazonas_condorcanqui,"mujeres_infectados": positivos_mujeres_amazonas_condorcanqui, "fallecidos": fallecidos_amazonas_condorcanqui, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_condorcanqui,
       "infancia": fallecidos_infancia_amazonas_condorcanqui,
       "adolescencia": fallecidos_adolescencia_amazonas_condorcanqui,
       "juventud": fallecidos_juventud_amazonas_condorcanqui,
       "adultez": fallecidos_adultez_amazonas_condorcanqui,
       "persona_mayor": fallecidos_persona_mayor_amazonas_condorcanqui
      }},

          {"name": "Luya", "positivos": positivos_amazonas_luya,"poblacion": poblacion_amazonas_luya,"hombres_infectados": positivos_hombres_amazonas_luya,"mujeres_infectados": positivos_mujeres_amazonas_luya, "fallecidos": fallecidos_amazonas_luya, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_luya,
       "infancia": fallecidos_infancia_amazonas_luya,
       "adolescencia": fallecidos_adolescencia_amazonas_luya,
       "juventud": fallecidos_juventud_amazonas_luya,
       "adultez": fallecidos_adultez_amazonas_luya,
       "persona_mayor": fallecidos_persona_mayor_amazonas_luya
      }},

          {"name": "Rodriguez de Mendoza", "positivos": positivos_amazonas_rodriguez_de_mendoza,"poblacion": poblacion_amazonas_rodriguez_de_mendoza,"hombres_infectados": positivos_hombres_amazonas_rodriguez_de_mendoza,"mujeres_infectados": positivos_mujeres_amazonas_rodriguez_de_mendoza, "fallecidos": fallecidos_amazonas_rodriguez_de_mendoza, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_rodriguez_de_mendoza,
       "infancia": fallecidos_infancia_amazonas_rodriguez_de_mendoza,
       "adolescencia": fallecidos_adolescencia_amazonas_rodriguez_de_mendoza,
       "juventud": fallecidos_juventud_amazonas_rodriguez_de_mendoza,
       "adultez": fallecidos_adultez_amazonas_rodriguez_de_mendoza,
       "persona_mayor": fallecidos_persona_mayor_amazonas_rodriguez_de_mendoza
      }},

          {"name": "Utcubamba", "positivos": positivos_amazonas_utcubamba,"poblacion": poblacion_amazonas_utcubamba,"hombres_infectados": positivos_hombres_amazonas_utcubamba,"mujeres_infectados": positivos_mujeres_amazonas_utcubamba, "fallecidos": fallecidos_amazonas_utcubamba, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_utcubamba,
       "infancia": fallecidos_infancia_amazonas_utcubamba,
       "adolescencia": fallecidos_adolescencia_amazonas_utcubamba,
       "juventud": fallecidos_juventud_amazonas_utcubamba,
       "adultez": fallecidos_adultez_amazonas_utcubamba,
       "persona_mayor": fallecidos_persona_mayor_amazonas_utcubamba
      }}
      ]
    },
    {
      "name": "Tumbes",
      "poblacion": poblacion_tumbes,
      "positivos": positivos_tumbes,
      "hombres_infectados": positivos_hombres_tumbes,
      "mujeres_infectados": positivos_mujeres_tumbes,
      "fallecidos": fallecidos_tumbes,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tumbes,
       "infancia": fallecidos_infancia_tumbes,
       "adolescencia": fallecidos_adolescencia_tumbes,
       "juventud": fallecidos_juventud_tumbes,
       "adultez": fallecidos_adultez_tumbes,
       "persona_mayor": fallecidos_persona_mayor_tumbes
      },
      "url": "tumbes",
      "provincias": [
          {"name": "Tumbes", "positivos": positivos_tumbes_tumbes, "poblacion": poblacion_tumbes_tumbes, "hombres_infectados": positivos_hombres_tumbes_tumbes,"mujeres_infectados": positivos_mujeres_tumbes_tumbes, "fallecidos": fallecidos_tumbes_tumbes, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tumbes_tumbes,
       "infancia": fallecidos_infancia_tumbes_tumbes,
       "adolescencia": fallecidos_adolescencia_tumbes_tumbes,
       "juventud": fallecidos_juventud_tumbes_tumbes,
       "adultez": fallecidos_adultez_tumbes_tumbes,
       "persona_mayor": fallecidos_persona_mayor_tumbes_tumbes
      }},

          {"name": "Contralmirante Villar", "positivos": positivos_tumbes_contralmirante_villar, "poblacion": poblacion_tumbes_contralmirante_villar, "hombres_infectados": positivos_hombres_tumbes_contralmirante_villar,"mujeres_infectados": positivos_mujeres_tumbes_contralmirante_villar, "fallecidos": fallecidos_tumbes_contralmirante_villar, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tumbes_contralmirante_villar,
       "infancia": fallecidos_infancia_tumbes_contralmirante_villar,
       "adolescencia": fallecidos_adolescencia_tumbes_contralmirante_villar,
       "juventud": fallecidos_juventud_tumbes_contralmirante_villar,
       "adultez": fallecidos_adultez_tumbes_contralmirante_villar,
       "persona_mayor": fallecidos_persona_mayor_tumbes_contralmirante_villar
      }},

          {"name": "Zarumilla", "positivos": positivos_tumbes_zarumilla, "poblacion": poblacion_tumbes_zarumilla, "hombres_infectados": positivos_hombres_tumbes_zarumilla,"mujeres_infectados": positivos_mujeres_tumbes_zarumilla, "fallecidos": fallecidos_tumbes_zarumilla, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tumbes_zarumilla,
       "infancia": fallecidos_infancia_tumbes_zarumilla,
       "adolescencia": fallecidos_adolescencia_tumbes_zarumilla,
       "juventud": fallecidos_juventud_tumbes_zarumilla,
       "adultez": fallecidos_adultez_tumbes_zarumilla,
       "persona_mayor": fallecidos_persona_mayor_tumbes_zarumilla
      }}
      ]
    },
    {
      "name": "Piura",
      "poblacion": poblacion_piura,
      "positivos": positivos_piura,
      "hombres_infectados": positivos_hombres_piura,
      "mujeres_infectados": positivos_mujeres_piura,
      "fallecidos": fallecidos_piura,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura,
       "infancia": fallecidos_infancia_piura,
       "adolescencia": fallecidos_adolescencia_piura,
       "juventud": fallecidos_juventud_piura,
       "adultez": fallecidos_adultez_piura,
       "persona_mayor": fallecidos_persona_mayor_piura
      },
      "url": "piura",
      "provincias": [
          {"name": "Piura", "positivos": positivos_piura_piura,"poblacion": poblacion_piura_piura,"hombres_infectados": positivos_hombres_piura_piura,"mujeres_infectados": positivos_mujeres_piura_piura, "fallecidos": fallecidos_piura_piura, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_piura,
       "infancia": fallecidos_infancia_piura_piura,
       "adolescencia": fallecidos_adolescencia_piura_piura,
       "juventud": fallecidos_juventud_piura_piura,
       "adultez": fallecidos_adultez_piura_piura,
       "persona_mayor": fallecidos_persona_mayor_piura_piura
      }},

          {"name": "Ayabaca", "positivos": positivos_piura_ayabaca,"poblacion": poblacion_piura_ayabaca,"hombres_infectados": positivos_hombres_piura_ayabaca,"mujeres_infectados": positivos_mujeres_piura_ayabaca, "fallecidos": fallecidos_piura_ayabaca, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_ayabaca,
       "infancia": fallecidos_infancia_piura_ayabaca,
       "adolescencia": fallecidos_adolescencia_piura_ayabaca,
       "juventud": fallecidos_juventud_piura_ayabaca,
       "adultez": fallecidos_adultez_piura_ayabaca,
       "persona_mayor": fallecidos_persona_mayor_piura_ayabaca
      }},

          {"name": "Huancabamba", "positivos": positivos_piura_huancabamba,"poblacion": poblacion_piura_huancabamba,"hombres_infectados": positivos_hombres_piura_huancabamba,"mujeres_infectados": positivos_mujeres_piura_huancabamba, "fallecidos": fallecidos_piura_huancabamba, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_huancabamba,
       "infancia": fallecidos_infancia_piura_huancabamba,
       "adolescencia": fallecidos_adolescencia_piura_huancabamba,
       "juventud": fallecidos_juventud_piura_huancabamba,
       "adultez": fallecidos_adultez_piura_huancabamba,
       "persona_mayor": fallecidos_persona_mayor_piura_huancabamba
      }},

          {"name": "Morropon", "positivos": positivos_piura_morropon,"poblacion": poblacion_piura_morropon,"hombres_infectados": positivos_hombres_piura_morropon,"mujeres_infectados": positivos_mujeres_piura_morropon, "fallecidos": fallecidos_piura_morropon, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_morropon,
       "infancia": fallecidos_infancia_piura_morropon,
       "adolescencia": fallecidos_adolescencia_piura_morropon,
       "juventud": fallecidos_juventud_piura_morropon,
       "adultez": fallecidos_adultez_piura_morropon,
       "persona_mayor": fallecidos_persona_mayor_piura_morropon
      }},

          {"name": "Paita", "positivos": positivos_piura_paita,"poblacion": poblacion_piura_paita,"hombres_infectados": positivos_hombres_piura_paita,"mujeres_infectados": positivos_mujeres_piura_paita, "fallecidos": fallecidos_piura_paita, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_paita,
       "infancia": fallecidos_infancia_piura_paita,
       "adolescencia": fallecidos_adolescencia_piura_paita,
       "juventud": fallecidos_juventud_piura_paita,
       "adultez": fallecidos_adultez_piura_paita,
       "persona_mayor": fallecidos_persona_mayor_piura_paita
      }},

          {"name": "Sullana", "positivos": positivos_piura_sullana,"poblacion": poblacion_piura_sullana,"hombres_infectados": positivos_hombres_piura_sullana,"mujeres_infectados": positivos_mujeres_piura_sullana, "fallecidos": fallecidos_piura_sullana, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_sullana,
       "infancia": fallecidos_infancia_piura_sullana,
       "adolescencia": fallecidos_adolescencia_piura_sullana,
       "juventud": fallecidos_juventud_piura_sullana,
       "adultez": fallecidos_adultez_piura_sullana,
       "persona_mayor": fallecidos_persona_mayor_piura_sullana
      }},

          {"name": "Talara", "positivos": positivos_piura_talara,"poblacion": poblacion_piura_talara,"hombres_infectados": positivos_hombres_piura_talara,"mujeres_infectados": positivos_mujeres_piura_talara, "fallecidos": fallecidos_piura_talara, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_talara,
       "infancia": fallecidos_infancia_piura_talara,
       "adolescencia": fallecidos_adolescencia_piura_talara,
       "juventud": fallecidos_juventud_piura_talara,
       "adultez": fallecidos_adultez_piura_talara,
       "persona_mayor": fallecidos_persona_mayor_piura_talara
      }},

          {"name": "Sechura", "positivos": positivos_piura_sechura,"poblacion": poblacion_piura_sechura, "hombres_infectados": positivos_hombres_piura_sechura,"mujeres_infectados": positivos_mujeres_piura_sechura, "fallecidos": fallecidos_piura_sechura, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_piura_sechura,
       "infancia": fallecidos_infancia_piura_sechura,
       "adolescencia": fallecidos_adolescencia_piura_sechura,
       "juventud": fallecidos_juventud_piura_sechura,
       "adultez": fallecidos_adultez_piura_sechura,
       "persona_mayor": fallecidos_persona_mayor_piura_sechura
      }}
      ]
    },
    {
      "name": "Lambayeque",
      "poblacion": poblacion_lambayeque,
      "positivos": positivos_lambayeque,
      "hombres_infectados": positivos_hombres_lambayeque,
      "mujeres_infectados": positivos_mujeres_lambayeque,
      "fallecidos": fallecidos_lambayeque,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lambayeque,
       "infancia": fallecidos_infancia_lambayeque,
       "adolescencia": fallecidos_adolescencia_lambayeque,
       "juventud": fallecidos_juventud_lambayeque,
       "adultez": fallecidos_adultez_lambayeque,
       "persona_mayor": fallecidos_persona_mayor_lambayeque
      },
      "url": "lambayeque",
      "provincias": [
          {"name": "Chiclayo", "positivos": positivos_lambayeque_chiclayo, "poblacion": poblacion_lambayeque_chiclayo, "hombres_infectados": positivos_hombres_lambayeque_chiclayo,"mujeres_infectados": positivos_mujeres_lambayeque_chiclayo, "fallecidos": fallecidos_lambayeque_chiclayo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lambayeque_chiclayo,
       "infancia": fallecidos_infancia_lambayeque_chiclayo,
       "adolescencia": fallecidos_adolescencia_lambayeque_chiclayo,
       "juventud": fallecidos_juventud_lambayeque_chiclayo,
       "adultez": fallecidos_adultez_lambayeque_chiclayo,
       "persona_mayor": fallecidos_persona_mayor_lambayeque_chiclayo
      }},

          {"name": "Ferreñafe", "positivos": positivos_lambayeque_ferrenafe, "poblacion": poblacion_lambayeque_ferrenafe, "hombres_infectados": positivos_hombres_lambayeque_ferrenafe,"mujeres_infectados": positivos_mujeres_lambayeque_ferrenafe, "fallecidos": fallecidos_lambayeque_ferrenafe, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lambayeque_ferrenafe,
       "infancia": fallecidos_infancia_lambayeque_ferrenafe,
       "adolescencia": fallecidos_adolescencia_lambayeque_ferrenafe,
       "juventud": fallecidos_juventud_lambayeque_ferrenafe,
       "adultez": fallecidos_adultez_lambayeque_ferrenafe,
       "persona_mayor": fallecidos_persona_mayor_lambayeque_ferrenafe
      }},

          {"name": "Lambayeque", "positivos": positivos_lambayeque_lambayeque, "poblacion": poblacion_lambayeque_lambayeque, "hombres_infectados": positivos_hombres_lambayeque_lambayeque,"mujeres_infectados": positivos_mujeres_lambayeque_lambayeque, "fallecidos": fallecidos_lambayeque_lambayeque, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lambayeque_lambayeque,
       "infancia": fallecidos_infancia_lambayeque_lambayeque,
       "adolescencia": fallecidos_adolescencia_lambayeque_lambayeque,
       "juventud": fallecidos_juventud_lambayeque_lambayeque,
       "adultez": fallecidos_adultez_lambayeque_lambayeque,
       "persona_mayor": fallecidos_persona_mayor_lambayeque_lambayeque
      }},
      ]
    },
    {
      "name": "Cajamarca",
      "poblacion": poblacion_cajamarca,
      "positivos": positivos_cajamarca,
      "hombres_infectados": positivos_hombres_cajamarca,
      "mujeres_infectados": positivos_mujeres_cajamarca,
      "fallecidos": fallecidos_cajamarca,
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
          {"name": "Cajamarca", "positivos": positivos_cajamarca_cajamarca,"poblacion": poblacion_cajamarca_cajamarca , "hombres_infectados": positivos_hombres_cajamarca_cajamarca,"mujeres_infectados": positivos_mujeres_cajamarca_cajamarca, "fallecidos": fallecidos_cajamarca_cajamarca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_cajamarca,
       "infancia": fallecidos_infancia_cajamarca_cajamarca,
       "adolescencia": fallecidos_adolescencia_cajamarca_cajamarca,
       "juventud": fallecidos_juventud_cajamarca_cajamarca,
       "adultez": fallecidos_adultez_cajamarca_cajamarca,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_cajamarca
      }},

          {"name": "Cajabamba", "positivos": positivos_cajamarca_cajabamba,"poblacion": poblacion_cajamarca_cajabamba , "hombres_infectados": positivos_hombres_cajamarca_cajabamba,"mujeres_infectados": positivos_mujeres_cajamarca_cajabamba, "fallecidos": fallecidos_cajamarca_cajabamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_cajabamba,
       "infancia": fallecidos_infancia_cajamarca_cajabamba,
       "adolescencia": fallecidos_adolescencia_cajamarca_cajabamba,
       "juventud": fallecidos_juventud_cajamarca_cajabamba,
       "adultez": fallecidos_adultez_cajamarca_cajabamba,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_cajabamba
      }},

          {"name": "Celendin", "positivos": positivos_cajamarca_celendin,"poblacion": poblacion_cajamarca_celendin , "hombres_infectados": positivos_hombres_cajamarca_celendin,"mujeres_infectados": positivos_mujeres_cajamarca_celendin, "fallecidos": fallecidos_cajamarca_celendin, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_celendin,
       "infancia": fallecidos_infancia_cajamarca_celendin,
       "adolescencia": fallecidos_adolescencia_cajamarca_celendin,
       "juventud": fallecidos_juventud_cajamarca_celendin,
       "adultez": fallecidos_adultez_cajamarca_celendin,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_celendin
      }},

          {"name": "Chota", "positivos": positivos_cajamarca_chota,"poblacion": poblacion_cajamarca_chota, "hombres_infectados": positivos_hombres_cajamarca_chota,"mujeres_infectados": positivos_mujeres_cajamarca_chota, "fallecidos": fallecidos_cajamarca_chota, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_chota,
       "infancia": fallecidos_infancia_cajamarca_chota,
       "adolescencia": fallecidos_adolescencia_cajamarca_chota,
       "juventud": fallecidos_juventud_cajamarca_chota,
       "adultez": fallecidos_adultez_cajamarca_chota,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_chota
      }},

          {"name": "Contumaza", "positivos": positivos_cajamarca_contumaza,"poblacion": poblacion_cajamarca_contumaza, "hombres_infectados": positivos_hombres_cajamarca_contumaza,"mujeres_infectados": positivos_mujeres_cajamarca_contumaza, "fallecidos": fallecidos_cajamarca_contumaza, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_contumaza,
       "infancia": fallecidos_infancia_cajamarca_contumaza,
       "adolescencia": fallecidos_adolescencia_cajamarca_contumaza,
       "juventud": fallecidos_juventud_cajamarca_contumaza,
       "adultez": fallecidos_adultez_cajamarca_contumaza,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_contumaza
      }},

          {"name": "Cutervo", "positivos": positivos_cajamarca_cutervo,"poblacion": poblacion_cajamarca_cutervo, "hombres_infectados": positivos_hombres_cajamarca_cutervo,"mujeres_infectados": positivos_mujeres_cajamarca_cutervo, "fallecidos": fallecidos_cajamarca_cutervo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_cutervo,
       "infancia": fallecidos_infancia_cajamarca_cutervo,
       "adolescencia": fallecidos_adolescencia_cajamarca_cutervo,
       "juventud": fallecidos_juventud_cajamarca_cutervo,
       "adultez": fallecidos_adultez_cajamarca_cutervo,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_cutervo
      }},

          {"name": "Hualgayoc", "positivos": positivos_cajamarca_hualgayoc,"poblacion": poblacion_cajamarca_hualgayoc, "hombres_infectados": positivos_hombres_cajamarca_hualgayoc,"mujeres_infectados": positivos_mujeres_cajamarca_hualgayoc, "fallecidos": fallecidos_cajamarca_hualgayoc, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_hualgayoc,
       "infancia": fallecidos_infancia_cajamarca_hualgayoc,
       "adolescencia": fallecidos_adolescencia_cajamarca_hualgayoc,
       "juventud": fallecidos_juventud_cajamarca_hualgayoc,
       "adultez": fallecidos_adultez_cajamarca_hualgayoc,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_hualgayoc
      }},

          {"name": "Jaen", "positivos": positivos_cajamarca_jaen,"poblacion": poblacion_cajamarca_jaen, "hombres_infectados": positivos_hombres_cajamarca_jaen,"mujeres_infectados": positivos_mujeres_cajamarca_jaen, "fallecidos": fallecidos_cajamarca_jaen, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_jaen,
       "infancia": fallecidos_infancia_cajamarca_jaen,
       "adolescencia": fallecidos_adolescencia_cajamarca_jaen,
       "juventud": fallecidos_juventud_cajamarca_jaen,
       "adultez": fallecidos_adultez_cajamarca_jaen,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_jaen
      }},

          {"name": "San Ignacio", "positivos": positivos_cajamarca_san_ignacio,"poblacion": poblacion_cajamarca_san_ignacio, "hombres_infectados": positivos_hombres_cajamarca_san_ignacio,"mujeres_infectados": positivos_mujeres_cajamarca_san_ignacio, "fallecidos": fallecidos_cajamarca_san_ignacio, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_san_ignacio,
       "infancia": fallecidos_infancia_cajamarca_san_ignacio,
       "adolescencia": fallecidos_adolescencia_cajamarca_san_ignacio,
       "juventud": fallecidos_juventud_cajamarca_san_ignacio,
       "adultez": fallecidos_adultez_cajamarca_san_ignacio,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_san_ignacio
      }},

          {"name": "San Marcos", "positivos": positivos_cajamarca_san_marcos,"poblacion": poblacion_cajamarca_san_marcos, "hombres_infectados": positivos_hombres_cajamarca_san_marcos,"mujeres_infectados": positivos_mujeres_cajamarca_san_marcos, "fallecidos": fallecidos_cajamarca_san_marcos, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_san_marcos,
       "infancia": fallecidos_infancia_cajamarca_san_marcos,
       "adolescencia": fallecidos_adolescencia_cajamarca_san_marcos,
       "juventud": fallecidos_juventud_cajamarca_san_marcos,
       "adultez": fallecidos_adultez_cajamarca_san_marcos,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_san_marcos
      }},

          {"name": "San Miguel", "positivos": positivos_cajamarca_san_miguel,"poblacion": poblacion_cajamarca_san_miguel, "hombres_infectados": positivos_hombres_cajamarca_san_miguel,"mujeres_infectados": positivos_mujeres_cajamarca_san_miguel, "fallecidos": fallecidos_cajamarca_san_miguel, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_san_miguel,
       "infancia": fallecidos_infancia_cajamarca_san_miguel,
       "adolescencia": fallecidos_adolescencia_cajamarca_san_miguel,
       "juventud": fallecidos_juventud_cajamarca_san_miguel,
       "adultez": fallecidos_adultez_cajamarca_san_miguel,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_san_miguel
      }},

          {"name": "San Pablo", "positivos": positivos_cajamarca_san_pablo,"poblacion": poblacion_cajamarca_san_pablo, "hombres_infectados": positivos_hombres_cajamarca_san_pablo,"mujeres_infectados": positivos_mujeres_cajamarca_san_pablo, "fallecidos": fallecidos_cajamarca_san_pablo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_san_pablo,
       "infancia": fallecidos_infancia_cajamarca_san_pablo,
       "adolescencia": fallecidos_adolescencia_cajamarca_san_pablo,
       "juventud": fallecidos_juventud_cajamarca_san_pablo,
       "adultez": fallecidos_adultez_cajamarca_san_pablo,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_san_pablo
      }},

          {"name": "Santa Cruz", "positivos": positivos_cajamarca_santa_cruz,"poblacion": poblacion_cajamarca_santa_cruz, "hombres_infectados": positivos_hombres_cajamarca_santa_cruz,"mujeres_infectados": positivos_mujeres_cajamarca_santa_cruz, "fallecidos": fallecidos_cajamarca_santa_cruz, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cajamarca_santa_cruz,
       "infancia": fallecidos_infancia_cajamarca_santa_cruz,
       "adolescencia": fallecidos_adolescencia_cajamarca_santa_cruz,
       "juventud": fallecidos_juventud_cajamarca_santa_cruz,
       "adultez": fallecidos_adultez_cajamarca_santa_cruz,
       "persona_mayor": fallecidos_persona_mayor_cajamarca_santa_cruz
      }}

      ]
    },
    {
      "name": "La Libertad",
      "poblacion": poblacion_libertad,
      "positivos": positivos_libertad,
      "hombres_infectados": positivos_hombres_libertad,
      "mujeres_infectados": positivos_mujeres_libertad,
      "fallecidos": fallecidos_libertad,
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
          {"name": "Trujillo", "positivos": positivos_libertad_trujillo, "poblacion": poblacion_libertad_trujillo,"hombres_infectados": positivos_hombres_libertad_trujillo,"mujeres_infectados": positivos_mujeres_libertad_trujillo, "fallecidos": fallecidos_libertad_trujillo, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_trujillo,
       "infancia": fallecidos_infancia_libertad_trujillo,
       "adolescencia": fallecidos_adolescencia_libertad_trujillo,
       "juventud": fallecidos_juventud_libertad_trujillo,
       "adultez": fallecidos_adultez_libertad_trujillo,
       "persona_mayor": fallecidos_persona_mayor_libertad_trujillo
      }},

          {"name": "Ascope", "positivos": positivos_libertad_ascope, "poblacion": poblacion_libertad_ascope,"hombres_infectados": positivos_hombres_libertad_ascope,"mujeres_infectados": positivos_mujeres_libertad_ascope, "fallecidos": fallecidos_libertad_ascope, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_ascope,
       "infancia": fallecidos_infancia_libertad_ascope,
       "adolescencia": fallecidos_adolescencia_libertad_ascope,
       "juventud": fallecidos_juventud_libertad_ascope,
       "adultez": fallecidos_adultez_libertad_ascope,
       "persona_mayor": fallecidos_persona_mayor_libertad_ascope
      }},

          {"name": "Bolivar", "positivos": positivos_libertad_bolivar, "poblacion": poblacion_libertad_bolivar,"hombres_infectados": positivos_hombres_libertad_bolivar,"mujeres_infectados": positivos_mujeres_libertad_bolivar, "fallecidos": fallecidos_libertad_bolivar, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_bolivar,
       "infancia": fallecidos_infancia_libertad_bolivar,
       "adolescencia": fallecidos_adolescencia_libertad_bolivar,
       "juventud": fallecidos_juventud_libertad_bolivar,
       "adultez": fallecidos_adultez_libertad_bolivar,
       "persona_mayor": fallecidos_persona_mayor_libertad_bolivar
      }},

          {"name": "Chepen", "positivos": positivos_libertad_chepen, "poblacion": poblacion_libertad_chepen,"hombres_infectados": positivos_hombres_libertad_chepen,"mujeres_infectados": positivos_mujeres_libertad_chepen, "fallecidos": fallecidos_libertad_chepen, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_chepen,
       "infancia": fallecidos_infancia_libertad_chepen,
       "adolescencia": fallecidos_adolescencia_libertad_chepen,
       "juventud": fallecidos_juventud_libertad_chepen,
       "adultez": fallecidos_adultez_libertad_chepen,
       "persona_mayor": fallecidos_persona_mayor_libertad_chepen
      }},

          {"name": "Julcan", "positivos": positivos_libertad_julcan, "poblacion": poblacion_libertad_julcan,"hombres_infectados": positivos_hombres_libertad_julcan,"mujeres_infectados": positivos_mujeres_libertad_julcan, "fallecidos": fallecidos_libertad_julcan, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_julcan,
       "infancia": fallecidos_infancia_libertad_julcan,
       "adolescencia": fallecidos_adolescencia_libertad_julcan,
       "juventud": fallecidos_juventud_libertad_julcan,
       "adultez": fallecidos_adultez_libertad_julcan,
       "persona_mayor": fallecidos_persona_mayor_libertad_julcan
      }},

          {"name": "Otuzco", "positivos": positivos_libertad_otuzco, "poblacion": poblacion_libertad_otuzco,"hombres_infectados": positivos_hombres_libertad_otuzco,"mujeres_infectados": positivos_mujeres_libertad_otuzco, "fallecidos": fallecidos_libertad_otuzco, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_otuzco,
       "infancia": fallecidos_infancia_libertad_otuzco,
       "adolescencia": fallecidos_adolescencia_libertad_otuzco,
       "juventud": fallecidos_juventud_libertad_otuzco,
       "adultez": fallecidos_adultez_libertad_otuzco,
       "persona_mayor": fallecidos_persona_mayor_libertad_otuzco
      }},

          {"name": "Pacasmayo", "positivos": positivos_libertad_pacasmayo, "poblacion": poblacion_libertad_pacasmayo,"hombres_infectados": positivos_hombres_libertad_pacasmayo,"mujeres_infectados": positivos_mujeres_libertad_pacasmayo, "fallecidos": fallecidos_libertad_pacasmayo, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_pacasmayo,
       "infancia": fallecidos_infancia_libertad_pacasmayo,
       "adolescencia": fallecidos_adolescencia_libertad_pacasmayo,
       "juventud": fallecidos_juventud_libertad_pacasmayo,
       "adultez": fallecidos_adultez_libertad_pacasmayo,
       "persona_mayor": fallecidos_persona_mayor_libertad_pacasmayo
      }},

          {"name": "Pataz", "positivos": positivos_libertad_pataz, "poblacion": poblacion_libertad_pataz,"hombres_infectados": positivos_hombres_libertad_pataz,"mujeres_infectados": positivos_mujeres_libertad_pataz, "fallecidos": fallecidos_libertad_pataz, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_pataz,
       "infancia": fallecidos_infancia_libertad_pataz,
       "adolescencia": fallecidos_adolescencia_libertad_pataz,
       "juventud": fallecidos_juventud_libertad_pataz,
       "adultez": fallecidos_adultez_libertad_pataz,
       "persona_mayor": fallecidos_persona_mayor_libertad_pataz
      }},

          {"name": "Sanchez Carrion", "positivos": positivos_libertad_sanchez_carrion, "poblacion": poblacion_libertad_sanchez_carrion,"hombres_infectados": positivos_hombres_libertad_sanchez_carrion,"mujeres_infectados": positivos_mujeres_libertad_sanchez_carrion, "fallecidos": fallecidos_libertad_sanchez_carrion, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_sanchez_carrion,
       "infancia": fallecidos_infancia_libertad_sanchez_carrion,
       "adolescencia": fallecidos_adolescencia_libertad_sanchez_carrion,
       "juventud": fallecidos_juventud_libertad_sanchez_carrion,
       "adultez": fallecidos_adultez_libertad_sanchez_carrion,
       "persona_mayor": fallecidos_persona_mayor_libertad_sanchez_carrion
      }},

          {"name": "Santiago de Chuco", "positivos": positivos_libertad_santiago_de_chuco, "poblacion": poblacion_libertad_santiago_de_chuco,"hombres_infectados": positivos_hombres_libertad_santiago_de_chuco,"mujeres_infectados": positivos_mujeres_libertad_santiago_de_chuco, "fallecidos": fallecidos_libertad_santiago_de_chuco, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_santiago_de_chuco,
       "infancia": fallecidos_infancia_libertad_santiago_de_chuco,
       "adolescencia": fallecidos_adolescencia_libertad_santiago_de_chuco,
       "juventud": fallecidos_juventud_libertad_santiago_de_chuco,
       "adultez": fallecidos_adultez_libertad_santiago_de_chuco,
       "persona_mayor": fallecidos_persona_mayor_libertad_santiago_de_chuco
      }},

          {"name": "Gran Chimu", "positivos": positivos_libertad_gran_chimu, "poblacion": poblacion_libertad_gran_chimu,"hombres_infectados": positivos_hombres_libertad_gran_chimu,"mujeres_infectados": positivos_mujeres_libertad_gran_chimu, "fallecidos": fallecidos_libertad_gran_chimu, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_gran_chimu,
       "infancia": fallecidos_infancia_libertad_gran_chimu,
       "adolescencia": fallecidos_adolescencia_libertad_gran_chimu,
       "juventud": fallecidos_juventud_libertad_gran_chimu,
       "adultez": fallecidos_adultez_libertad_gran_chimu,
       "persona_mayor": fallecidos_persona_mayor_libertad_gran_chimu
      }},

          {"name": "Viru", "positivos": positivos_libertad_viru, "poblacion": poblacion_libertad_viru,"hombres_infectados": positivos_hombres_libertad_viru,"mujeres_infectados": positivos_mujeres_libertad_viru, "fallecidos": fallecidos_libertad_viru, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_libertad_viru,
       "infancia": fallecidos_infancia_libertad_viru,
       "adolescencia": fallecidos_adolescencia_libertad_viru,
       "juventud": fallecidos_juventud_libertad_viru,
       "adultez": fallecidos_adultez_libertad_viru,
       "persona_mayor": fallecidos_persona_mayor_libertad_viru
      }}
      ]
    },
    {
      "name": "Ancash",
      "poblacion": poblacion_ancash,
      "positivos": positivos_ancash,
      "hombres_infectados": positivos_hombres_ancash,
      "mujeres_infectados": positivos_mujeres_ancash,
      "fallecidos": fallecidos_ancash,
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
          {"name": "Huaraz", "positivos": positivos_ancash_huaraz, "poblacion": poblacion_ancash_huaraz , "hombres_infectados": positivos_hombres_ancash_huaraz,"mujeres_infectados": positivos_mujeres_ancash_huaraz, "fallecidos": fallecidos_ancash_huaraz, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_huaraz,
       "infancia": fallecidos_infancia_ancash_huaraz,
       "adolescencia": fallecidos_adolescencia_ancash_huaraz,
       "juventud": fallecidos_juventud_ancash_huaraz,
       "adultez": fallecidos_adultez_ancash_huaraz,
       "persona_mayor": fallecidos_persona_mayor_ancash_huaraz
      }},

          {"name": "Aija", "positivos": positivos_ancash_aija, "poblacion": poblacion_ancash_aija , "hombres_infectados": positivos_hombres_ancash_aija,"mujeres_infectados": positivos_mujeres_ancash_aija, "fallecidos": fallecidos_ancash_aija, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_aija,
       "infancia": fallecidos_infancia_ancash_aija,
       "adolescencia": fallecidos_adolescencia_ancash_aija,
       "juventud": fallecidos_juventud_ancash_aija,
       "adultez": fallecidos_adultez_ancash_aija,
       "persona_mayor": fallecidos_persona_mayor_ancash_aija
      }},

          {"name": "Antonio Raimondi", "positivos": positivos_ancash_antonio_raimondi, "poblacion": poblacion_ancash_antonio_raimondi , "hombres_infectados": positivos_hombres_ancash_antonio_raimondi,"mujeres_infectados": positivos_mujeres_ancash_antonio_raimondi, "fallecidos": fallecidos_ancash_antonio_raimondi, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_antonio_raimondi,
       "infancia": fallecidos_infancia_ancash_antonio_raimondi,
       "adolescencia": fallecidos_adolescencia_ancash_antonio_raimondi,
       "juventud": fallecidos_juventud_ancash_antonio_raimondi,
       "adultez": fallecidos_adultez_ancash_antonio_raimondi,
       "persona_mayor": fallecidos_persona_mayor_ancash_antonio_raimondi
      }},

          {"name": "Asuncion", "positivos": positivos_ancash_asuncion, "poblacion": poblacion_ancash_asuncion , "hombres_infectados": positivos_hombres_ancash_asuncion,"mujeres_infectados": positivos_mujeres_ancash_asuncion, "fallecidos": fallecidos_ancash_asuncion, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_asuncion,
       "infancia": fallecidos_infancia_ancash_asuncion,
       "adolescencia": fallecidos_adolescencia_ancash_asuncion,
       "juventud": fallecidos_juventud_ancash_asuncion,
       "adultez": fallecidos_adultez_ancash_asuncion,
       "persona_mayor": fallecidos_persona_mayor_ancash_asuncion
      }},

          {"name": "Bolognesi", "positivos": positivos_ancash_bolognesi, "poblacion": poblacion_ancash_bolognesi , "hombres_infectados": positivos_hombres_ancash_bolognesi,"mujeres_infectados": positivos_mujeres_ancash_bolognesi, "fallecidos": fallecidos_ancash_bolognesi, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_bolognesi,
       "infancia": fallecidos_infancia_ancash_bolognesi,
       "adolescencia": fallecidos_adolescencia_ancash_bolognesi,
       "juventud": fallecidos_juventud_ancash_bolognesi,
       "adultez": fallecidos_adultez_ancash_bolognesi,
       "persona_mayor": fallecidos_persona_mayor_ancash_bolognesi
      }},

          {"name": "Carhuaz", "positivos": positivos_ancash_carhuaz, "poblacion": poblacion_ancash_carhuaz , "hombres_infectados": positivos_hombres_ancash_carhuaz,"mujeres_infectados": positivos_mujeres_ancash_carhuaz, "fallecidos": fallecidos_ancash_carhuaz, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_carhuaz,
       "infancia": fallecidos_infancia_ancash_carhuaz,
       "adolescencia": fallecidos_adolescencia_ancash_carhuaz,
       "juventud": fallecidos_juventud_ancash_carhuaz,
       "adultez": fallecidos_adultez_ancash_carhuaz,
       "persona_mayor": fallecidos_persona_mayor_ancash_carhuaz
      }},

          {"name": "Carlos Fermin Fitzcarrald", "positivos": positivos_ancash_carlos_fermin_fitzcarrald, "poblacion": poblacion_ancash_carlos_fermin_fitzcarrald , "hombres_infectados": positivos_hombres_ancash_carlos_fermin_fitzcarrald,"mujeres_infectados": positivos_mujeres_ancash_carlos_fermin_fitzcarrald, "fallecidos": fallecidos_ancash_carlos_fermin_fitzcarrald, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_carlos_fermin_fitzcarrald,
       "infancia": fallecidos_infancia_ancash_carlos_fermin_fitzcarrald,
       "adolescencia": fallecidos_adolescencia_ancash_carlos_fermin_fitzcarrald,
       "juventud": fallecidos_juventud_ancash_carlos_fermin_fitzcarrald,
       "adultez": fallecidos_adultez_ancash_carlos_fermin_fitzcarrald,
       "persona_mayor": fallecidos_persona_mayor_ancash_carlos_fermin_fitzcarrald
      }},

          {"name": "Casma", "positivos": positivos_ancash_casma, "poblacion": poblacion_ancash_casma , "hombres_infectados": positivos_hombres_ancash_casma,"mujeres_infectados": positivos_mujeres_ancash_casma, "fallecidos": fallecidos_ancash_casma, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_casma,
       "infancia": fallecidos_infancia_ancash_casma,
       "adolescencia": fallecidos_adolescencia_ancash_casma,
       "juventud": fallecidos_juventud_ancash_casma,
       "adultez": fallecidos_adultez_ancash_casma,
       "persona_mayor": fallecidos_persona_mayor_ancash_casma
      }},

          {"name": "Corongo", "positivos": positivos_ancash_corongo, "poblacion": poblacion_ancash_corongo , "hombres_infectados": positivos_hombres_ancash_corongo,"mujeres_infectados": positivos_mujeres_ancash_corongo, "fallecidos": fallecidos_ancash_corongo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_corongo,
       "infancia": fallecidos_infancia_ancash_corongo,
       "adolescencia": fallecidos_adolescencia_ancash_corongo,
       "juventud": fallecidos_juventud_ancash_corongo,
       "adultez": fallecidos_adultez_ancash_corongo,
       "persona_mayor": fallecidos_persona_mayor_ancash_corongo
      }},

          {"name": "Huari", "positivos": positivos_ancash_huari, "poblacion": poblacion_ancash_huari , "hombres_infectados": positivos_hombres_ancash_huari,"mujeres_infectados": positivos_mujeres_ancash_huari, "fallecidos": fallecidos_ancash_huari, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_huari,
       "infancia": fallecidos_infancia_ancash_huari,
       "adolescencia": fallecidos_adolescencia_ancash_huari,
       "juventud": fallecidos_juventud_ancash_huari,
       "adultez": fallecidos_adultez_ancash_huari,
       "persona_mayor": fallecidos_persona_mayor_ancash_huari
      }},

          {"name": "Huarmey", "positivos": positivos_ancash_huarmey, "poblacion": poblacion_ancash_huarmey , "hombres_infectados": positivos_hombres_ancash_huarmey,"mujeres_infectados": positivos_mujeres_ancash_huarmey, "fallecidos": fallecidos_ancash_huarmey, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_huarmey,
       "infancia": fallecidos_infancia_ancash_huarmey,
       "adolescencia": fallecidos_adolescencia_ancash_huarmey,
       "juventud": fallecidos_juventud_ancash_huarmey,
       "adultez": fallecidos_adultez_ancash_huarmey,
       "persona_mayor": fallecidos_persona_mayor_ancash_huarmey
      }},

          {"name": "Huaylas", "positivos": positivos_ancash_huaylas, "poblacion": poblacion_ancash_huaylas , "hombres_infectados": positivos_hombres_ancash_huaylas,"mujeres_infectados": positivos_mujeres_ancash_huaylas, "fallecidos": fallecidos_ancash_huaylas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_huaylas,
       "infancia": fallecidos_infancia_ancash_huaylas,
       "adolescencia": fallecidos_adolescencia_ancash_huaylas,
       "juventud": fallecidos_juventud_ancash_huaylas,
       "adultez": fallecidos_adultez_ancash_huaylas,
       "persona_mayor": fallecidos_persona_mayor_ancash_huaylas
      }},

          {"name": "Mariscal Luzuriaga", "positivos": positivos_ancash_mariscal_luzuriaga, "poblacion": poblacion_ancash_mariscal_luzuriaga , "hombres_infectados": positivos_hombres_ancash_mariscal_luzuriaga,"mujeres_infectados": positivos_mujeres_ancash_mariscal_luzuriaga, "fallecidos": fallecidos_ancash_mariscal_luzuriaga, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_mariscal_luzuriaga,
       "infancia": fallecidos_infancia_ancash_mariscal_luzuriaga,
       "adolescencia": fallecidos_adolescencia_ancash_mariscal_luzuriaga,
       "juventud": fallecidos_juventud_ancash_mariscal_luzuriaga,
       "adultez": fallecidos_adultez_ancash_mariscal_luzuriaga,
       "persona_mayor": fallecidos_persona_mayor_ancash_mariscal_luzuriaga
      }},

          {"name": "Ocros", "positivos": positivos_ancash_ocros, "poblacion": poblacion_ancash_ocros , "hombres_infectados": positivos_hombres_ancash_ocros,"mujeres_infectados": positivos_mujeres_ancash_ocros, "fallecidos": fallecidos_ancash_ocros, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_ocros,
       "infancia": fallecidos_infancia_ancash_ocros,
       "adolescencia": fallecidos_adolescencia_ancash_ocros,
       "juventud": fallecidos_juventud_ancash_ocros,
       "adultez": fallecidos_adultez_ancash_ocros,
       "persona_mayor": fallecidos_persona_mayor_ancash_ocros
      }},

          {"name": "Pallasca", "positivos": positivos_ancash_pallasca, "poblacion": poblacion_ancash_pallasca , "hombres_infectados": positivos_hombres_ancash_pallasca,"mujeres_infectados": positivos_mujeres_ancash_pallasca, "fallecidos": fallecidos_ancash_pallasca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_pallasca,
       "infancia": fallecidos_infancia_ancash_pallasca,
       "adolescencia": fallecidos_adolescencia_ancash_pallasca,
       "juventud": fallecidos_juventud_ancash_pallasca,
       "adultez": fallecidos_adultez_ancash_pallasca,
       "persona_mayor": fallecidos_persona_mayor_ancash_pallasca
      }},

          {"name": "Pomabamba", "positivos": positivos_ancash_pomabamba, "poblacion": poblacion_ancash_pomabamba , "hombres_infectados": positivos_hombres_ancash_pomabamba,"mujeres_infectados": positivos_mujeres_ancash_pomabamba, "fallecidos": fallecidos_ancash_pomabamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_pomabamba,
       "infancia": fallecidos_infancia_ancash_pomabamba,
       "adolescencia": fallecidos_adolescencia_ancash_pomabamba,
       "juventud": fallecidos_juventud_ancash_pomabamba,
       "adultez": fallecidos_adultez_ancash_pomabamba,
       "persona_mayor": fallecidos_persona_mayor_ancash_pomabamba
      }},

          {"name": "Recuay", "positivos": positivos_ancash_recuay, "poblacion": poblacion_ancash_recuay , "hombres_infectados": positivos_hombres_ancash_recuay,"mujeres_infectados": positivos_mujeres_ancash_recuay, "fallecidos": fallecidos_ancash_recuay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_recuay,
       "infancia": fallecidos_infancia_ancash_recuay,
       "adolescencia": fallecidos_adolescencia_ancash_recuay,
       "juventud": fallecidos_juventud_ancash_recuay,
       "adultez": fallecidos_adultez_ancash_recuay,
       "persona_mayor": fallecidos_persona_mayor_ancash_recuay
      }},

          {"name": "Santa", "positivos": positivos_ancash_santa, "poblacion": poblacion_ancash_santa , "hombres_infectados": positivos_hombres_ancash_santa,"mujeres_infectados": positivos_mujeres_ancash_santa, "fallecidos": fallecidos_ancash_santa, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_santa,
       "infancia": fallecidos_infancia_ancash_santa,
       "adolescencia": fallecidos_adolescencia_ancash_santa,
       "juventud": fallecidos_juventud_ancash_santa,
       "adultez": fallecidos_adultez_ancash_santa,
       "persona_mayor": fallecidos_persona_mayor_ancash_santa
      }},

          {"name": "Sihuas", "positivos": positivos_ancash_sihuas, "poblacion": poblacion_ancash_sihuas , "hombres_infectados": positivos_hombres_ancash_sihuas,"mujeres_infectados": positivos_mujeres_ancash_sihuas, "fallecidos": fallecidos_ancash_sihuas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_sihuas,
       "infancia": fallecidos_infancia_ancash_sihuas,
       "adolescencia": fallecidos_adolescencia_ancash_sihuas,
       "juventud": fallecidos_juventud_ancash_sihuas,
       "adultez": fallecidos_adultez_ancash_sihuas,
       "persona_mayor": fallecidos_persona_mayor_ancash_sihuas
      }},

          {"name": "Yungay", "positivos": positivos_ancash_yungay, "poblacion": poblacion_ancash_yungay , "hombres_infectados": positivos_hombres_ancash_yungay,"mujeres_infectados": positivos_mujeres_ancash_yungay, "fallecidos": fallecidos_ancash_yungay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ancash_yungay,
       "infancia": fallecidos_infancia_ancash_yungay,
       "adolescencia": fallecidos_adolescencia_ancash_yungay,
       "juventud": fallecidos_juventud_ancash_yungay,
       "adultez": fallecidos_adultez_ancash_yungay,
       "persona_mayor": fallecidos_persona_mayor_ancash_yungay
      }}
      ]
    },
    {
      "name": "San Martin",
      "poblacion": poblacion_sanmartin,
      "positivos": positivos_sanmartin,
      "hombres_infectados": positivos_hombres_sanmartin,
      "mujeres_infectados": positivos_mujeres_sanmartin,
      "fallecidos": fallecidos_sanmartin,
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
          {"name": "Moyobamba", "positivos": positivos_san_martin_moyobamba,"poblacion": poblacion_san_martin_moyobamba , "hombres_infectados": positivos_hombres_san_martin_moyobamba,"mujeres_infectados": positivos_mujeres_san_martin_moyobamba, "fallecidos": fallecidos_san_martin_moyobamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_moyobamba,
       "infancia": fallecidos_infancia_san_martin_moyobamba,
       "adolescencia": fallecidos_adolescencia_san_martin_moyobamba,
       "juventud": fallecidos_juventud_san_martin_moyobamba,
       "adultez": fallecidos_adultez_san_martin_moyobamba,
       "persona_mayor": fallecidos_persona_mayor_san_martin_moyobamba
      }},

          {"name": "Bellavista", "positivos": positivos_san_martin_bellavista,"poblacion": poblacion_san_martin_bellavista , "hombres_infectados": positivos_hombres_san_martin_bellavista,"mujeres_infectados": positivos_mujeres_san_martin_bellavista, "fallecidos": fallecidos_san_martin_bellavista, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_bellavista,
       "infancia": fallecidos_infancia_san_martin_bellavista,
       "adolescencia": fallecidos_adolescencia_san_martin_bellavista,
       "juventud": fallecidos_juventud_san_martin_bellavista,
       "adultez": fallecidos_adultez_san_martin_bellavista,
       "persona_mayor": fallecidos_persona_mayor_san_martin_bellavista
      }},

          {"name": "El Dorado", "positivos": positivos_san_martin_dorado,"poblacion": poblacion_san_martin_dorado , "hombres_infectados": positivos_hombres_san_martin_dorado,"mujeres_infectados": positivos_mujeres_san_martin_dorado, "fallecidos": fallecidos_san_martin_dorado, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_dorado,
       "infancia": fallecidos_infancia_san_martin_dorado,
       "adolescencia": fallecidos_adolescencia_san_martin_dorado,
       "juventud": fallecidos_juventud_san_martin_dorado,
       "adultez": fallecidos_adultez_san_martin_dorado,
       "persona_mayor": fallecidos_persona_mayor_san_martin_dorado
      }},

          {"name": "Huallaga", "positivos": positivos_san_martin_huallaga,"poblacion": poblacion_san_martin_huallaga , "hombres_infectados": positivos_hombres_san_martin_huallaga,"mujeres_infectados": positivos_mujeres_san_martin_huallaga, "fallecidos": fallecidos_san_martin_huallaga, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_huallaga,
       "infancia": fallecidos_infancia_san_martin_huallaga,
       "adolescencia": fallecidos_adolescencia_san_martin_huallaga,
       "juventud": fallecidos_juventud_san_martin_huallaga,
       "adultez": fallecidos_adultez_san_martin_huallaga,
       "persona_mayor": fallecidos_persona_mayor_san_martin_huallaga
      }},

          {"name": "Lamas", "positivos": positivos_san_martin_lamas,"poblacion": poblacion_san_martin_lamas , "hombres_infectados": positivos_hombres_san_martin_lamas,"mujeres_infectados": positivos_mujeres_san_martin_lamas, "fallecidos": fallecidos_san_martin_lamas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_lamas,
       "infancia": fallecidos_infancia_san_martin_lamas,
       "adolescencia": fallecidos_adolescencia_san_martin_lamas,
       "juventud": fallecidos_juventud_san_martin_lamas,
       "adultez": fallecidos_adultez_san_martin_lamas,
       "persona_mayor": fallecidos_persona_mayor_san_martin_lamas
      }},

          {"name": "Mariscal Caceres", "positivos": positivos_san_martin_mariscal_caceres,"poblacion": poblacion_san_martin_mariscal_caceres , "hombres_infectados": positivos_hombres_san_martin_mariscal_caceres,"mujeres_infectados": positivos_mujeres_san_martin_mariscal_caceres, "fallecidos": fallecidos_san_martin_mariscal_caceres, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_mariscal_caceres,
       "infancia": fallecidos_infancia_san_martin_mariscal_caceres,
       "adolescencia": fallecidos_adolescencia_san_martin_mariscal_caceres,
       "juventud": fallecidos_juventud_san_martin_mariscal_caceres,
       "adultez": fallecidos_adultez_san_martin_mariscal_caceres,
       "persona_mayor": fallecidos_persona_mayor_san_martin_mariscal_caceres
      }},

          {"name": "Picota", "positivos": positivos_san_martin_picota,"poblacion": poblacion_san_martin_picota , "hombres_infectados": positivos_hombres_san_martin_picota,"mujeres_infectados": positivos_mujeres_san_martin_picota, "fallecidos": fallecidos_ancash_yungay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_picota,
       "infancia": fallecidos_infancia_san_martin_picota,
       "adolescencia": fallecidos_adolescencia_san_martin_picota,
       "juventud": fallecidos_juventud_san_martin_picota,
       "adultez": fallecidos_adultez_san_martin_picota,
       "persona_mayor": fallecidos_persona_mayor_san_martin_picota
      }},

          {"name": "Rioja", "positivos": positivos_san_martin_rioja,"poblacion": poblacion_san_martin_rioja , "hombres_infectados": positivos_hombres_san_martin_rioja,"mujeres_infectados": positivos_mujeres_san_martin_rioja, "fallecidos": fallecidos_ancash_yungay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_rioja,
       "infancia": fallecidos_infancia_san_martin_rioja,
       "adolescencia": fallecidos_adolescencia_san_martin_rioja,
       "juventud": fallecidos_juventud_san_martin_rioja,
       "adultez": fallecidos_adultez_san_martin_rioja,
       "persona_mayor": fallecidos_persona_mayor_san_martin_rioja
      }},

          {"name": "San Martin", "positivos": positivos_san_martin_san_martin,"poblacion": poblacion_san_martin_san_martin , "hombres_infectados": positivos_hombres_san_martin_san_martin,"mujeres_infectados": positivos_mujeres_san_martin_san_martin, "fallecidos": fallecidos_ancash_yungay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_san_martin,
       "infancia": fallecidos_infancia_san_martin_san_martin,
       "adolescencia": fallecidos_adolescencia_san_martin_san_martin,
       "juventud": fallecidos_juventud_san_martin_san_martin,
       "adultez": fallecidos_adultez_san_martin_san_martin,
       "persona_mayor": fallecidos_persona_mayor_san_martin_san_martin
      }},

          {"name": "Tocache", "positivos": positivos_san_martin_tocache,"poblacion": poblacion_san_martin_tocache , "hombres_infectados": positivos_hombres_san_martin_tocache,"mujeres_infectados": positivos_mujeres_san_martin_tocache, "fallecidos": fallecidos_san_martin_tocache, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_san_martin_tocache,
       "infancia": fallecidos_infancia_san_martin_tocache,
       "adolescencia": fallecidos_adolescencia_san_martin_tocache,
       "juventud": fallecidos_juventud_san_martin_tocache,
       "adultez": fallecidos_adultez_san_martin_tocache,
       "persona_mayor": fallecidos_persona_mayor_san_martin_tocache
      }}
      ]
    },
    {
      "name": "Huanuco",
      "poblacion": poblacion_huanuco,
      "positivos": positivos_huanuco,
      "hombres_infectados": positivos_hombres_huanuco,
      "mujeres_infectados": positivos_mujeres_huanuco,
      "fallecidos": fallecidos_huanuco,
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
         {"name": "Huanuco", "positivos": positivos_huanuco_huanuco,"poblacion": poblacion_huanuco_huanuco , "hombres_infectados": positivos_hombres_huanuco_huanuco,"mujeres_infectados": positivos_mujeres_huanuco_huanuco, "fallecidos": fallecidos_huanuco_huanuco, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_huanuco,
       "infancia": fallecidos_infancia_huanuco_huanuco,
       "adolescencia": fallecidos_adolescencia_huanuco_huanuco,
       "juventud": fallecidos_juventud_huanuco_huanuco,
       "adultez": fallecidos_adultez_huanuco_huanuco,
       "persona_mayor": fallecidos_persona_mayor_huanuco_huanuco
      }},

          {"name": "Ambo", "positivos": positivos_huanuco_ambo,"poblacion": poblacion_huanuco_ambo , "hombres_infectados": positivos_hombres_huanuco_ambo,"mujeres_infectados": positivos_mujeres_huanuco_ambo, "fallecidos": fallecidos_huanuco_ambo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_ambo,
       "infancia": fallecidos_infancia_huanuco_ambo,
       "adolescencia": fallecidos_adolescencia_huanuco_ambo,
       "juventud": fallecidos_juventud_huanuco_ambo,
       "adultez": fallecidos_adultez_huanuco_ambo,
       "persona_mayor": fallecidos_persona_mayor_huanuco_ambo
      }},

          {"name": "Dos de Mayo", "positivos": positivos_huanuco_dos_de_mayo,"poblacion": poblacion_huanuco_dos_de_mayo , "hombres_infectados": positivos_hombres_huanuco_dos_de_mayo,"mujeres_infectados": positivos_mujeres_huanuco_dos_de_mayo, "fallecidos": fallecidos_huanuco_dos_de_mayo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_dos_de_mayo,
       "infancia": fallecidos_infancia_huanuco_dos_de_mayo,
       "adolescencia": fallecidos_adolescencia_huanuco_dos_de_mayo,
       "juventud": fallecidos_juventud_huanuco_dos_de_mayo,
       "adultez": fallecidos_adultez_huanuco_dos_de_mayo,
       "persona_mayor": fallecidos_persona_mayor_huanuco_dos_de_mayo
      }},
          
          {"name": "Huacaybamba", "positivos": positivos_huanuco_huacaybamba,"poblacion": poblacion_huanuco_huacaybamba , "hombres_infectados": positivos_hombres_huanuco_huacaybamba,"mujeres_infectados": positivos_mujeres_huanuco_huacaybamba, "fallecidos": fallecidos_huanuco_huacaybamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_huacaybamba,
       "infancia": fallecidos_infancia_huanuco_huacaybamba,
       "adolescencia": fallecidos_adolescencia_huanuco_huacaybamba,
       "juventud": fallecidos_juventud_huanuco_huacaybamba,
       "adultez": fallecidos_adultez_huanuco_huacaybamba,
       "persona_mayor": fallecidos_persona_mayor_huanuco_huacaybamba
      }},

          {"name": "Huamalies", "positivos": positivos_huanuco_huamalies,"poblacion": poblacion_huanuco_huamalies , "hombres_infectados": positivos_hombres_huanuco_huamalies,"mujeres_infectados": positivos_mujeres_huanuco_huamalies, "fallecidos": fallecidos_huanuco_huamalies, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_huamalies,
       "infancia": fallecidos_infancia_huanuco_huamalies,
       "adolescencia": fallecidos_adolescencia_huanuco_huamalies,
       "juventud": fallecidos_juventud_huanuco_huamalies,
       "adultez": fallecidos_adultez_huanuco_huamalies,
       "persona_mayor": fallecidos_persona_mayor_huanuco_huamalies
      }},

          {"name": "Leoncio Prado", "positivos": positivos_huanuco_leoncio_prado,"poblacion": poblacion_huanuco_leoncio_prado , "hombres_infectados": positivos_hombres_huanuco_leoncio_prado,"mujeres_infectados": positivos_mujeres_huanuco_leoncio_prado, "fallecidos": fallecidos_huanuco_leoncio_prado, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_leoncio_prado,
       "infancia": fallecidos_infancia_huanuco_leoncio_prado,
       "adolescencia": fallecidos_adolescencia_huanuco_leoncio_prado,
       "juventud": fallecidos_juventud_huanuco_leoncio_prado,
       "adultez": fallecidos_adultez_huanuco_leoncio_prado,
       "persona_mayor": fallecidos_persona_mayor_huanuco_leoncio_prado
      }},

          {"name": "Marañon", "positivos": positivos_huanuco_marañon,"poblacion": poblacion_huanuco_marañon , "hombres_infectados": positivos_hombres_huanuco_marañon,"mujeres_infectados": positivos_mujeres_huanuco_marañon, "fallecidos": fallecidos_huanuco_marañon, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_marañon,
       "infancia": fallecidos_infancia_huanuco_marañon,
       "adolescencia": fallecidos_adolescencia_huanuco_marañon,
       "juventud": fallecidos_juventud_huanuco_marañon,
       "adultez": fallecidos_adultez_huanuco_marañon,
       "persona_mayor": fallecidos_persona_mayor_huanuco_marañon
      }},

          {"name": "Pachitea", "positivos": positivos_huanuco_pachitea,"poblacion": poblacion_huanuco_pachitea , "hombres_infectados": positivos_hombres_huanuco_pachitea,"mujeres_infectados": positivos_mujeres_huanuco_pachitea, "fallecidos": fallecidos_huanuco_pachitea, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_pachitea,
       "infancia": fallecidos_infancia_huanuco_pachitea,
       "adolescencia": fallecidos_adolescencia_huanuco_pachitea,
       "juventud": fallecidos_juventud_huanuco_pachitea,
       "adultez": fallecidos_adultez_huanuco_pachitea,
       "persona_mayor": fallecidos_persona_mayor_huanuco_pachitea
      }},

          {"name": "Puerto Inca", "positivos": positivos_huanuco_puerto_inca,"poblacion": poblacion_huanuco_puerto_inca , "hombres_infectados": positivos_hombres_huanuco_puerto_inca,"mujeres_infectados": positivos_mujeres_huanuco_puerto_inca, "fallecidos": fallecidos_huanuco_puerto_inca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_puerto_inca,
       "infancia": fallecidos_infancia_huanuco_puerto_inca,
       "adolescencia": fallecidos_adolescencia_huanuco_puerto_inca,
       "juventud": fallecidos_juventud_huanuco_puerto_inca,
       "adultez": fallecidos_adultez_huanuco_puerto_inca,
       "persona_mayor": fallecidos_persona_mayor_huanuco_puerto_inca
      }},

          {"name": "Lauricocha", "positivos": positivos_huanuco_lauricocha,"poblacion": poblacion_huanuco_lauricocha , "hombres_infectados": positivos_hombres_huanuco_lauricocha,"mujeres_infectados": positivos_mujeres_huanuco_lauricocha, "fallecidos": fallecidos_huanuco_lauricocha, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_lauricocha,
       "infancia": fallecidos_infancia_huanuco_lauricocha,
       "adolescencia": fallecidos_adolescencia_huanuco_lauricocha,
       "juventud": fallecidos_juventud_huanuco_lauricocha,
       "adultez": fallecidos_adultez_huanuco_lauricocha,
       "persona_mayor": fallecidos_persona_mayor_huanuco_lauricocha
      }},

          {"name": "Yarowilca", "positivos": positivos_huanuco_yarowilca,"poblacion": poblacion_huanuco_yarowilca , "hombres_infectados": positivos_hombres_huanuco_yarowilca,"mujeres_infectados": positivos_mujeres_huanuco_yarowilca, "fallecidos": fallecidos_huanuco_yarowilca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huanuco_yarowilca,
       "infancia": fallecidos_infancia_huanuco_yarowilca,
       "adolescencia": fallecidos_adolescencia_huanuco_yarowilca,
       "juventud": fallecidos_juventud_huanuco_yarowilca,
       "adultez": fallecidos_adultez_huanuco_yarowilca,
       "persona_mayor": fallecidos_persona_mayor_huanuco_yarowilca
      }}
      ]
    },
    {
      "name": "Ucayali",
      "poblacion": poblacion_ucayali,
      "positivos": positivos_ucayali,
      "hombres_infectados": positivos_hombres_ucayali,
      "mujeres_infectados": positivos_mujeres_ucayali,
      "fallecidos": fallecidos_ucayali,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ucayali,
       "infancia": fallecidos_infancia_ucayali,
       "adolescencia": fallecidos_adolescencia_ucayali,
       "juventud": fallecidos_juventud_ucayali,
       "adultez": fallecidos_adultez_ucayali,
       "persona_mayor": fallecidos_persona_mayor_ucayali
      },
      "url": "ucayali",
      "provincias": [
          {"name": "Coronel Portillo", "positivos": positivos_ucayali_coronel_portillo,"poblacion": poblacion_ucayali_coronel_portillo , "hombres_infectados": positivos_hombres_ucayali_coronel_portillo,"mujeres_infectados": positivos_mujeres_ucayali_coronel_portillo, "fallecidos": fallecidos_ucayali_coronel_portillo, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ucayali_coronel_portillo,
       "infancia": fallecidos_infancia_ucayali_coronel_portillo,
       "adolescencia": fallecidos_adolescencia_ucayali_coronel_portillo,
       "juventud": fallecidos_juventud_ucayali_coronel_portillo,
       "adultez": fallecidos_adultez_ucayali_coronel_portillo,
       "persona_mayor": fallecidos_persona_mayor_ucayali_coronel_portillo
      }},

          {"name": "Atalaya", "positivos": positivos_ucayali_atalaya,"poblacion": poblacion_ucayali_atalaya , "hombres_infectados": positivos_hombres_ucayali_atalaya,"mujeres_infectados": positivos_mujeres_ucayali_atalaya, "fallecidos": fallecidos_ucayali_atalaya, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ucayali_atalaya,
       "infancia": fallecidos_infancia_ucayali_atalaya,
       "adolescencia": fallecidos_adolescencia_ucayali_atalaya,
       "juventud": fallecidos_juventud_ucayali_atalaya,
       "adultez": fallecidos_adultez_ucayali_atalaya,
       "persona_mayor": fallecidos_persona_mayor_ucayali_atalaya
      }},

          {"name": "Padre Abad", "positivos": positivos_ucayali_padre_abad,"poblacion": poblacion_ucayali_padre_abad , "hombres_infectados": positivos_hombres_ucayali_padre_abad,"mujeres_infectados": positivos_mujeres_ucayali_padre_abad, "fallecidos": fallecidos_ucayali_padre_abad, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ucayali_padre_abad,
       "infancia": fallecidos_infancia_ucayali_padre_abad,
       "adolescencia": fallecidos_adolescencia_ucayali_padre_abad,
       "juventud": fallecidos_juventud_ucayali_padre_abad,
       "adultez": fallecidos_adultez_ucayali_padre_abad,
       "persona_mayor": fallecidos_persona_mayor_ucayali_padre_abad
      }},
          
          {"name": "Purus", "positivos": positivos_ucayali_purus,"poblacion": poblacion_ucayali_purus , "hombres_infectados": positivos_hombres_ucayali_purus,"mujeres_infectados": positivos_mujeres_ucayali_purus, "fallecidos": fallecidos_ucayali_purus, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ucayali_purus,
       "infancia": fallecidos_infancia_ucayali_purus,
       "adolescencia": fallecidos_adolescencia_ucayali_purus,
       "juventud": fallecidos_juventud_ucayali_purus,
       "adultez": fallecidos_adultez_ucayali_purus,
       "persona_mayor": fallecidos_persona_mayor_ucayali_purus
      }}
      ]
    },
    {
      "name": "Pasco",
      "poblacion": poblacion_pasco,
      "positivos": positivos_pasco,
      "hombres_infectados": positivos_hombres_pasco,
      "mujeres_infectados": positivos_mujeres_pasco,
      "fallecidos": fallecidos_pasco,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_pasco,
       "infancia": fallecidos_infancia_pasco,
       "adolescencia": fallecidos_adolescencia_pasco,
       "juventud": fallecidos_juventud_pasco,
       "adultez": fallecidos_adultez_pasco,
       "persona_mayor": fallecidos_persona_mayor_pasco
      },
      "url": "pasco",
      "provincias": [
          {"name": "Pasco", "positivos": positivos_pasco_pasco,"poblacion": poblacion_pasco_pasco , "hombres_infectados": positivos_hombres_pasco_pasco,"mujeres_infectados": positivos_mujeres_pasco_pasco, "fallecidos": fallecidos_pasco_pasco, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_pasco_pasco,
       "infancia": fallecidos_infancia_pasco_pasco,
       "adolescencia": fallecidos_adolescencia_pasco_pasco,
       "juventud": fallecidos_juventud_pasco_pasco,
       "adultez": fallecidos_adultez_pasco_pasco,
       "persona_mayor": fallecidos_persona_mayor_pasco_pasco
      }},

          {"name": "Daniel Alcides Carrion", "positivos": positivos_pasco_daniel_alcide_carrion,"poblacion": poblacion_pasco_daniel_alcide_carrion , "hombres_infectados": positivos_hombres_pasco_daniel_alcide_carrion,"mujeres_infectados": positivos_mujeres_pasco_daniel_alcide_carrion, "fallecidos": fallecidos_pasco_daniel_alcide_carrion, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_pasco_daniel_alcide_carrion,
       "infancia": fallecidos_infancia_pasco_daniel_alcide_carrion,
       "adolescencia": fallecidos_adolescencia_pasco_daniel_alcide_carrion,
       "juventud": fallecidos_juventud_pasco_daniel_alcide_carrion,
       "adultez": fallecidos_adultez_pasco_daniel_alcide_carrion,
       "persona_mayor": fallecidos_persona_mayor_pasco_daniel_alcide_carrion
      }},

          {"name": "Oxapampa", "positivos": positivos_pasco_oxapampa,"poblacion": poblacion_pasco_oxapampa , "hombres_infectados": positivos_hombres_pasco_oxapampa,"mujeres_infectados": positivos_mujeres_pasco_oxapampa, "fallecidos": fallecidos_pasco_oxapampa, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_pasco_oxapampa,
       "infancia": fallecidos_infancia_pasco_oxapampa,
       "adolescencia": fallecidos_adolescencia_pasco_oxapampa,
       "juventud": fallecidos_juventud_pasco_oxapampa,
       "adultez": fallecidos_adultez_pasco_oxapampa,
       "persona_mayor": fallecidos_persona_mayor_pasco_oxapampa
      }}

      ]
    },
    {
      "name": "Lima",
      "poblacion": poblacion_lima,
      "positivos": positivos_lima,
      "hombres_infectados": positivos_hombres_lima,
      "mujeres_infectados": positivos_mujeres_lima,
      "fallecidos": fallecidos_lima,
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
          {"name": "Lima", "positivos": positivos_lima_lima,"poblacion": poblacion_lima_lima , "hombres_infectados": positivos_hombres_lima_lima,"mujeres_infectados": positivos_mujeres_lima_lima, "fallecidos": fallecidos_lima_lima, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_lima,
       "infancia": fallecidos_infancia_lima_lima,
       "adolescencia": fallecidos_adolescencia_lima_lima,
       "juventud": fallecidos_juventud_lima_lima,
       "adultez": fallecidos_adultez_lima_lima,
       "persona_mayor": fallecidos_persona_mayor_lima_lima
      }},

          {"name": "Barranca", "positivos": positivos_lima_barranca,"poblacion": poblacion_lima_barranca , "hombres_infectados": positivos_hombres_lima_barranca,"mujeres_infectados": positivos_mujeres_lima_barranca, "fallecidos": fallecidos_lima_barranca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_barranca,
       "infancia": fallecidos_infancia_lima_barranca,
       "adolescencia": fallecidos_adolescencia_lima_barranca,
       "juventud": fallecidos_juventud_lima_barranca,
       "adultez": fallecidos_adultez_lima_barranca,
       "persona_mayor": fallecidos_persona_mayor_lima_barranca
      }},

          {"name": "Cajatambo", "positivos": positivos_lima_cajatambo,"poblacion": poblacion_lima_cajatambo , "hombres_infectados": positivos_hombres_lima_cajatambo,"mujeres_infectados": positivos_mujeres_lima_cajatambo, "fallecidos": fallecidos_lima_cajatambo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_cajatambo,
       "infancia": fallecidos_infancia_lima_cajatambo,
       "adolescencia": fallecidos_adolescencia_lima_cajatambo,
       "juventud": fallecidos_juventud_lima_cajatambo,
       "adultez": fallecidos_adultez_lima_cajatambo,
       "persona_mayor": fallecidos_persona_mayor_lima_cajatambo
      }},

          {"name": "Canta", "positivos": positivos_lima_canta,"poblacion": poblacion_lima_canta , "hombres_infectados": positivos_hombres_lima_canta,"mujeres_infectados": positivos_mujeres_lima_canta, "fallecidos": fallecidos_lima_canta, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_canta,
       "infancia": fallecidos_infancia_lima_canta,
       "adolescencia": fallecidos_adolescencia_lima_canta,
       "juventud": fallecidos_juventud_lima_canta,
       "adultez": fallecidos_adultez_lima_canta,
       "persona_mayor": fallecidos_persona_mayor_lima_canta
      }},

          {"name": "Cañete", "positivos": positivos_lima_canete,"poblacion": poblacion_lima_canete , "hombres_infectados": positivos_hombres_lima_canete,"mujeres_infectados": positivos_mujeres_lima_canete, "fallecidos": fallecidos_lima_canete, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_canete,
       "infancia": fallecidos_infancia_lima_canete,
       "adolescencia": fallecidos_adolescencia_lima_canete,
       "juventud": fallecidos_juventud_lima_canete,
       "adultez": fallecidos_adultez_lima_canete,
       "persona_mayor": fallecidos_persona_mayor_lima_canete
      }},

          {"name": "Huaral", "positivos": positivos_lima_huaral,"poblacion": poblacion_lima_huaral , "hombres_infectados": positivos_hombres_lima_huaral,"mujeres_infectados": positivos_mujeres_lima_huaral, "fallecidos": fallecidos_lima_huaral, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_huaral,
       "infancia": fallecidos_infancia_lima_huaral,
       "adolescencia": fallecidos_adolescencia_lima_huaral,
       "juventud": fallecidos_juventud_lima_huaral,
       "adultez": fallecidos_adultez_lima_huaral,
       "persona_mayor": fallecidos_persona_mayor_lima_huaral
      }},

          {"name": "Huarochiri", "positivos": positivos_lima_huarochiri,"poblacion": poblacion_lima_huarochiri , "hombres_infectados": positivos_hombres_lima_huarochiri,"mujeres_infectados": positivos_mujeres_lima_huarochiri, "fallecidos": fallecidos_lima_huarochiri, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_huarochiri,
       "infancia": fallecidos_infancia_lima_huarochiri,
       "adolescencia": fallecidos_adolescencia_lima_huarochiri,
       "juventud": fallecidos_juventud_lima_huarochiri,
       "adultez": fallecidos_adultez_lima_huarochiri,
       "persona_mayor": fallecidos_persona_mayor_lima_huarochiri
      }},

          {"name": "Huaura", "positivos": positivos_lima_huaura,"poblacion": poblacion_lima_huaura , "hombres_infectados": positivos_hombres_lima_huaura,"mujeres_infectados": positivos_mujeres_lima_huaura, "fallecidos": fallecidos_lima_huaura, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_huaura,
       "infancia": fallecidos_infancia_lima_huaura,
       "adolescencia": fallecidos_adolescencia_lima_huaura,
       "juventud": fallecidos_juventud_lima_huaura,
       "adultez": fallecidos_adultez_lima_huaura,
       "persona_mayor": fallecidos_persona_mayor_lima_huaura
      }},

          {"name": "Oyon", "positivos": positivos_lima_oyon,"poblacion": poblacion_lima_oyon , "hombres_infectados": positivos_hombres_lima_oyon,"mujeres_infectados": positivos_mujeres_lima_oyon, "fallecidos": fallecidos_lima_oyon, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_oyon,
       "infancia": fallecidos_infancia_lima_oyon,
       "adolescencia": fallecidos_adolescencia_lima_oyon,
       "juventud": fallecidos_juventud_lima_oyon,
       "adultez": fallecidos_adultez_lima_oyon,
       "persona_mayor": fallecidos_persona_mayor_lima_oyon
      }},

          {"name": "Yauyos", "positivos": positivos_lima_yauyos,"poblacion": poblacion_lima_yauyos , "hombres_infectados": positivos_hombres_lima_yauyos,"mujeres_infectados": positivos_mujeres_lima_yauyos, "fallecidos": fallecidos_lima_yauyos, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_lima_yauyos,
       "infancia": fallecidos_infancia_lima_yauyos,
       "adolescencia": fallecidos_adolescencia_lima_yauyos,
       "juventud": fallecidos_juventud_lima_yauyos,
       "adultez": fallecidos_adultez_lima_yauyos,
       "persona_mayor": fallecidos_persona_mayor_lima_yauyos
      }}
      ]
    },
    {
      "name": "Junin",
      "poblacion": poblacion_junin,
      "positivos": positivos_junin,
      "hombres_infectados": positivos_hombres_junin,
      "mujeres_infectados": positivos_mujeres_junin,
      "fallecidos": fallecidos_junin,
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
          {"name": "Huancayo", "positivos": positivos_junin_huancayo,"poblacion": poblacion_junin_huancayo , "hombres_infectados": positivos_hombres_junin_huancayo,"mujeres_infectados": positivos_mujeres_junin_huancayo, "fallecidos": fallecidos_junin_huancayo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_huancayo,
       "infancia": fallecidos_infancia_junin_huancayo,
       "adolescencia": fallecidos_adolescencia_junin_huancayo,
       "juventud": fallecidos_juventud_junin_huancayo,
       "adultez": fallecidos_adultez_junin_huancayo,
       "persona_mayor": fallecidos_persona_mayor_junin_huancayo
      }},

          {"name": "Concepcion", "positivos": positivos_junin_concepcion,"poblacion": poblacion_junin_concepcion , "hombres_infectados": positivos_hombres_junin_concepcion,"mujeres_infectados": positivos_mujeres_junin_concepcion, "fallecidos": fallecidos_junin_concepcion, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_concepcion,
       "infancia": fallecidos_infancia_junin_concepcion,
       "adolescencia": fallecidos_adolescencia_junin_concepcion,
       "juventud": fallecidos_juventud_junin_concepcion,
       "adultez": fallecidos_adultez_junin_concepcion,
       "persona_mayor": fallecidos_persona_mayor_junin_concepcion
      }},

          {"name": "Chanchamayo", "positivos": positivos_junin_chanchamayo,"poblacion": poblacion_junin_chanchamayo , "hombres_infectados": positivos_hombres_junin_chanchamayo,"mujeres_infectados": positivos_mujeres_junin_chanchamayo, "fallecidos": fallecidos_junin_chanchamayo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_chanchamayo,
       "infancia": fallecidos_infancia_junin_chanchamayo,
       "adolescencia": fallecidos_adolescencia_junin_chanchamayo,
       "juventud": fallecidos_juventud_junin_chanchamayo,
       "adultez": fallecidos_adultez_junin_chanchamayo,
       "persona_mayor": fallecidos_persona_mayor_junin_chanchamayo
      }},

          {"name": "Jauja", "positivos": positivos_junin_jauja,"poblacion": poblacion_junin_jauja , "hombres_infectados": positivos_hombres_junin_jauja,"mujeres_infectados": positivos_mujeres_junin_jauja, "fallecidos": fallecidos_junin_jauja, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_jauja,
       "infancia": fallecidos_infancia_junin_jauja,
       "adolescencia": fallecidos_adolescencia_junin_jauja,
       "juventud": fallecidos_juventud_junin_jauja,
       "adultez": fallecidos_adultez_junin_jauja,
       "persona_mayor": fallecidos_persona_mayor_junin_jauja
      }},

          {"name": "Junin", "positivos": positivos_junin_junin,"poblacion": poblacion_junin_junin , "hombres_infectados": positivos_hombres_junin_junin,"mujeres_infectados": positivos_mujeres_junin_junin, "fallecidos": fallecidos_junin_junin, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_junin,
       "infancia": fallecidos_infancia_junin_junin,
       "adolescencia": fallecidos_adolescencia_junin_junin,
       "juventud": fallecidos_juventud_junin_junin,
       "adultez": fallecidos_adultez_junin_junin,
       "persona_mayor": fallecidos_persona_mayor_junin_junin
      }},

          {"name": "Satipo", "positivos": positivos_junin_satipo,"poblacion": poblacion_junin_satipo , "hombres_infectados": positivos_hombres_junin_satipo,"mujeres_infectados": positivos_mujeres_junin_satipo, "fallecidos": fallecidos_junin_satipo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_satipo,
       "infancia": fallecidos_infancia_junin_satipo,
       "adolescencia": fallecidos_adolescencia_junin_satipo,
       "juventud": fallecidos_juventud_junin_satipo,
       "adultez": fallecidos_adultez_junin_satipo,
       "persona_mayor": fallecidos_persona_mayor_junin_satipo
      }},

          {"name": "Tarma", "positivos": positivos_junin_tarma,"poblacion": poblacion_junin_tarma , "hombres_infectados": positivos_hombres_junin_tarma,"mujeres_infectados": positivos_mujeres_junin_tarma, "fallecidos": fallecidos_junin_tarma, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_tarma,
       "infancia": fallecidos_infancia_junin_tarma,
       "adolescencia": fallecidos_adolescencia_junin_tarma,
       "juventud": fallecidos_juventud_junin_tarma,
       "adultez": fallecidos_adultez_junin_tarma,
       "persona_mayor": fallecidos_persona_mayor_junin_tarma
      }},

          {"name": "Yauli", "positivos": positivos_junin_yauli,"poblacion": poblacion_junin_yauli , "hombres_infectados": positivos_hombres_junin_yauli,"mujeres_infectados": positivos_mujeres_junin_yauli, "fallecidos": fallecidos_junin_yauli, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_yauli,
       "infancia": fallecidos_infancia_junin_yauli,
       "adolescencia": fallecidos_adolescencia_junin_yauli,
       "juventud": fallecidos_juventud_junin_yauli,
       "adultez": fallecidos_adultez_junin_yauli,
       "persona_mayor": fallecidos_persona_mayor_junin_yauli
      }},

          {"name": "Chupaca", "positivos": positivos_junin_chupaca,"poblacion": poblacion_junin_chupaca , "hombres_infectados": positivos_hombres_junin_chupaca,"mujeres_infectados": positivos_mujeres_junin_chupaca, "fallecidos": fallecidos_junin_chupaca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_junin_chupaca,
       "infancia": fallecidos_infancia_junin_chupaca,
       "adolescencia": fallecidos_adolescencia_junin_chupaca,
       "juventud": fallecidos_juventud_junin_chupaca,
       "adultez": fallecidos_adultez_junin_chupaca,
       "persona_mayor": fallecidos_persona_mayor_junin_chupaca
      }}
      ]
    },
    {
      "name": "Huancavelica",
      "poblacion": poblacion_huancavelica,
      "positivos": positivos_huancavelica,
      "hombres_infectados": positivos_hombres_huancavelica,
      "mujeres_infectados": positivos_mujeres_huancavelica,
      "fallecidos": fallecidos_huancavelica,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica,
       "infancia": fallecidos_infancia_huancavelica,
       "adolescencia": fallecidos_adolescencia_huancavelica,
       "juventud": fallecidos_juventud_huancavelica,
       "adultez": fallecidos_adultez_huancavelica,
       "persona_mayor": fallecidos_persona_mayor_huancavelica
      },
      "url": "huancavelica",
      "provincias": [
          {"name": "Huancavelica", "positivos": positivos_huancavelica_huancavelica, "poblacion": poblacion_huancavelica_huancavelica , "hombres_infectados": positivos_hombres_huancavelica_huancavelica,"mujeres_infectados": positivos_mujeres_huancavelica_huancavelica, "fallecidos": fallecidos_huancavelica_huancavelica, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_huancavelica,
       "infancia": fallecidos_infancia_huancavelica_huancavelica,
       "adolescencia": fallecidos_adolescencia_huancavelica_huancavelica,
       "juventud": fallecidos_juventud_huancavelica_huancavelica,
       "adultez": fallecidos_adultez_huancavelica_huancavelica,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_huancavelica
      }},

          {"name": "Acobamba", "positivos": positivos_huancavelica_acobamba,"poblacion": poblacion_huancavelica_acobamba , "hombres_infectados": positivos_hombres_huancavelica_acobamba,"mujeres_infectados": positivos_mujeres_huancavelica_acobamba, "fallecidos": fallecidos_huancavelica_acobamba, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_acobamba,
       "infancia": fallecidos_infancia_huancavelica_acobamba,
       "adolescencia": fallecidos_adolescencia_huancavelica_acobamba,
       "juventud": fallecidos_juventud_huancavelica_acobamba,
       "adultez": fallecidos_adultez_huancavelica_acobamba,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_acobamba
      }},

          {"name": "Angaraes", "positivos": positivos_huancavelica_angaraes,"poblacion": poblacion_huancavelica_angaraes , "hombres_infectados": positivos_hombres_huancavelica_angaraes,"mujeres_infectados": positivos_mujeres_huancavelica_angaraes, "fallecidos": fallecidos_huancavelica_angaraes, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_angaraes,
       "infancia": fallecidos_infancia_huancavelica_angaraes,
       "adolescencia": fallecidos_adolescencia_huancavelica_angaraes,
       "juventud": fallecidos_juventud_huancavelica_angaraes,
       "adultez": fallecidos_adultez_huancavelica_angaraes,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_angaraes
      }},

          {"name": "Castrovirreyna", "positivos": positivos_huancavelica_castrovirreyna, "poblacion": poblacion_huancavelica_castrovirreyna , "hombres_infectados": positivos_hombres_huancavelica_castrovirreyna,"mujeres_infectados": positivos_mujeres_huancavelica_castrovirreyna, "fallecidos": fallecidos_huancavelica_castrovirreyna, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_castrovirreyna,
       "infancia": fallecidos_infancia_huancavelica_castrovirreyna,
       "adolescencia": fallecidos_adolescencia_huancavelica_castrovirreyna,
       "juventud": fallecidos_juventud_huancavelica_castrovirreyna,
       "adultez": fallecidos_adultez_huancavelica_castrovirreyna,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_castrovirreyna
      }},

          {"name": "Churcampa", "positivos": positivos_huancavelica_churcampa,"poblacion": poblacion_huancavelica_churcampa , "hombres_infectados": positivos_hombres_huancavelica_churcampa,"mujeres_infectados": positivos_mujeres_huancavelica_churcampa, "fallecidos": fallecidos_huancavelica_churcampa, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_churcampa,
       "infancia": fallecidos_infancia_huancavelica_churcampa,
       "adolescencia": fallecidos_adolescencia_huancavelica_churcampa,
       "juventud": fallecidos_juventud_huancavelica_churcampa,
       "adultez": fallecidos_adultez_huancavelica_churcampa,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_churcampa
      }},

          {"name": "Huaytara", "positivos": positivos_huancavelica_huaytara,"poblacion": poblacion_huancavelica_huaytara , "hombres_infectados": positivos_hombres_huancavelica_huaytara,"mujeres_infectados": positivos_mujeres_huancavelica_huaytara, "fallecidos": fallecidos_huancavelica_huaytara, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_huaytara,
       "infancia": fallecidos_infancia_huancavelica_huaytara,
       "adolescencia": fallecidos_adolescencia_huancavelica_huaytara,
       "juventud": fallecidos_juventud_huancavelica_huaytara,
       "adultez": fallecidos_adultez_huancavelica_huaytara,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_huaytara
      }},

          {"name": "Tayacaja", "positivos": positivos_huancavelica_tayacaja,"poblacion": poblacion_huancavelica_tayacaja , "hombres_infectados": positivos_hombres_huancavelica_tayacaja,"mujeres_infectados": positivos_mujeres_huancavelica_tayacaja, "fallecidos": fallecidos_huancavelica_tayacaja, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_huancavelica_tayacaja,
       "infancia": fallecidos_infancia_huancavelica_tayacaja,
       "adolescencia": fallecidos_adolescencia_huancavelica_tayacaja,
       "juventud": fallecidos_juventud_huancavelica_tayacaja,
       "adultez": fallecidos_adultez_huancavelica_tayacaja,
       "persona_mayor": fallecidos_persona_mayor_huancavelica_tayacaja
      }}
      ]
    },
    {
      "name": "Ica",
      "poblacion": poblacion_ica,
      "positivos": positivos_ica,
      "hombres_infectados": positivos_hombres_ica,
      "mujeres_infectados": positivos_mujeres_ica,
      "fallecidos": fallecidos_ica,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica,
       "infancia": fallecidos_infancia_ica,
       "adolescencia": fallecidos_adolescencia_ica,
       "juventud": fallecidos_juventud_ica,
       "adultez": fallecidos_adultez_ica,
       "persona_mayor": fallecidos_persona_mayor_ica
      },
      "url": "ica",
      "provincias": [
          {"name": "Ica", "positivos": positivos_ica_ica, "poblacion": poblacion_ica_ica , "hombres_infectados": positivos_hombres_ica_ica,"mujeres_infectados": positivos_mujeres_ica_ica, "fallecidos": fallecidos_ica_ica, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica_ica,
       "infancia": fallecidos_infancia_ica_ica,
       "adolescencia": fallecidos_adolescencia_ica_ica,
       "juventud": fallecidos_juventud_ica_ica,
       "adultez": fallecidos_adultez_ica_ica,
       "persona_mayor": fallecidos_persona_mayor_ica_ica
      }},
          
          {"name": "Chincha", "positivos": positivos_ica_chincha,"poblacion": poblacion_ica_chincha , "hombres_infectados": positivos_hombres_ica_chincha,"mujeres_infectados": positivos_mujeres_ica_chincha, "fallecidos": fallecidos_ica_chincha, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica_chincha,
       "infancia": fallecidos_infancia_ica_chincha,
       "adolescencia": fallecidos_adolescencia_ica_chincha,
       "juventud": fallecidos_juventud_ica_chincha,
       "adultez": fallecidos_adultez_ica_chincha,
       "persona_mayor": fallecidos_persona_mayor_ica_chincha
      }},

          {"name": "Nazca", "positivos": positivos_ica_nazca,"poblacion": poblacion_ica_nazca , "hombres_infectados": positivos_hombres_ica_nazca,"mujeres_infectados": positivos_mujeres_ica_nazca, "fallecidos": fallecidos_ica_nazca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica_nazca,
       "infancia": fallecidos_infancia_ica_nazca,
       "adolescencia": fallecidos_adolescencia_ica_nazca,
       "juventud": fallecidos_juventud_ica_nazca,
       "adultez": fallecidos_adultez_ica_nazca,
       "persona_mayor": fallecidos_persona_mayor_ica_nazca
      }},

          {"name": "Palpa", "positivos": positivos_ica_palpa,"poblacion": poblacion_ica_palpa , "hombres_infectados": positivos_hombres_ica_palpa,"mujeres_infectados": positivos_mujeres_ica_palpa, "fallecidos": fallecidos_ica_palpa, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica_palpa,
       "infancia": fallecidos_infancia_ica_palpa,
       "adolescencia": fallecidos_adolescencia_ica_palpa,
       "juventud": fallecidos_juventud_ica_palpa,
       "adultez": fallecidos_adultez_ica_palpa,
       "persona_mayor": fallecidos_persona_mayor_ica_palpa
      }},

          {"name": "Pisco", "positivos": positivos_ica_pisco,"poblacion": poblacion_ica_pisco , "hombres_infectados": positivos_hombres_ica_pisco,"mujeres_infectados": positivos_mujeres_ica_pisco, "fallecidos": fallecidos_ica_pisco, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ica_pisco,
       "infancia": fallecidos_infancia_ica_pisco,
       "adolescencia": fallecidos_adolescencia_ica_pisco,
       "juventud": fallecidos_juventud_ica_pisco,
       "adultez": fallecidos_adultez_ica_pisco,
       "persona_mayor": fallecidos_persona_mayor_ica_pisco
      }},
      ]
    },
    {
      "name": "Ayacucho",
      "poblacion": poblacion_ayacucho,
      "positivos": positivos_ayacucho,
      "hombres_infectados": positivos_hombres_ayacucho,
      "mujeres_infectados": positivos_mujeres_ayacucho,
      "fallecidos": fallecidos_ayacucho,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho,
       "infancia": fallecidos_infancia_ayacucho,
       "adolescencia": fallecidos_adolescencia_ayacucho,
       "juventud": fallecidos_juventud_ayacucho,
       "adultez": fallecidos_adultez_ayacucho,
       "persona_mayor": fallecidos_persona_mayor_ayacucho
      },
      "url": "ayacucho",
      "provincias": [
          {"name": "Huamanga", "positivos": positivos_ayacucho_huamanga,"poblacion": poblacion_ayacucho_huamanga , "hombres_infectados": positivos_hombres_ayacucho_huamanga,"mujeres_infectados": positivos_mujeres_ayacucho_huamanga, "fallecidos": fallecidos_ayacucho_huamanga, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_huamanga,
       "infancia": fallecidos_infancia_ayacucho_huamanga,
       "adolescencia": fallecidos_adolescencia_ayacucho_huamanga,
       "juventud": fallecidos_juventud_ayacucho_huamanga,
       "adultez": fallecidos_adultez_ayacucho_huamanga,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_huamanga
      }},

          {"name": "Cangallo", "positivos": positivos_ayacucho_cangallo,"poblacion": poblacion_ayacucho_cangallo , "hombres_infectados": positivos_hombres_ayacucho_cangallo,"mujeres_infectados": positivos_mujeres_ayacucho_cangallo, "fallecidos": fallecidos_ayacucho_cangallo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_cangallo,
       "infancia": fallecidos_infancia_ayacucho_cangallo,
       "adolescencia": fallecidos_adolescencia_ayacucho_cangallo,
       "juventud": fallecidos_juventud_ayacucho_cangallo,
       "adultez": fallecidos_adultez_ayacucho_cangallo,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_cangallo
      }},

          {"name": "Huanca Sancos", "positivos": positivos_ayacucho_huanca_sancos,"poblacion": poblacion_ayacucho_huanca_sancos , "hombres_infectados": positivos_hombres_ayacucho_huanca_sancos,"mujeres_infectados": positivos_mujeres_ayacucho_huanca_sancos, "fallecidos": fallecidos_ayacucho_huanca_sancos, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_huanca_sancos,
       "infancia": fallecidos_infancia_ayacucho_huanca_sancos,
       "adolescencia": fallecidos_adolescencia_ayacucho_huanca_sancos,
       "juventud": fallecidos_juventud_ayacucho_huanca_sancos,
       "adultez": fallecidos_adultez_ayacucho_huanca_sancos,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_huanca_sancos
      }},

          {"name": "Huanta", "positivos": positivos_ayacucho_huanta,"poblacion": poblacion_ayacucho_huanta , "hombres_infectados": positivos_hombres_ayacucho_huanta,"mujeres_infectados": positivos_mujeres_ayacucho_huanta, "fallecidos": fallecidos_ayacucho_huanta, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_huanta,
       "infancia": fallecidos_infancia_ayacucho_huanta,
       "adolescencia": fallecidos_adolescencia_ayacucho_huanta,
       "juventud": fallecidos_juventud_ayacucho_huanta,
       "adultez": fallecidos_adultez_ayacucho_huanta,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_huanta
      }},

          {"name": "La Mar", "positivos": positivos_ayacucho_mar,"poblacion": poblacion_ayacucho_mar , "hombres_infectados": positivos_hombres_ayacucho_mar,"mujeres_infectados": positivos_mujeres_ayacucho_mar, "fallecidos": fallecidos_ayacucho_mar, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_mar,
       "infancia": fallecidos_infancia_ayacucho_mar,
       "adolescencia": fallecidos_adolescencia_ayacucho_mar,
       "juventud": fallecidos_juventud_ayacucho_mar,
       "adultez": fallecidos_adultez_ayacucho_mar,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_mar
      }},

          {"name": "Lucanas", "positivos": positivos_ayacucho_lucanas,"poblacion": poblacion_ayacucho_lucanas , "hombres_infectados": positivos_hombres_ayacucho_lucanas,"mujeres_infectados": positivos_mujeres_ayacucho_lucanas, "fallecidos": fallecidos_ayacucho_lucanas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_lucanas,
       "infancia": fallecidos_infancia_ayacucho_lucanas,
       "adolescencia": fallecidos_adolescencia_ayacucho_lucanas,
       "juventud": fallecidos_juventud_ayacucho_lucanas,
       "adultez": fallecidos_adultez_ayacucho_lucanas,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_lucanas
      }},

          {"name": "Parinacochas", "positivos": positivos_ayacucho_parinacochas,"poblacion": poblacion_ayacucho_parinacochas , "hombres_infectados": positivos_hombres_ayacucho_parinacochas,"mujeres_infectados": positivos_mujeres_ayacucho_parinacochas, "fallecidos": fallecidos_ayacucho_parinacochas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_parinacochas,
       "infancia": fallecidos_infancia_ayacucho_parinacochas,
       "adolescencia": fallecidos_adolescencia_ayacucho_parinacochas,
       "juventud": fallecidos_juventud_ayacucho_parinacochas,
       "adultez": fallecidos_adultez_ayacucho_parinacochas,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_parinacochas
      }},

          {"name": "Paucar del Sara Sara", "positivos": positivos_ayacucho_paucar,"poblacion": poblacion_ayacucho_paucar , "hombres_infectados": positivos_hombres_ayacucho_paucar,"mujeres_infectados": positivos_mujeres_ayacucho_paucar, "fallecidos": fallecidos_ayacucho_paucar, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_paucar,
       "infancia": fallecidos_infancia_ayacucho_paucar,
       "adolescencia": fallecidos_adolescencia_ayacucho_paucar,
       "juventud": fallecidos_juventud_ayacucho_paucar,
       "adultez": fallecidos_adultez_ayacucho_paucar,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_paucar
      }},

          {"name": "Sucre", "positivos": positivos_ayacucho_sucre,"poblacion": poblacion_ayacucho_sucre , "hombres_infectados": positivos_hombres_ayacucho_sucre,"mujeres_infectados": positivos_mujeres_ayacucho_sucre, "fallecidos": fallecidos_ayacucho_sucre, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_sucre,
       "infancia": fallecidos_infancia_ayacucho_sucre,
       "adolescencia": fallecidos_adolescencia_ayacucho_sucre,
       "juventud": fallecidos_juventud_ayacucho_sucre,
       "adultez": fallecidos_adultez_ayacucho_sucre,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_sucre
      }},

          {"name": "Victor Fajardo", "positivos": positivos_ayacucho_victor_fajardo,"poblacion": poblacion_ayacucho_victor_fajardo , "hombres_infectados": positivos_hombres_ayacucho_victor_fajardo,"mujeres_infectados": positivos_mujeres_ayacucho_victor_fajardo, "fallecidos": fallecidos_ayacucho_victor_fajardo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_victor_fajardo,
       "infancia": fallecidos_infancia_ayacucho_victor_fajardo,
       "adolescencia": fallecidos_adolescencia_ayacucho_victor_fajardo,
       "juventud": fallecidos_juventud_ayacucho_victor_fajardo,
       "adultez": fallecidos_adultez_ayacucho_victor_fajardo,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_victor_fajardo
      }},

          {"name": "Vilcas Huaman", "positivos": positivos_ayacucho_vilcas_huaman,"poblacion": poblacion_ayacucho_vilcas_huaman , "hombres_infectados": positivos_hombres_ayacucho_vilcas_huaman,"mujeres_infectados": positivos_mujeres_ayacucho_vilcas_huaman, "fallecidos": fallecidos_ayacucho_vilcas_huaman, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_vilcas_huaman,
       "infancia": fallecidos_infancia_ayacucho_vilcas_huaman,
       "adolescencia": fallecidos_adolescencia_ayacucho_vilcas_huaman,
       "juventud": fallecidos_juventud_ayacucho_vilcas_huaman,
       "adultez": fallecidos_adultez_ayacucho_vilcas_huaman,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_vilcas_huaman
      }}
      ]
    },
    {
      "name": "Apurimac",
      "poblacion": poblacion_apurimac,
      "positivos": positivos_apurimac,
      "hombres_infectados": positivos_hombres_apurimac,
      "mujeres_infectados": positivos_mujeres_apurimac,
      "fallecidos": fallecidos_apurimac,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac,
       "infancia": fallecidos_infancia_apurimac,
       "adolescencia": fallecidos_adolescencia_apurimac,
       "juventud": fallecidos_juventud_apurimac,
       "adultez": fallecidos_adultez_apurimac,
       "persona_mayor": fallecidos_persona_mayor_apurimac
      },
      "url": "apurimac",
      "provincias": [
          {"name": "Abancay", "positivos": positivos_apurimac_abancay,"poblacion": poblacion_apurimac_abancay , "hombres_infectados": positivos_hombres_apurimac_abancay,"mujeres_infectados": positivos_mujeres_apurimac_abancay, "fallecidos": fallecidos_apurimac_abancay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_abancay,
       "infancia": fallecidos_infancia_apurimac_abancay,
       "adolescencia": fallecidos_adolescencia_apurimac_abancay,
       "juventud": fallecidos_juventud_apurimac_abancay,
       "adultez": fallecidos_adultez_apurimac_abancay,
       "persona_mayor": fallecidos_persona_mayor_apurimac_abancay,
      }},

          {"name": "Andahuaylas", "positivos": positivos_apurimac_andahuaylas,"poblacion": poblacion_apurimac_andahuaylas , "hombres_infectados": positivos_hombres_apurimac_andahuaylas,"mujeres_infectados": positivos_mujeres_apurimac_andahuaylas, "fallecidos": fallecidos_apurimac_andahuaylas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_andahuaylas,
       "infancia": fallecidos_infancia_apurimac_andahuaylas,
       "adolescencia": fallecidos_adolescencia_apurimac_andahuaylas,
       "juventud": fallecidos_juventud_apurimac_andahuaylas,
       "adultez": fallecidos_adultez_apurimac_andahuaylas,
       "persona_mayor": fallecidos_persona_mayor_apurimac_andahuaylas
      }},

          {"name": "Antabamba", "positivos": positivos_apurimac_antabamba,"poblacion": poblacion_apurimac_antabamba , "hombres_infectados": positivos_hombres_apurimac_antabamba,"mujeres_infectados": positivos_mujeres_apurimac_antabamba, "fallecidos": fallecidos_apurimac_antabamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_antabamba,
       "infancia": fallecidos_infancia_apurimac_antabamba,
       "adolescencia": fallecidos_adolescencia_apurimac_antabamba,
       "juventud": fallecidos_juventud_apurimac_antabamba,
       "adultez": fallecidos_adultez_apurimac_antabamba,
       "persona_mayor": fallecidos_persona_mayor_apurimac_antabamba
      }},

          {"name": "Aymaraes", "positivos": positivos_apurimac_aymaraes,"poblacion": poblacion_apurimac_aymaraes , "hombres_infectados": positivos_hombres_apurimac_aymaraes,"mujeres_infectados": positivos_mujeres_apurimac_aymaraes, "fallecidos": fallecidos_apurimac_aymaraes, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_aymaraes,
       "infancia": fallecidos_infancia_apurimac_aymaraes,
       "adolescencia": fallecidos_adolescencia_apurimac_aymaraes,
       "juventud": fallecidos_juventud_apurimac_aymaraes,
       "adultez": fallecidos_adultez_apurimac_aymaraes,
       "persona_mayor": fallecidos_persona_mayor_apurimac_aymaraes
      }},

          {"name": "Cotabambas", "positivos": positivos_apurimac_cotabambas,"poblacion": poblacion_apurimac_cotabambas , "hombres_infectados": positivos_hombres_apurimac_cotabambas,"mujeres_infectados": positivos_mujeres_apurimac_cotabambas, "fallecidos": fallecidos_apurimac_cotabambas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_cotabambas,
       "infancia": fallecidos_infancia_apurimac_cotabambas,
       "adolescencia": fallecidos_adolescencia_apurimac_cotabambas,
       "juventud": fallecidos_juventud_apurimac_cotabambas,
       "adultez": fallecidos_adultez_apurimac_cotabambas,
       "persona_mayor": fallecidos_persona_mayor_apurimac_cotabambas
      }},

          {"name": "Chincheros", "positivos": positivos_apurimac_chincheros,"poblacion": poblacion_apurimac_chincheros , "hombres_infectados": positivos_hombres_apurimac_chincheros,"mujeres_infectados": positivos_mujeres_apurimac_chincheros, "fallecidos": fallecidos_apurimac_chincheros, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_chincheros,
       "infancia": fallecidos_infancia_apurimac_chincheros,
       "adolescencia": fallecidos_adolescencia_apurimac_chincheros,
       "juventud": fallecidos_juventud_apurimac_chincheros,
       "adultez": fallecidos_adultez_apurimac_chincheros,
       "persona_mayor": fallecidos_persona_mayor_apurimac_chincheros
      }},

          {"name": "Grau", "positivos": positivos_apurimac_grau,"poblacion": poblacion_apurimac_grau , "hombres_infectados": positivos_hombres_apurimac_grau,"mujeres_infectados": positivos_mujeres_apurimac_grau, "fallecidos": fallecidos_apurimac_grau, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_grau,
       "infancia": fallecidos_infancia_apurimac_grau,
       "adolescencia": fallecidos_adolescencia_apurimac_grau,
       "juventud": fallecidos_juventud_apurimac_grau,
       "adultez": fallecidos_adultez_apurimac_grau,
       "persona_mayor": fallecidos_persona_mayor_apurimac_grau
      }}
      ]
    },
    {
      "name": "Cusco",
      "poblacion": poblacion_cusco,
      "positivos": positivos_cusco,
      "hombres_infectados": positivos_hombres_cusco,
      "mujeres_infectados": positivos_mujeres_cusco,
      "fallecidos": fallecidos_cusco,
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
        {"name": "Cusco", "positivos": positivos_cusco_cusco,"poblacion": poblacion_cusco_cusco , "hombres_infectados": positivos_hombres_cusco_cusco,"mujeres_infectados": positivos_mujeres_cusco_cusco, "fallecidos": fallecidos_cusco_cusco, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_cusco,
       "infancia": fallecidos_infancia_cusco_cusco,
       "adolescencia": fallecidos_adolescencia_cusco_cusco,
       "juventud": fallecidos_juventud_cusco_cusco,
       "adultez": fallecidos_adultez_cusco_cusco,
       "persona_mayor": fallecidos_persona_mayor_cusco_cusco
      }},

        {"name": "Acomayo", "positivos": positivos_cusco_acomayo,"poblacion": poblacion_cusco_acomayo , "hombres_infectados": positivos_hombres_cusco_acomayo,"mujeres_infectados": positivos_mujeres_cusco_acomayo, "fallecidos": fallecidos_cusco_acomayo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_acomayo,
       "infancia": fallecidos_infancia_cusco_acomayo,
       "adolescencia": fallecidos_adolescencia_cusco_acomayo,
       "juventud": fallecidos_juventud_cusco_acomayo,
       "adultez": fallecidos_adultez_cusco_acomayo,
       "persona_mayor": fallecidos_persona_mayor_cusco_acomayo
      }},

        {"name": "Anta", "positivos": positivos_cusco_anta,"poblacion": poblacion_cusco_anta , "hombres_infectados": positivos_hombres_cusco_anta,"mujeres_infectados": positivos_mujeres_cusco_anta, "fallecidos": fallecidos_cusco_anta, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_anta,
       "infancia": fallecidos_infancia_cusco_anta,
       "adolescencia": fallecidos_adolescencia_cusco_anta,
       "juventud": fallecidos_juventud_cusco_anta,
       "adultez": fallecidos_adultez_cusco_anta,
       "persona_mayor": fallecidos_persona_mayor_cusco_anta
      }},

        {"name": "Calca", "positivos": positivos_cusco_calca,"poblacion": poblacion_cusco_calca , "hombres_infectados": positivos_hombres_cusco_calca,"mujeres_infectados": positivos_mujeres_cusco_calca, "fallecidos": fallecidos_cusco_calca, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_calca,
       "infancia": fallecidos_infancia_cusco_calca,
       "adolescencia": fallecidos_adolescencia_cusco_calca,
       "juventud": fallecidos_juventud_cusco_calca,
       "adultez": fallecidos_adultez_cusco_calca,
       "persona_mayor": fallecidos_persona_mayor_cusco_calca
      }},

        {"name": "Canas", "positivos": positivos_cusco_canas,"poblacion": poblacion_cusco_canas , "hombres_infectados": positivos_hombres_cusco_canas,"mujeres_infectados": positivos_mujeres_cusco_canas, "fallecidos": fallecidos_cusco_canas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_canas,
       "infancia": fallecidos_infancia_cusco_canas,
       "adolescencia": fallecidos_adolescencia_cusco_canas,
       "juventud": fallecidos_juventud_cusco_canas,
       "adultez": fallecidos_adultez_cusco_canas,
       "persona_mayor": fallecidos_persona_mayor_cusco_canas
      }},

        {"name": "Canchis", "positivos": positivos_cusco_canchis,"poblacion": poblacion_cusco_canchis , "hombres_infectados": positivos_hombres_cusco_canchis,"mujeres_infectados": positivos_mujeres_cusco_canchis, "fallecidos": fallecidos_cusco_canchis, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_canchis,
       "infancia": fallecidos_infancia_cusco_canchis,
       "adolescencia": fallecidos_adolescencia_cusco_canchis,
       "juventud": fallecidos_juventud_cusco_canchis,
       "adultez": fallecidos_adultez_cusco_canchis,
       "persona_mayor": fallecidos_persona_mayor_cusco_canchis
      }},

        {"name": "Chumbivilcas", "positivos": positivos_cusco_chumbivilcas,"poblacion": poblacion_cusco_chumbivilcas , "hombres_infectados": positivos_hombres_cusco_chumbivilcas,"mujeres_infectados": positivos_mujeres_cusco_chumbivilcas, "fallecidos": fallecidos_cusco_chumbivilcas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_chumbivilcas,
       "infancia": fallecidos_infancia_cusco_chumbivilcas,
       "adolescencia": fallecidos_adolescencia_cusco_chumbivilcas,
       "juventud": fallecidos_juventud_cusco_chumbivilcas,
       "adultez": fallecidos_adultez_cusco_chumbivilcas,
       "persona_mayor": fallecidos_persona_mayor_cusco_chumbivilcas
      }},

        {"name": "Espinar", "positivos": positivos_cusco_espinar,"poblacion": poblacion_cusco_espinar , "hombres_infectados": positivos_hombres_cusco_espinar,"mujeres_infectados": positivos_mujeres_cusco_espinar, "fallecidos": fallecidos_cusco_espinar, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_espinar,
       "infancia": fallecidos_infancia_cusco_espinar,
       "adolescencia": fallecidos_adolescencia_cusco_espinar,
       "juventud": fallecidos_juventud_cusco_espinar,
       "adultez": fallecidos_adultez_cusco_espinar,
       "persona_mayor": fallecidos_persona_mayor_cusco_espinar
      }},

        {"name": "La Convencion", "positivos": positivos_cusco_convencion,"poblacion": poblacion_cusco_convencion , "hombres_infectados": positivos_hombres_cusco_convencion,"mujeres_infectados": positivos_mujeres_cusco_convencion, "fallecidos": fallecidos_cusco_convencion, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_convencion,
       "infancia": fallecidos_infancia_cusco_convencion,
       "adolescencia": fallecidos_adolescencia_cusco_convencion,
       "juventud": fallecidos_juventud_cusco_convencion,
       "adultez": fallecidos_adultez_cusco_convencion,
       "persona_mayor": fallecidos_persona_mayor_cusco_convencion
      }},

        {"name": "Paruro", "positivos": positivos_cusco_paruro,"poblacion": poblacion_cusco_paruro , "hombres_infectados": positivos_hombres_cusco_paruro,"mujeres_infectados": positivos_mujeres_cusco_paruro, "fallecidos": fallecidos_cusco_paruro, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_paruro,
       "infancia": fallecidos_infancia_cusco_paruro,
       "adolescencia": fallecidos_adolescencia_cusco_paruro,
       "juventud": fallecidos_juventud_cusco_paruro,
       "adultez": fallecidos_adultez_cusco_paruro,
       "persona_mayor": fallecidos_persona_mayor_cusco_paruro
      }},

        {"name": "Paucartambo", "positivos": positivos_cusco_paucartambo,"poblacion": poblacion_cusco_paucartambo , "hombres_infectados": positivos_hombres_cusco_paucartambo,"mujeres_infectados": positivos_mujeres_cusco_paucartambo, "fallecidos": fallecidos_cusco_paucartambo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_paucartambo,
       "infancia": fallecidos_infancia_cusco_paucartambo,
       "adolescencia": fallecidos_adolescencia_cusco_paucartambo,
       "juventud": fallecidos_juventud_cusco_paucartambo,
       "adultez": fallecidos_adultez_cusco_paucartambo,
       "persona_mayor": fallecidos_persona_mayor_cusco_paucartambo
      }},

        {"name": "Quispicanchi", "positivos": positivos_cusco_quispicanchi,"poblacion": poblacion_cusco_quispicanchi , "hombres_infectados": positivos_hombres_cusco_quispicanchi,"mujeres_infectados": positivos_mujeres_cusco_quispicanchi, "fallecidos": fallecidos_cusco_quispicanchi, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_quispicanchi,
       "infancia": fallecidos_infancia_cusco_quispicanchi,
       "adolescencia": fallecidos_adolescencia_cusco_quispicanchi,
       "juventud": fallecidos_juventud_cusco_quispicanchi,
       "adultez": fallecidos_adultez_cusco_quispicanchi,
       "persona_mayor": fallecidos_persona_mayor_cusco_quispicanchi
      }},

        {"name": "Urubamba", "positivos": positivos_cusco_urubamba,"poblacion": poblacion_cusco_urubamba , "hombres_infectados": positivos_hombres_cusco_urubamba,"mujeres_infectados": positivos_mujeres_cusco_urubamba, "fallecidos": fallecidos_cusco_urubamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_cusco_urubamba,
       "infancia": fallecidos_infancia_cusco_urubamba,
       "adolescencia": fallecidos_adolescencia_cusco_urubamba,
       "juventud": fallecidos_juventud_cusco_urubamba,
       "adultez": fallecidos_adultez_cusco_urubamba,
       "persona_mayor": fallecidos_persona_mayor_cusco_urubamba
      }}
      ]
    },
    {
      "name": "Madre de Dios",
      "poblacion": poblacion_madrededios,
      "positivos": positivos_madrededios,
      "hombres_infectados": positivos_hombres_madrededios,
      "mujeres_infectados": positivos_mujeres_madrededios,
      "fallecidos": fallecidos_madrededios,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_madrededios,
       "infancia": fallecidos_infancia_madrededios,
       "adolescencia": fallecidos_adolescencia_madrededios,
       "juventud": fallecidos_juventud_madrededios,
       "adultez": fallecidos_adultez_madrededios,
       "persona_mayor": fallecidos_persona_mayor_madrededios
      },
      "url": "madre-de-dios",
      "provincias": [
        {"name": "Tambopata", "positivos": positivos_madre_de_dios_tambopata,"poblacion": poblacion_madre_de_dios_tambopata , "hombres_infectados": positivos_hombres_madre_de_dios_tambopata,"mujeres_infectados": positivos_mujeres_madre_de_dios_tambopata, "fallecidos": fallecidos_madre_de_dios_tambopata, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_madre_de_dios_tambopata,
       "infancia": fallecidos_infancia_madre_de_dios_tambopata,
       "adolescencia": fallecidos_adolescencia_madre_de_dios_tambopata,
       "juventud": fallecidos_juventud_madre_de_dios_tambopata,
       "adultez": fallecidos_adultez_madre_de_dios_tambopata,
       "persona_mayor": fallecidos_persona_mayor_madre_de_dios_tambopata
      }},

        {"name": "Manu", "positivos": positivos_madre_de_dios_manu,"poblacion": poblacion_madre_de_dios_manu , "hombres_infectados": positivos_hombres_madre_de_dios_manu,"mujeres_infectados": positivos_mujeres_madre_de_dios_manu, "fallecidos": fallecidos_madre_de_dios_manu, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_madre_de_dios_manu,
       "infancia": fallecidos_infancia_madre_de_dios_manu,
       "adolescencia": fallecidos_adolescencia_madre_de_dios_manu,
       "juventud": fallecidos_juventud_madre_de_dios_manu,
       "adultez": fallecidos_adultez_madre_de_dios_manu,
       "persona_mayor": fallecidos_persona_mayor_madre_de_dios_manu
      }},

        {"name": "Tahuamanu", "positivos": positivos_madre_de_dios_tahuamanu,"poblacion": poblacion_madre_de_dios_tahuamanu , "hombres_infectados": positivos_hombres_madre_de_dios_tahuamanu,"mujeres_infectados": positivos_mujeres_madre_de_dios_tahuamanu, "fallecidos": fallecidos_madre_de_dios_tahuamanu, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_madre_de_dios_tahuamanu,
       "infancia": fallecidos_infancia_madre_de_dios_tahuamanu,
       "adolescencia": fallecidos_adolescencia_madre_de_dios_tahuamanu,
       "juventud": fallecidos_juventud_madre_de_dios_tahuamanu,
       "adultez": fallecidos_adultez_madre_de_dios_tahuamanu,
       "persona_mayor": fallecidos_persona_mayor_madre_de_dios_tahuamanu
      }} 
      ]
    },
    {
      "name": "Puno",
      "poblacion": poblacion_puno,
      "positivos": positivos_puno,
      "hombres_infectados": positivos_hombres_puno,
      "mujeres_infectados": positivos_mujeres_puno,
      "fallecidos": fallecidos_puno,
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
        {"name": "Puno", "positivos": positivos_puno_puno,"poblacion": poblacion_puno_puno , "hombres_infectados": positivos_hombres_puno_puno,"mujeres_infectados": positivos_mujeres_puno_puno, "fallecidos": fallecidos_puno_puno, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_puno,
       "infancia": fallecidos_infancia_puno_puno,
       "adolescencia": fallecidos_adolescencia_puno_puno,
       "juventud": fallecidos_juventud_puno_puno,
       "adultez": fallecidos_adultez_puno_puno,
       "persona_mayor": fallecidos_persona_mayor_puno_puno
      }},

        {"name": "Azangaro", "positivos": positivos_puno_azangaro,"poblacion": poblacion_puno_azangaro , "hombres_infectados": positivos_hombres_puno_azangaro,"mujeres_infectados": positivos_mujeres_puno_azangaro, "fallecidos": fallecidos_puno_azangaro, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_azangaro,
       "infancia": fallecidos_infancia_puno_azangaro,
       "adolescencia": fallecidos_adolescencia_puno_azangaro,
       "juventud": fallecidos_juventud_puno_azangaro,
       "adultez": fallecidos_adultez_puno_azangaro,
       "persona_mayor": fallecidos_persona_mayor_puno_azangaro
      }},

        {"name": "Carabaya", "positivos": positivos_puno_carabaya,"poblacion": poblacion_puno_carabaya , "hombres_infectados": positivos_hombres_puno_carabaya,"mujeres_infectados": positivos_mujeres_puno_carabaya, "fallecidos": fallecidos_puno_carabaya, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_carabaya,
       "infancia": fallecidos_infancia_puno_carabaya,
       "adolescencia": fallecidos_adolescencia_puno_carabaya,
       "juventud": fallecidos_juventud_puno_carabaya,
       "adultez": fallecidos_adultez_puno_carabaya,
       "persona_mayor": fallecidos_persona_mayor_puno_carabaya
      }},

        {"name": "Chucuito", "positivos": positivos_puno_chucuito,"poblacion": poblacion_puno_chucuito , "hombres_infectados": positivos_hombres_puno_chucuito,"mujeres_infectados": positivos_mujeres_puno_chucuito, "fallecidos": fallecidos_puno_chucuito, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_chucuito,
       "infancia": fallecidos_infancia_puno_chucuito,
       "adolescencia": fallecidos_adolescencia_puno_chucuito,
       "juventud": fallecidos_juventud_puno_chucuito,
       "adultez": fallecidos_adultez_puno_chucuito,
       "persona_mayor": fallecidos_persona_mayor_puno_chucuito
      }},

        {"name": "El Collao", "positivos": positivos_puno_collao,"poblacion": poblacion_puno_collao , "hombres_infectados": positivos_hombres_puno_collao,"mujeres_infectados": positivos_mujeres_puno_collao, "fallecidos": fallecidos_puno_collao, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_collao,
       "infancia": fallecidos_infancia_puno_collao,
       "adolescencia": fallecidos_adolescencia_puno_collao,
       "juventud": fallecidos_juventud_puno_collao,
       "adultez": fallecidos_adultez_puno_collao,
       "persona_mayor": fallecidos_persona_mayor_puno_collao
      }},

        {"name": "Huancane", "positivos": positivos_puno_huancane,"poblacion": poblacion_puno_huancane , "hombres_infectados": positivos_hombres_puno_huancane,"mujeres_infectados": positivos_mujeres_puno_huancane, "fallecidos": fallecidos_puno_huancane, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_huancane,
       "infancia": fallecidos_infancia_puno_huancane,
       "adolescencia": fallecidos_adolescencia_puno_huancane,
       "juventud": fallecidos_juventud_puno_huancane,
       "adultez": fallecidos_adultez_puno_huancane,
       "persona_mayor": fallecidos_persona_mayor_puno_huancane
      }},

        {"name": "Lampa", "positivos": positivos_puno_lampa,"poblacion": poblacion_puno_lampa , "hombres_infectados": positivos_hombres_puno_lampa,"mujeres_infectados": positivos_mujeres_puno_lampa, "fallecidos": fallecidos_puno_lampa, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_lampa,
       "infancia": fallecidos_infancia_puno_lampa,
       "adolescencia": fallecidos_adolescencia_puno_lampa,
       "juventud": fallecidos_juventud_puno_lampa,
       "adultez": fallecidos_adultez_puno_lampa,
       "persona_mayor": fallecidos_persona_mayor_puno_lampa
      }},

        {"name": "Melgar", "positivos": positivos_puno_melgar,"poblacion": poblacion_puno_melgar , "hombres_infectados": positivos_hombres_puno_melgar,"mujeres_infectados": positivos_mujeres_puno_melgar, "fallecidos": fallecidos_puno_melgar, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_melgar,
       "infancia": fallecidos_infancia_puno_melgar,
       "adolescencia": fallecidos_adolescencia_puno_melgar,
       "juventud": fallecidos_juventud_puno_melgar,
       "adultez": fallecidos_adultez_puno_melgar,
       "persona_mayor": fallecidos_persona_mayor_puno_melgar
      }},

        {"name": "Moho", "positivos": positivos_puno_moho,"poblacion": poblacion_puno_moho , "hombres_infectados": positivos_hombres_puno_moho,"mujeres_infectados": positivos_mujeres_puno_moho, "fallecidos": fallecidos_puno_moho, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_moho,
       "infancia": fallecidos_infancia_puno_moho,
       "adolescencia": fallecidos_adolescencia_puno_moho,
       "juventud": fallecidos_juventud_puno_moho,
       "adultez": fallecidos_adultez_puno_moho,
       "persona_mayor": fallecidos_persona_mayor_puno_moho
      }},

        {"name": "San Antonio de Putina", "positivos": positivos_puno_san_antonio_de_putina,"poblacion": poblacion_puno_san_antonio_de_putina , "hombres_infectados": positivos_hombres_puno_san_antonio_de_putina,"mujeres_infectados": positivos_mujeres_puno_san_antonio_de_putina, "fallecidos": fallecidos_puno_san_antonio_de_putina, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_san_antonio_de_putina,
       "infancia": fallecidos_infancia_puno_san_antonio_de_putina,
       "adolescencia": fallecidos_adolescencia_puno_san_antonio_de_putina,
       "juventud": fallecidos_juventud_puno_san_antonio_de_putina,
       "adultez": fallecidos_adultez_puno_san_antonio_de_putina,
       "persona_mayor": fallecidos_persona_mayor_puno_san_antonio_de_putina
      }},

        {"name": "San Roman", "positivos": positivos_puno_san_roman,"poblacion": poblacion_puno_san_roman , "hombres_infectados": positivos_hombres_puno_san_roman,"mujeres_infectados": positivos_mujeres_puno_san_roman, "fallecidos": fallecidos_puno_san_roman, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_san_roman,
       "infancia": fallecidos_infancia_puno_san_roman,
       "adolescencia": fallecidos_adolescencia_puno_san_roman,
       "juventud": fallecidos_juventud_puno_san_roman,
       "adultez": fallecidos_adultez_puno_san_roman,
       "persona_mayor": fallecidos_persona_mayor_puno_san_roman
      }},

        {"name": "Sandia", "positivos": positivos_puno_sandia,"poblacion": poblacion_puno_sandia , "hombres_infectados": positivos_hombres_puno_sandia,"mujeres_infectados": positivos_mujeres_puno_sandia, "fallecidos": fallecidos_puno_sandia, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_sandia,
       "infancia": fallecidos_infancia_puno_sandia,
       "adolescencia": fallecidos_adolescencia_puno_sandia,
       "juventud": fallecidos_juventud_puno_sandia,
       "adultez": fallecidos_adultez_puno_sandia,
       "persona_mayor": fallecidos_persona_mayor_puno_sandia
      }},

        {"name": "Yunguyo", "positivos": positivos_puno_yunguyo,"poblacion": poblacion_puno_yunguyo , "hombres_infectados": positivos_hombres_puno_yunguyo,"mujeres_infectados": positivos_mujeres_puno_yunguyo, "fallecidos": fallecidos_puno_yunguyo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_puno_yunguyo,
       "infancia": fallecidos_infancia_puno_yunguyo,
       "adolescencia": fallecidos_adolescencia_puno_yunguyo,
       "juventud": fallecidos_juventud_puno_yunguyo,
       "adultez": fallecidos_adultez_puno_yunguyo,
       "persona_mayor": fallecidos_persona_mayor_puno_yunguyo
      }}
      ]
    },
    {
      "name": "Arequipa",
      "poblacion": poblacion_arequipa,
      "positivos": positivos_arequipa,
      "hombres_infectados": positivos_hombres_arequipa,
      "mujeres_infectados": positivos_mujeres_arequipa,
      "fallecidos": fallecidos_arequipa,
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
        {"name": "Arequipa", "positivos": positivos_arequipa_arequipa,"poblacion": poblacion_arequipa_arequipa , "hombres_infectados": positivos_hombres_arequipa_arequipa,"mujeres_infectados": positivos_mujeres_arequipa_arequipa, "fallecidos": fallecidos_arequipa_arequipa, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_arequipa,
       "infancia": fallecidos_infancia_arequipa_arequipa,
       "adolescencia": fallecidos_adolescencia_arequipa_arequipa,
       "juventud": fallecidos_juventud_arequipa_arequipa,
       "adultez": fallecidos_adultez_arequipa_arequipa,
       "persona_mayor": fallecidos_persona_mayor_arequipa_arequipa
      }},

        {"name": "Camana", "positivos": positivos_arequipa_camana,"poblacion": poblacion_arequipa_camana , "hombres_infectados": positivos_hombres_arequipa_camana,"mujeres_infectados": positivos_mujeres_arequipa_camana, "fallecidos": fallecidos_arequipa_camana, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_camana,
       "infancia": fallecidos_infancia_arequipa_camana,
       "adolescencia": fallecidos_adolescencia_arequipa_camana,
       "juventud": fallecidos_juventud_arequipa_camana,
       "adultez": fallecidos_adultez_arequipa_camana,
       "persona_mayor": fallecidos_persona_mayor_arequipa_camana
      }},

        {"name": "Caraveli", "positivos": positivos_arequipa_caraveli,"poblacion": poblacion_arequipa_caraveli , "hombres_infectados": positivos_hombres_arequipa_caraveli,"mujeres_infectados": positivos_mujeres_arequipa_caraveli, "fallecidos": fallecidos_arequipa_caraveli, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_caraveli,
       "infancia": fallecidos_infancia_arequipa_caraveli,
       "adolescencia": fallecidos_adolescencia_arequipa_caraveli,
       "juventud": fallecidos_juventud_arequipa_caraveli,
       "adultez": fallecidos_adultez_arequipa_caraveli,
       "persona_mayor": fallecidos_persona_mayor_arequipa_caraveli
      }},

        {"name": "Castilla", "positivos": positivos_arequipa_castilla,"poblacion": poblacion_arequipa_castilla , "hombres_infectados": positivos_hombres_arequipa_castilla,"mujeres_infectados": positivos_mujeres_arequipa_castilla, "fallecidos": fallecidos_arequipa_castilla, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_castilla,
       "infancia": fallecidos_infancia_arequipa_castilla,
       "adolescencia": fallecidos_adolescencia_arequipa_castilla,
       "juventud": fallecidos_juventud_arequipa_castilla,
       "adultez": fallecidos_adultez_arequipa_castilla,
       "persona_mayor": fallecidos_persona_mayor_arequipa_castilla
      }},

        {"name": "Cayllona", "positivos": positivos_arequipa_cayllona,"poblacion": poblacion_arequipa_cayllona , "hombres_infectados": positivos_hombres_arequipa_cayllona,"mujeres_infectados": positivos_mujeres_arequipa_cayllona, "fallecidos": fallecidos_arequipa_cayllona, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_cayllona,
       "infancia": fallecidos_infancia_arequipa_cayllona,
       "adolescencia": fallecidos_adolescencia_arequipa_cayllona,
       "juventud": fallecidos_juventud_arequipa_cayllona,
       "adultez": fallecidos_adultez_arequipa_cayllona,
       "persona_mayor": fallecidos_persona_mayor_arequipa_cayllona
      }},

        {"name": "Condesuyos", "positivos": positivos_arequipa_condesuyos,"poblacion": poblacion_arequipa_condesuyos , "hombres_infectados": positivos_hombres_arequipa_condesuyos,"mujeres_infectados": positivos_mujeres_arequipa_condesuyos, "fallecidos": fallecidos_arequipa_condesuyos, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_condesuyos,
       "infancia": fallecidos_infancia_arequipa_condesuyos,
       "adolescencia": fallecidos_adolescencia_arequipa_condesuyos,
       "juventud": fallecidos_juventud_arequipa_condesuyos,
       "adultez": fallecidos_adultez_arequipa_condesuyos,
       "persona_mayor": fallecidos_persona_mayor_arequipa_condesuyos
      }},

        {"name": "Islay", "positivos": positivos_arequipa_islay,"poblacion": poblacion_arequipa_islay , "hombres_infectados": positivos_hombres_arequipa_islay,"mujeres_infectados": positivos_mujeres_arequipa_islay, "fallecidos": fallecidos_arequipa_islay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_islay,
       "infancia": fallecidos_infancia_arequipa_islay,
       "adolescencia": fallecidos_adolescencia_arequipa_islay,
       "juventud": fallecidos_juventud_arequipa_islay,
       "adultez": fallecidos_adultez_arequipa_islay,
       "persona_mayor": fallecidos_persona_mayor_arequipa_islay
      }},

        {"name": "La Union", "positivos": positivos_arequipa_union,"poblacion": poblacion_arequipa_union , "hombres_infectados": positivos_hombres_arequipa_union,"mujeres_infectados": positivos_mujeres_arequipa_union, "fallecidos": fallecidos_arequipa_union, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_arequipa_union,
       "infancia": fallecidos_infancia_arequipa_union,
       "adolescencia": fallecidos_adolescencia_arequipa_union,
       "juventud": fallecidos_juventud_arequipa_union,
       "adultez": fallecidos_adultez_arequipa_union,
       "persona_mayor": fallecidos_persona_mayor_arequipa_union
      }}
      ]
    },
    {
      "name": "Moquegua",
      "poblacion": poblacion_moquegua,
      "positivos": positivos_moquegua,
      "hombres_infectados": positivos_hombres_moquegua,
      "mujeres_infectados": positivos_mujeres_moquegua,
      "fallecidos": fallecidos_moquegua,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_moquegua,
       "infancia": fallecidos_infancia_moquegua,
       "adolescencia": fallecidos_adolescencia_moquegua,
       "juventud": fallecidos_juventud_moquegua,
       "adultez": fallecidos_adultez_moquegua,
       "persona_mayor": fallecidos_persona_mayor_moquegua
      },
      "url": "moquegua",
      "provincias": [
        {"name": "Mariscal Nieto", "positivos": positivos_moquegua_mariscal_nieto,"poblacion": poblacion_moquegua_mariscal_nieto , "hombres_infectados": positivos_hombres_moquegua_mariscal_nieto,"mujeres_infectados": positivos_mujeres_moquegua_mariscal_nieto, "fallecidos": fallecidos_moquegua_mariscal_nieto, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_moquegua_mariscal_nieto,
       "infancia": fallecidos_infancia_moquegua_mariscal_nieto,
       "adolescencia": fallecidos_adolescencia_moquegua_mariscal_nieto,
       "juventud": fallecidos_juventud_moquegua_mariscal_nieto,
       "adultez": fallecidos_adultez_moquegua_mariscal_nieto,
       "persona_mayor": fallecidos_persona_mayor_moquegua_mariscal_nieto
      }},

        {"name": "General Sanchez Cerro", "positivos": positivos_moquegua_general_sanchez_cerro,"poblacion": poblacion_moquegua_general_sanchez_cerro , "hombres_infectados": positivos_hombres_moquegua_general_sanchez_cerro,"mujeres_infectados": positivos_mujeres_moquegua_general_sanchez_cerro, "fallecidos": fallecidos_moquegua_general_sanchez_cerro, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_moquegua_general_sanchez_cerro,
       "infancia": fallecidos_infancia_moquegua_general_sanchez_cerro,
       "adolescencia": fallecidos_adolescencia_moquegua_general_sanchez_cerro,
       "juventud": fallecidos_juventud_moquegua_general_sanchez_cerro,
       "adultez": fallecidos_adultez_moquegua_general_sanchez_cerro,
       "persona_mayor": fallecidos_persona_mayor_moquegua_general_sanchez_cerro
      }},

        {"name": "Ilo", "positivos": positivos_moquegua_ilo,"poblacion": poblacion_moquegua_ilo , "hombres_infectados": positivos_hombres_moquegua_ilo,"mujeres_infectados": positivos_mujeres_moquegua_ilo, "fallecidos": fallecidos_moquegua_ilo, "type": "Provincia",  "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_moquegua_ilo,
       "infancia": fallecidos_infancia_moquegua_ilo,
       "adolescencia": fallecidos_adolescencia_moquegua_ilo,
       "juventud": fallecidos_juventud_moquegua_ilo,
       "adultez": fallecidos_adultez_moquegua_ilo,
       "persona_mayor": fallecidos_persona_mayor_moquegua_ilo
      }}
      ]
    },
    {
      "name": "Tacna",
      "poblacion": poblacion_tacna,
      "positivos": positivos_tacna,
      "hombres_infectados": positivos_hombres_tacna,
      "mujeres_infectados": positivos_mujeres_tacna,
      "fallecidos": fallecidos_tacna,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tacna,
       "infancia": fallecidos_infancia_tacna,
       "adolescencia": fallecidos_adolescencia_tacna,
       "juventud": fallecidos_juventud_tacna,
       "adultez": fallecidos_adultez_tacna,
       "persona_mayor": fallecidos_persona_mayor_tacna
      },
      "url": "tacna",
      "provincias": [
        {"name": "Tacna", "positivos": positivos_tacna_tacna,"poblacion": poblacion_tacna_tacna , "hombres_infectados": positivos_hombres_tacna_tacna,"mujeres_infectados": positivos_mujeres_tacna_tacna, "fallecidos": fallecidos_tacna_tacna, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tacna_tacna,
       "infancia": fallecidos_infancia_tacna_tacna,
       "adolescencia": fallecidos_adolescencia_tacna_tacna,
       "juventud": fallecidos_juventud_tacna_tacna,
       "adultez": fallecidos_adultez_tacna_tacna,
       "persona_mayor": fallecidos_persona_mayor_tacna_tacna
      }},

        {"name": "Candarave", "positivos": positivos_tacna_candarave,"poblacion": poblacion_tacna_candarave , "hombres_infectados": positivos_hombres_tacna_candarave,"mujeres_infectados": positivos_mujeres_tacna_candarave, "fallecidos": fallecidos_tacna_candarave, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tacna_candarave,
       "infancia": fallecidos_infancia_tacna_candarave,
       "adolescencia": fallecidos_adolescencia_tacna_candarave,
       "juventud": fallecidos_juventud_tacna_candarave,
       "adultez": fallecidos_adultez_tacna_candarave,
       "persona_mayor": fallecidos_persona_mayor_tacna_candarave
      }},

        {"name": "Jorge Basadre", "positivos": positivos_tacna_jorge_basadre,"poblacion": poblacion_tacna_jorge_basadre , "hombres_infectados": positivos_hombres_tacna_jorge_basadre,"mujeres_infectados": positivos_mujeres_tacna_jorge_basadre, "fallecidos": fallecidos_tacna_jorge_basadre, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tacna_jorge_basadre,
       "infancia": fallecidos_infancia_tacna_jorge_basadre,
       "adolescencia": fallecidos_adolescencia_tacna_jorge_basadre,
       "juventud": fallecidos_juventud_tacna_jorge_basadre,
       "adultez": fallecidos_adultez_tacna_jorge_basadre,
       "persona_mayor": fallecidos_persona_mayor_tacna_jorge_basadre
      }},

        {"name": "Tarata", "positivos": positivos_tacna_tarata,"poblacion": poblacion_tacna_tarata , "hombres_infectados": positivos_hombres_tacna_tarata,"mujeres_infectados": positivos_mujeres_tacna_tarata, "fallecidos": fallecidos_tacna_tarata, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_tacna_tarata,
       "infancia": fallecidos_infancia_tacna_tarata,
       "adolescencia": fallecidos_adolescencia_tacna_tarata,
       "juventud": fallecidos_juventud_tacna_tarata,
       "adultez": fallecidos_adultez_tacna_tarata,
       "persona_mayor": fallecidos_persona_mayor_tacna_tarata
      }},
      ]
    },
    {
      "name": "Callao",
      "poblacion": poblacion_callao,
      "positivos": positivos_callao,
      "hombres_infectados": positivos_hombres_callao,
      "mujeres_infectados": positivos_mujeres_callao,
      "fallecidos": fallecidos_callao,
      "type": "Departamento",
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_callao,
       "infancia": fallecidos_infancia_callao,
       "adolescencia": fallecidos_adolescencia_callao,
       "juventud": fallecidos_juventud_callao,
       "adultez": fallecidos_adultez_callao,
       "persona_mayor": fallecidos_persona_mayor_callao
      },
      "url": "callao",
        "provincias": [
            {"name": "Callao", "positivos": positivos_callao_callao,"poblacion": poblacion_callao_callao , "hombres_infectados": positivos_hombres_callao_callao,"mujeres_infectados": positivos_mujeres_callao_callao, "fallecidos": fallecidos_callao_callao, "type": "Provincia",  "etapa_de_vida_fallecidos": {
        "primera_infancia": fallecidos_preinfancia_callao_callao,
        "infancia": fallecidos_infancia_callao_callao,
        "adolescencia": fallecidos_adolescencia_callao_callao,
        "juventud": fallecidos_juventud_callao_callao,
        "adultez": fallecidos_adultez_callao_callao,
        "persona_mayor": fallecidos_persona_mayor_callao_callao
        }}
        ]
    }
]

print(json.dumps(busqueda));
sys.stdout.flush();





















