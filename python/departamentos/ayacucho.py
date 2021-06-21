import pandas as pd
import json
import sys
from casos import casos_positivos, casos_fallecidos
    
poblacion_ayacucho = 658300
positivos_ayacucho = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "AYACUCHO"].shape)[0]
positivos_hombres_ayacucho = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AYACUCHO") &(casos_positivos['SEXO'] == "MASCULINO")].shape)[0]
positivos_mujeres_ayacucho = list(casos_positivos[(casos_positivos['DEPARTAMENTO'] == "AYACUCHO") &(casos_positivos['SEXO'] == "FEMENINO")].shape)[0]
fallecidos_ayacucho = list(casos_fallecidos[casos_fallecidos['DEPARTAMENTO'] == "AYACUCHO"].shape)[0]
fallecidos_hombres_ayacucho  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AYACUCHO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho  = list(casos_fallecidos[(casos_fallecidos['DEPARTAMENTO'] == "AYACUCHO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_ayacucho_huamanga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMANGA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_huamanga = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUAMANGA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_ayacucho_cangallo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANGALLO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_cangallo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "CANGALLO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_ayacucho_huanca_sancos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCA SANCOS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_huanca_sancos = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANCA SANCOS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_ayacucho_huanta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANTA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_huanta = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "HUANTA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_ayacucho_mar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA MAR") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_mar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LA MAR") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_ayacucho_lucanas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUCANAS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_lucanas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "LUCANAS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_ayacucho_parinacochas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARINACOCHAS") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_parinacochas = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PARINACOCHAS") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_ayacucho_paucar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCAR DEL SARA SARA") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_paucar = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "PAUCAR DEL SARA SARA") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]


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
fallecidos_hombres_ayacucho_sucre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SUCRE") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_sucre = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "SUCRE") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_ayacucho_victor_fajardo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VICTOR FAJARDO") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_victor_fajardo = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VICTOR FAJARDO") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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
fallecidos_hombres_ayacucho_vilcas_huaman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VILCAS HUAMAN") &(casos_fallecidos['SEXO'] == "MASCULINO")].shape)[0]
fallecidos_mujeres_ayacucho_vilcas_huaman = list(casos_fallecidos[(casos_fallecidos['PROVINCIA'] == "VILCAS HUAMAN") &(casos_fallecidos['SEXO'] == "FEMENINO")].shape)[0]

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


