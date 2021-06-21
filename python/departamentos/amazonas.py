import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos

poblacion_amazonas = 433907
positivos_amazonas = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "AMAZONAS"].shape)[0]
positivos_hombres_amazonas = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AMAZONAS") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_amazonas = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AMAZONAS") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_amazonas = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "AMAZONAS"].shape)[0]
fallecidos_hombres_amazonas = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AMAZONAS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_amazonas = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AMAZONAS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

#!Departamento Amazonas - Etapa de vida Fallecimiento
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
fallecidos_hombres_amazonas_chachapoyas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHACHAPOYAS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_amazonas_chachapoyas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CHACHAPOYAS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_amazonas_bagua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BAGUA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_amazonas_bagua = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BAGUA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_amazonas_bongara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BONGARA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_amazonas_bongara = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "BONGARA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_amazonas_condorcanqui = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONDORCANQUI") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_amazonas_condorcanqui = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CONDORCANQUI") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_amazonas_luya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUYA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_amazonas_luya = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUYA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_amazonas_rodriguez_de_mendoza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_amazonas_rodriguez_de_mendoza = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "RODRIGUEZ DE MENDOZA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_amazonas_utcubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UTCUBAMBA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_amazonas_utcubamba = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "UTCUBAMBA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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

amazonas =  {
      "name": "Amazonas",
      "poblacion": poblacion_amazonas,
      "positivos": positivos_amazonas,
      "hombres_infectados": positivos_hombres_amazonas,
      "mujeres_infectados": positivos_mujeres_amazonas,
      "fallecidos": fallecidos_amazonas,
      "hombres_fallecidos": fallecidos_hombres_amazonas, 
      "mujeres_fallecidos": fallecidos_mujeres_amazonas,
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
          {"name": "Chachapoyas", "positivos": positivos_amazonas_chachapoyas, "poblacion": poblacion_amazonas_chachapoyas, "hombres_infectados": positivos_hombres_amazonas_chachapoyas, "mujeres_infectados": positivos_mujeres_amazonas_chachapoyas, "fallecidos": fallecidos_amazonas_chachapoyas, "hombres_fallecidos": fallecidos_hombres_amazonas_chachapoyas, "mujeres_fallecidos": fallecidos_mujeres_amazonas_chachapoyas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_chachapoyas,
       "infancia": fallecidos_infancia_amazonas_chachapoyas,
       "adolescencia": fallecidos_adolescencia_amazonas_chachapoyas,
       "juventud": fallecidos_juventud_amazonas_chachapoyas,
       "adultez": fallecidos_adultez_amazonas_chachapoyas,
       "persona_mayor": fallecidos_persona_mayor_amazonas_chachapoyas
      }},

          {"name": "Bagua", "positivos": positivos_amazonas_bagua,"poblacion": poblacion_amazonas_bagua,"hombres_infectados": positivos_hombres_amazonas_bagua,"mujeres_infectados": positivos_mujeres_amazonas_bagua, "fallecidos": fallecidos_amazonas_bagua, "hombres_fallecidos": fallecidos_hombres_amazonas_bagua, "mujeres_fallecidos": fallecidos_mujeres_amazonas_bagua, "type": "Provincia",   
      "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_bagua,
       "infancia": fallecidos_infancia_amazonas_bagua,
       "adolescencia": fallecidos_adolescencia_amazonas_bagua,
       "juventud": fallecidos_juventud_amazonas_bagua,
       "adultez": fallecidos_adultez_amazonas_bagua,
       "persona_mayor": fallecidos_persona_mayor_amazonas_bagua
      }},

          {"name": "Bongara", "positivos": positivos_amazonas_bongara,"poblacion": poblacion_amazonas_bongara,"hombres_infectados": positivos_hombres_amazonas_bongara,"mujeres_infectados": positivos_mujeres_amazonas_bongara, "fallecidos": fallecidos_amazonas_bongara, "hombres_fallecidos": fallecidos_hombres_amazonas_bongara, "mujeres_fallecidos": fallecidos_mujeres_amazonas_bongara, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_bongara,
       "infancia": fallecidos_infancia_amazonas_bongara,
       "adolescencia": fallecidos_adolescencia_amazonas_bongara,
       "juventud": fallecidos_juventud_amazonas_bongara,
       "adultez": fallecidos_adultez_amazonas_bongara,
       "persona_mayor": fallecidos_persona_mayor_amazonas_bongara
      }},

          {"name": "Condorcanqui", "positivos": positivos_amazonas_condorcanqui,"poblacion": poblacion_amazonas_condorcanqui,"hombres_infectados": positivos_hombres_amazonas_condorcanqui,"mujeres_infectados": positivos_mujeres_amazonas_condorcanqui, "fallecidos": fallecidos_amazonas_condorcanqui, "hombres_fallecidos": fallecidos_hombres_amazonas_condorcanqui, "mujeres_fallecidos": fallecidos_mujeres_amazonas_condorcanqui, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_condorcanqui,
       "infancia": fallecidos_infancia_amazonas_condorcanqui,
       "adolescencia": fallecidos_adolescencia_amazonas_condorcanqui,
       "juventud": fallecidos_juventud_amazonas_condorcanqui,
       "adultez": fallecidos_adultez_amazonas_condorcanqui,
       "persona_mayor": fallecidos_persona_mayor_amazonas_condorcanqui
      }}, 

          {"name": "Luya", "positivos": positivos_amazonas_luya, "poblacion": poblacion_amazonas_luya, "hombres_infectados": positivos_hombres_amazonas_luya, "mujeres_infectados": positivos_mujeres_amazonas_luya, "fallecidos": fallecidos_amazonas_luya, "hombres_fallecidos": fallecidos_hombres_amazonas_luya, "mujeres_fallecidos": fallecidos_mujeres_amazonas_luya, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_luya,
       "infancia": fallecidos_infancia_amazonas_luya,
       "adolescencia": fallecidos_adolescencia_amazonas_luya,
       "juventud": fallecidos_juventud_amazonas_luya,
       "adultez": fallecidos_adultez_amazonas_luya,
       "persona_mayor": fallecidos_persona_mayor_amazonas_luya
      }}, 

          {"name": "Rodriguez de Mendoza", "positivos": positivos_amazonas_rodriguez_de_mendoza,"poblacion": poblacion_amazonas_rodriguez_de_mendoza,"hombres_infectados": positivos_hombres_amazonas_rodriguez_de_mendoza,"mujeres_infectados": positivos_mujeres_amazonas_rodriguez_de_mendoza, "fallecidos": fallecidos_amazonas_rodriguez_de_mendoza, "hombres_fallecidos": fallecidos_hombres_amazonas_rodriguez_de_mendoza, "mujeres_fallecidos": fallecidos_mujeres_amazonas_rodriguez_de_mendoza, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_rodriguez_de_mendoza,
       "infancia": fallecidos_infancia_amazonas_rodriguez_de_mendoza,
       "adolescencia": fallecidos_adolescencia_amazonas_rodriguez_de_mendoza,
       "juventud": fallecidos_juventud_amazonas_rodriguez_de_mendoza,
       "adultez": fallecidos_adultez_amazonas_rodriguez_de_mendoza,
       "persona_mayor": fallecidos_persona_mayor_amazonas_rodriguez_de_mendoza
      }}, 

          {"name": "Utcubamba", "positivos": positivos_amazonas_utcubamba,"poblacion": poblacion_amazonas_utcubamba,"hombres_infectados": positivos_hombres_amazonas_utcubamba,"mujeres_infectados": positivos_mujeres_amazonas_utcubamba, "fallecidos": fallecidos_amazonas_utcubamba, "hombres_fallecidos": fallecidos_hombres_amazonas_utcubamba, "mujeres_fallecidos": fallecidos_mujeres_amazonas_utcubamba, "type": "Provincia",   "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_amazonas_utcubamba,
       "infancia": fallecidos_infancia_amazonas_utcubamba,
       "adolescencia": fallecidos_adolescencia_amazonas_utcubamba,
       "juventud": fallecidos_juventud_amazonas_utcubamba,
       "adultez": fallecidos_adultez_amazonas_utcubamba,
       "persona_mayor": fallecidos_persona_mayor_amazonas_utcubamba
      }} 
      ]
    }
    
print(json.dumps(amazonas));
sys.stdout.flush();
