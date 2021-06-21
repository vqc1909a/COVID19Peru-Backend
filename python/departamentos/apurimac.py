import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_apurimac = 424272
positivos_apurimac = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "APURIMAC"].shape)[0]
positivos_hombres_apurimac = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "APURIMAC") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_apurimac = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "APURIMAC") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_apurimac = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "APURIMAC"].shape)[0]
fallecidos_hombres_apurimac = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "APURIMAC") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_apurimac = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "APURIMAC") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_apurimac_abancay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ABANCAY") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_apurimac_abancay = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ABANCAY") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_apurimac_andahuaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANDAHUAYLAS") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_apurimac_andahuaylas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANDAHUAYLAS") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_apurimac_antabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTABAMBA") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_apurimac_antabamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "ANTABAMBA") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_apurimac_aymaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYMARAES") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_apurimac_aymaraes = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "AYMARAES") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_apurimac_cotabambas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "COTABAMBAS") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_apurimac_cotabambas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "COTABAMBAS") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_apurimac_chincheros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHEROS") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_apurimac_chincheros = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHINCHEROS") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]



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
fallecidos_hombres_apurimac_grau = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAU") & (casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_apurimac_grau = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "GRAU") & (casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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

apurimac =  {
      "name": "Apurimac",
      "poblacion": poblacion_apurimac,
      "positivos": positivos_apurimac,
      "hombres_infectados": positivos_hombres_apurimac,
      "mujeres_infectados": positivos_mujeres_apurimac,
      "fallecidos": fallecidos_apurimac,
      "hombres_fallecidos": fallecidos_hombres_apurimac,
      "mujeres_fallecidos": fallecidos_mujeres_apurimac,
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
          {"name": "Abancay", "positivos": positivos_apurimac_abancay, "poblacion": poblacion_apurimac_abancay, "hombres_infectados": positivos_hombres_apurimac_abancay, "mujeres_infectados": positivos_mujeres_apurimac_abancay, "fallecidos": fallecidos_apurimac_abancay, "hombres_fallecidos": fallecidos_hombres_apurimac_abancay, "mujeres_fallecidos": fallecidos_mujeres_apurimac_abancay, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_abancay,
       "infancia": fallecidos_infancia_apurimac_abancay,
       "adolescencia": fallecidos_adolescencia_apurimac_abancay,
       "juventud": fallecidos_juventud_apurimac_abancay,
       "adultez": fallecidos_adultez_apurimac_abancay,
       "persona_mayor": fallecidos_persona_mayor_apurimac_abancay,
      }},

          {"name": "Andahuaylas", "positivos": positivos_apurimac_andahuaylas,"poblacion": poblacion_apurimac_andahuaylas , "hombres_infectados": positivos_hombres_apurimac_andahuaylas,"mujeres_infectados": positivos_mujeres_apurimac_andahuaylas, "fallecidos": fallecidos_apurimac_andahuaylas, "hombres_fallecidos": fallecidos_hombres_apurimac_andahuaylas, "mujeres_fallecidos": fallecidos_mujeres_apurimac_andahuaylas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_andahuaylas,
       "infancia": fallecidos_infancia_apurimac_andahuaylas,
       "adolescencia": fallecidos_adolescencia_apurimac_andahuaylas,
       "juventud": fallecidos_juventud_apurimac_andahuaylas,
       "adultez": fallecidos_adultez_apurimac_andahuaylas,
       "persona_mayor": fallecidos_persona_mayor_apurimac_andahuaylas
      }},

          {"name": "Antabamba", "positivos": positivos_apurimac_antabamba,"poblacion": poblacion_apurimac_antabamba , "hombres_infectados": positivos_hombres_apurimac_antabamba,"mujeres_infectados": positivos_mujeres_apurimac_antabamba, "fallecidos": fallecidos_apurimac_antabamba, "hombres_fallecidos": fallecidos_hombres_apurimac_antabamba, "mujeres_fallecidos": fallecidos_mujeres_apurimac_antabamba, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_antabamba,
       "infancia": fallecidos_infancia_apurimac_antabamba,
       "adolescencia": fallecidos_adolescencia_apurimac_antabamba,
       "juventud": fallecidos_juventud_apurimac_antabamba,
       "adultez": fallecidos_adultez_apurimac_antabamba,
       "persona_mayor": fallecidos_persona_mayor_apurimac_antabamba
      }},

          {"name": "Aymaraes", "positivos": positivos_apurimac_aymaraes, "poblacion": poblacion_apurimac_aymaraes, "hombres_infectados": positivos_hombres_apurimac_aymaraes, "mujeres_infectados": positivos_mujeres_apurimac_aymaraes, "fallecidos": fallecidos_apurimac_aymaraes, "hombres_fallecidos": fallecidos_hombres_apurimac_aymaraes, "mujeres_fallecidos": fallecidos_mujeres_apurimac_aymaraes, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_aymaraes,
       "infancia": fallecidos_infancia_apurimac_aymaraes,
       "adolescencia": fallecidos_adolescencia_apurimac_aymaraes,
       "juventud": fallecidos_juventud_apurimac_aymaraes,
       "adultez": fallecidos_adultez_apurimac_aymaraes,
       "persona_mayor": fallecidos_persona_mayor_apurimac_aymaraes
      }},

          {"name": "Cotabambas", "positivos": positivos_apurimac_cotabambas,"poblacion": poblacion_apurimac_cotabambas , "hombres_infectados": positivos_hombres_apurimac_cotabambas,"mujeres_infectados": positivos_mujeres_apurimac_cotabambas, "fallecidos": fallecidos_apurimac_cotabambas, "hombres_fallecidos": fallecidos_hombres_apurimac_cotabambas, "mujeres_fallecidos": fallecidos_mujeres_apurimac_cotabambas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_cotabambas,
       "infancia": fallecidos_infancia_apurimac_cotabambas,
       "adolescencia": fallecidos_adolescencia_apurimac_cotabambas,
       "juventud": fallecidos_juventud_apurimac_cotabambas,
       "adultez": fallecidos_adultez_apurimac_cotabambas,
       "persona_mayor": fallecidos_persona_mayor_apurimac_cotabambas
      }},

          {"name": "Chincheros", "positivos": positivos_apurimac_chincheros, "poblacion": poblacion_apurimac_chincheros, "hombres_infectados": positivos_hombres_apurimac_chincheros, "mujeres_infectados": positivos_mujeres_apurimac_chincheros, "fallecidos": fallecidos_apurimac_chincheros, "hombres_fallecidos": fallecidos_hombres_apurimac_chincheros, "mujeres_fallecidos": fallecidos_mujeres_apurimac_chincheros, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_chincheros,
       "infancia": fallecidos_infancia_apurimac_chincheros,
       "adolescencia": fallecidos_adolescencia_apurimac_chincheros,
       "juventud": fallecidos_juventud_apurimac_chincheros,
       "adultez": fallecidos_adultez_apurimac_chincheros,
       "persona_mayor": fallecidos_persona_mayor_apurimac_chincheros
      }}, 

          {"name": "Grau", "positivos": positivos_apurimac_grau, "poblacion": poblacion_apurimac_grau, "hombres_infectados": positivos_hombres_apurimac_grau, "mujeres_infectados": positivos_mujeres_apurimac_grau, "fallecidos": fallecidos_apurimac_grau, "hombres_fallecidos": fallecidos_hombres_apurimac_grau, "mujeres_fallecidos": fallecidos_mujeres_apurimac_grau, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_apurimac_grau,
       "infancia": fallecidos_infancia_apurimac_grau,
       "adolescencia": fallecidos_adolescencia_apurimac_grau,
       "juventud": fallecidos_juventud_apurimac_grau,
       "adultez": fallecidos_adultez_apurimac_grau,
       "persona_mayor": fallecidos_persona_mayor_apurimac_grau
      }}
      ]
    }

print(json.dumps(apurimac));
sys.stdout.flush();
