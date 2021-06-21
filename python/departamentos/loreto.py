import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos


poblacion_loreto = 1041482
positivos_loreto = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "LORETO"].shape)[0]
positivos_hombres_loreto = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LORETO") & (casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_loreto = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LORETO") & (casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_loreto = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "LORETO"].shape)[0]
fallecidos_hombres_loreto  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LORETO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_loreto  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "LORETO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_loreto_maynas  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MAYNAS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_loreto_maynas  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MAYNAS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_loreto_alto_amazonas  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ALTO AMAZONAS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_loreto_alto_amazonas  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ALTO AMAZONAS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_loreto_loreto  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LORETO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_loreto_loreto  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LORETO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_loreto_mariscal_ramon_castilla  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL RAMON CASTILLA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_loreto_mariscal_ramon_castilla  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "MARISCAL RAMON CASTILLA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_loreto_requena  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "REQUENA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_loreto_requena  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "REQUENA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_loreto_ucayali  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UCAYALI") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_loreto_ucayali  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UCAYALI") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_loreto_datem_del_maranon  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DATEM DEL MARAÑON") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_loreto_datem_del_maranon  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "DATEM DEL MARAÑON") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_loreto_putumayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUTUMAYO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_loreto_putumayo  = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PUTUMAYO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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