ayacucho = {
      "name": "Ayacucho",
      "poblacion": poblacion_ayacucho,
      "positivos": positivos_ayacucho,
      "hombres_infectados": positivos_hombres_ayacucho,
      "mujeres_infectados": positivos_mujeres_ayacucho,
      "fallecidos": fallecidos_ayacucho,
      "hombres_fallecidos": fallecidos_hombres_ayacucho,
      "mujeres_fallecidos": fallecidos_mujeres_ayacucho,
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
          {"name": "Huamanga", "positivos": positivos_ayacucho_huamanga,"poblacion": poblacion_ayacucho_huamanga , "hombres_infectados": positivos_hombres_ayacucho_huamanga,"mujeres_infectados": positivos_mujeres_ayacucho_huamanga, "fallecidos": fallecidos_ayacucho_huamanga, "hombres_fallecidos": fallecidos_hombres_ayacucho_huamanga,
      "mujeres_fallecidos": fallecidos_mujeres_ayacucho_huamanga, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_huamanga,
       "infancia": fallecidos_infancia_ayacucho_huamanga,
       "adolescencia": fallecidos_adolescencia_ayacucho_huamanga,
       "juventud": fallecidos_juventud_ayacucho_huamanga,
       "adultez": fallecidos_adultez_ayacucho_huamanga,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_huamanga
      }},

          {"name": "Cangallo", "positivos": positivos_ayacucho_cangallo,"poblacion": poblacion_ayacucho_cangallo , "hombres_infectados": positivos_hombres_ayacucho_cangallo,"mujeres_infectados": positivos_mujeres_ayacucho_cangallo, "fallecidos": fallecidos_ayacucho_cangallo, "hombres_fallecidos": fallecidos_hombres_ayacucho_cangallo,
      "mujeres_fallecidos": fallecidos_mujeres_ayacucho_cangallo, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_cangallo,
       "infancia": fallecidos_infancia_ayacucho_cangallo,
       "adolescencia": fallecidos_adolescencia_ayacucho_cangallo,
       "juventud": fallecidos_juventud_ayacucho_cangallo,
       "adultez": fallecidos_adultez_ayacucho_cangallo,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_cangallo
      }},

        {"name": "Huanca Sancos", "positivos": positivos_ayacucho_huanca_sancos,"poblacion": poblacion_ayacucho_huanca_sancos , "hombres_infectados": positivos_hombres_ayacucho_huanca_sancos,"mujeres_infectados": positivos_mujeres_ayacucho_huanca_sancos, "fallecidos": fallecidos_ayacucho_huanca_sancos, "hombres_fallecidos": fallecidos_hombres_ayacucho_huanca_sancos,
      "mujeres_fallecidos": fallecidos_mujeres_ayacucho_huanca_sancos, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_huanca_sancos,
       "infancia": fallecidos_infancia_ayacucho_huanca_sancos,
       "adolescencia": fallecidos_adolescencia_ayacucho_huanca_sancos,
       "juventud": fallecidos_juventud_ayacucho_huanca_sancos,
       "adultez": fallecidos_adultez_ayacucho_huanca_sancos,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_huanca_sancos
      }},

          {"name": "Huanta", "positivos": positivos_ayacucho_huanta, "poblacion": poblacion_ayacucho_huanta, "hombres_infectados": positivos_hombres_ayacucho_huanta, "mujeres_infectados": positivos_mujeres_ayacucho_huanta, "fallecidos": fallecidos_ayacucho_huanta, "hombres_fallecidos": fallecidos_hombres_ayacucho_huanta,
           "mujeres_fallecidos": fallecidos_mujeres_ayacucho_huanta, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_huanta,
       "infancia": fallecidos_infancia_ayacucho_huanta,
       "adolescencia": fallecidos_adolescencia_ayacucho_huanta,
       "juventud": fallecidos_juventud_ayacucho_huanta,
       "adultez": fallecidos_adultez_ayacucho_huanta,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_huanta
      }},

          {"name": "La Mar", "positivos": positivos_ayacucho_mar,"poblacion": poblacion_ayacucho_mar , "hombres_infectados": positivos_hombres_ayacucho_mar,"mujeres_infectados": positivos_mujeres_ayacucho_mar, "fallecidos": fallecidos_ayacucho_mar, "hombres_fallecidos": fallecidos_hombres_ayacucho_mar,
           "mujeres_fallecidos": fallecidos_mujeres_ayacucho_mar, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_mar,
       "infancia": fallecidos_infancia_ayacucho_mar,
       "adolescencia": fallecidos_adolescencia_ayacucho_mar,
       "juventud": fallecidos_juventud_ayacucho_mar,
       "adultez": fallecidos_adultez_ayacucho_mar,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_mar
      }},

          {"name": "Lucanas", "positivos": positivos_ayacucho_lucanas,"poblacion": poblacion_ayacucho_lucanas , "hombres_infectados": positivos_hombres_ayacucho_lucanas,"mujeres_infectados": positivos_mujeres_ayacucho_lucanas, "fallecidos": fallecidos_ayacucho_lucanas, "hombres_fallecidos": fallecidos_hombres_ayacucho_lucanas,
           "mujeres_fallecidos": fallecidos_mujeres_ayacucho_lucanas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_lucanas,
       "infancia": fallecidos_infancia_ayacucho_lucanas,
       "adolescencia": fallecidos_adolescencia_ayacucho_lucanas,
       "juventud": fallecidos_juventud_ayacucho_lucanas,
       "adultez": fallecidos_adultez_ayacucho_lucanas,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_lucanas
      }},

          {"name": "Parinacochas", "positivos": positivos_ayacucho_parinacochas,"poblacion": poblacion_ayacucho_parinacochas , "hombres_infectados": positivos_hombres_ayacucho_parinacochas,"mujeres_infectados": positivos_mujeres_ayacucho_parinacochas, "fallecidos": fallecidos_ayacucho_parinacochas, "hombres_fallecidos": fallecidos_hombres_ayacucho_parinacochas,
           "mujeres_fallecidos": fallecidos_mujeres_ayacucho_parinacochas, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_parinacochas,
       "infancia": fallecidos_infancia_ayacucho_parinacochas,
       "adolescencia": fallecidos_adolescencia_ayacucho_parinacochas,
       "juventud": fallecidos_juventud_ayacucho_parinacochas,
       "adultez": fallecidos_adultez_ayacucho_parinacochas,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_parinacochas
      }},

          {"name": "Paucar del Sara Sara", "positivos": positivos_ayacucho_paucar,"poblacion": poblacion_ayacucho_paucar , "hombres_infectados": positivos_hombres_ayacucho_paucar,"mujeres_infectados": positivos_mujeres_ayacucho_paucar, "fallecidos": fallecidos_ayacucho_paucar, "hombres_fallecidos": fallecidos_hombres_ayacucho_paucar,
           "mujeres_fallecidos": fallecidos_mujeres_ayacucho_paucar, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_paucar,
       "infancia": fallecidos_infancia_ayacucho_paucar,
       "adolescencia": fallecidos_adolescencia_ayacucho_paucar,
       "juventud": fallecidos_juventud_ayacucho_paucar,
       "adultez": fallecidos_adultez_ayacucho_paucar,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_paucar
      }},

          {"name": "Sucre", "positivos": positivos_ayacucho_sucre,"poblacion": poblacion_ayacucho_sucre , "hombres_infectados": positivos_hombres_ayacucho_sucre,"mujeres_infectados": positivos_mujeres_ayacucho_sucre, "fallecidos": fallecidos_ayacucho_sucre, "hombres_fallecidos": fallecidos_hombres_ayacucho_sucre,
           "mujeres_fallecidos": fallecidos_mujeres_ayacucho_sucre, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_sucre,
       "infancia": fallecidos_infancia_ayacucho_sucre,
       "adolescencia": fallecidos_adolescencia_ayacucho_sucre,
       "juventud": fallecidos_juventud_ayacucho_sucre,
       "adultez": fallecidos_adultez_ayacucho_sucre,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_sucre
      }},

          {"name": "Victor Fajardo", "positivos": positivos_ayacucho_victor_fajardo,"poblacion": poblacion_ayacucho_victor_fajardo , "hombres_infectados": positivos_hombres_ayacucho_victor_fajardo,"mujeres_infectados": positivos_mujeres_ayacucho_victor_fajardo, "fallecidos": fallecidos_ayacucho_victor_fajardo, "hombres_fallecidos": fallecidos_hombres_ayacucho_victor_fajardo,
           "mujeres_fallecidos": fallecidos_mujeres_ayacucho_victor_fajardo,"type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_victor_fajardo,
       "infancia": fallecidos_infancia_ayacucho_victor_fajardo,
       "adolescencia": fallecidos_adolescencia_ayacucho_victor_fajardo,
       "juventud": fallecidos_juventud_ayacucho_victor_fajardo,
       "adultez": fallecidos_adultez_ayacucho_victor_fajardo,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_victor_fajardo
      }},

          {"name": "Vilcas Huaman", "positivos": positivos_ayacucho_vilcas_huaman,"poblacion": poblacion_ayacucho_vilcas_huaman , "hombres_infectados": positivos_hombres_ayacucho_vilcas_huaman,"mujeres_infectados": positivos_mujeres_ayacucho_vilcas_huaman, "fallecidos": fallecidos_ayacucho_vilcas_huaman, "hombres_fallecidos": fallecidos_hombres_ayacucho_vilcas_huaman,
           "mujeres_fallecidos": fallecidos_mujeres_ayacucho_vilcas_huaman, "type": "Provincia", "etapa_de_vida_fallecidos": {
       "primera_infancia": fallecidos_preinfancia_ayacucho_vilcas_huaman,
       "infancia": fallecidos_infancia_ayacucho_vilcas_huaman,
       "adolescencia": fallecidos_adolescencia_ayacucho_vilcas_huaman,
       "juventud": fallecidos_juventud_ayacucho_vilcas_huaman,
       "adultez": fallecidos_adultez_ayacucho_vilcas_huaman,
       "persona_mayor": fallecidos_persona_mayor_ayacucho_vilcas_huaman
      }}
      ]
    }
    
print(json.dumps(ayacucho));
sys.stdout.flush();