loreto = {
      "name": "Loreto",
      "poblacion": poblacion_loreto,
      "positivos": positivos_loreto,
      "hombres_infectados": positivos_hombres_loreto,
      "mujeres_infectados": positivos_mujeres_loreto,
      "fallecidos": fallecidos_loreto,
      "hombres_fallecidos": fallecidos_hombres_loreto,
      "mujeres_fallecidos": fallecidos_mujeres_loreto,
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
          {"name": "Maynas", "positivos": positivos_loreto_maynas  , "poblacion": poblacion_loreto_maynas , "hombres_infectados": positivos_hombres_loreto_maynas,"mujeres_infectados": positivos_mujeres_loreto_maynas, "fallecidos": fallecidos_loreto_maynas, "hombres_fallecidos": fallecidos_hombres_loreto_maynas, "mujeres_fallecidos": fallecidos_mujeres_loreto_maynas, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_maynas,
          "infancia": fallecidos_infancia_loreto_maynas,
          "adolescencia": fallecidos_adolescencia_loreto_maynas,
          "juventud": fallecidos_juventud_loreto_maynas,
          "adultez": fallecidos_adultez_loreto_maynas,
          "persona_mayor": fallecidos_persona_mayor_loreto_maynas
          }},

          {"name": "Alto Amazonas", "positivos": positivos_loreto_alto_amazonas, "poblacion": poblacion_loreto_alto_amazonas , "hombres_infectados": positivos_hombres_loreto_alto_amazonas,"mujeres_infectados": positivos_mujeres_loreto_alto_amazonas, "fallecidos": fallecidos_loreto_alto_amazonas, "hombres_fallecidos": fallecidos_hombres_loreto_alto_amazonas, "mujeres_fallecidos": fallecidos_mujeres_loreto_alto_amazonas, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_alto_amazonas,
          "infancia": fallecidos_infancia_loreto_alto_amazonas,
          "adolescencia": fallecidos_adolescencia_loreto_alto_amazonas,
          "juventud": fallecidos_juventud_loreto_alto_amazonas,
          "adultez": fallecidos_adultez_loreto_alto_amazonas,
          "persona_mayor": fallecidos_persona_mayor_loreto_alto_amazonas
          }},

          {"name": "Loreto", "positivos": positivos_loreto_loreto, "poblacion": poblacion_loreto_loreto, "hombres_infectados": positivos_hombres_loreto_loreto, "mujeres_infectados": positivos_mujeres_loreto_loreto, "fallecidos": fallecidos_loreto_loreto, "hombres_fallecidos": fallecidos_hombres_loreto_loreto, "mujeres_fallecidos": fallecidos_mujeres_loreto_loreto, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_loreto,
          "infancia": fallecidos_infancia_loreto_loreto,
          "adolescencia": fallecidos_adolescencia_loreto_loreto,
          "juventud": fallecidos_juventud_loreto_loreto,
          "adultez": fallecidos_adultez_loreto_loreto,
          "persona_mayor": fallecidos_persona_mayor_loreto_loreto
          }},

          {"name": "Mariscal Ramon Castilla", "positivos": positivos_loreto_mariscal_ramon_castilla, "poblacion": poblacion_loreto_mariscal_ramon_castilla , "hombres_infectados": positivos_hombres_loreto_mariscal_ramon_castilla,"mujeres_infectados": positivos_mujeres_loreto_mariscal_ramon_castilla, "fallecidos": fallecidos_loreto_mariscal_ramon_castilla, "hombres_fallecidos": fallecidos_hombres_loreto_mariscal_ramon_castilla, "mujeres_fallecidos": fallecidos_mujeres_loreto_mariscal_ramon_castilla, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_mariscal_ramon_castilla,
          "infancia": fallecidos_infancia_loreto_mariscal_ramon_castilla,
          "adolescencia": fallecidos_adolescencia_loreto_mariscal_ramon_castilla,
          "juventud": fallecidos_juventud_loreto_mariscal_ramon_castilla,
          "adultez": fallecidos_adultez_loreto_mariscal_ramon_castilla,
          "persona_mayor": fallecidos_persona_mayor_loreto_mariscal_ramon_castilla
          }},

          {"name": "Requena", "positivos": positivos_loreto_requena, "poblacion": poblacion_loreto_requena , "hombres_infectados": positivos_hombres_loreto_requena,"mujeres_infectados": positivos_mujeres_loreto_requena, "fallecidos": fallecidos_loreto_requena, "hombres_fallecidos": fallecidos_hombres_loreto_requena, "mujeres_fallecidos": fallecidos_mujeres_loreto_requena, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_requena,
          "infancia": fallecidos_infancia_loreto_requena,
          "adolescencia": fallecidos_adolescencia_loreto_requena,
          "juventud": fallecidos_juventud_loreto_requena,
          "adultez": fallecidos_adultez_loreto_requena,
          "persona_mayor": fallecidos_persona_mayor_loreto_requena
          }},

          {"name": "Ucayali", "positivos": positivos_loreto_ucayali, "poblacion": poblacion_loreto_ucayali , "hombres_infectados": positivos_hombres_loreto_ucayali,"mujeres_infectados": positivos_mujeres_loreto_ucayali, "fallecidos": fallecidos_loreto_ucayali, "hombres_fallecidos": fallecidos_hombres_loreto_ucayali, "mujeres_fallecidos": fallecidos_mujeres_loreto_ucayali, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_ucayali,
          "infancia": fallecidos_infancia_loreto_ucayali,
          "adolescencia": fallecidos_adolescencia_loreto_ucayali,
          "juventud": fallecidos_juventud_loreto_ucayali,
          "adultez": fallecidos_adultez_loreto_ucayali,
          "persona_mayor": fallecidos_persona_mayor_loreto_ucayali
          }},

          {"name": "Datem del Marañon", "positivos": positivos_loreto_datem_del_maranon, "poblacion": poblacion_loreto_datem_del_maranon, "hombres_infectados": positivos_hombres_loreto_datem_del_maranon, "mujeres_infectados": positivos_mujeres_loreto_datem_del_maranon, "fallecidos": fallecidos_loreto_datem_del_maranon, "hombres_fallecidos": fallecidos_hombres_loreto_datem_del_maranon, "mujeres_fallecidos": fallecidos_mujeres_loreto_datem_del_maranon, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_datem_del_maranon,
          "infancia": fallecidos_infancia_loreto_datem_del_maranon,
          "adolescencia": fallecidos_adolescencia_loreto_datem_del_maranon,
          "juventud": fallecidos_juventud_loreto_datem_del_maranon,
          "adultez": fallecidos_adultez_loreto_datem_del_maranon,
          "persona_mayor": fallecidos_persona_mayor_loreto_datem_del_maranon
          }},

          {"name": "Putumayo", "positivos": positivos_loreto_putumayo, "poblacion": poblacion_loreto_putumayo , "hombres_infectados": positivos_hombres_loreto_putumayo,"mujeres_infectados": positivos_mujeres_loreto_putumayo, "fallecidos": fallecidos_loreto_putumayo, "hombres_fallecidos": fallecidos_hombres_loreto_putumayo, "mujeres_fallecidos": fallecidos_mujeres_loreto_putumayo, "type": "Provincia",  "etapa_de_vida_fallecidos": {
          "primera_infancia": fallecidos_preinfancia_loreto_putumayo,
          "infancia": fallecidos_infancia_loreto_putumayo,
          "adolescencia": fallecidos_adolescencia_loreto_putumayo,
          "juventud": fallecidos_juventud_loreto_putumayo,
          "adultez": fallecidos_adultez_loreto_putumayo,
          "persona_mayor": fallecidos_persona_mayor_loreto_putumayo
          }}
      ]
    }


print(json.dumps(loreto));
sys.stdout.flush();
