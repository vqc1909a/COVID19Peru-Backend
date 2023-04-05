import requests
import json
import sys
from bs4 import BeautifulSoup
from casos import casos_positivos, casos_fallecidos


poblacion_total = 33028673

#!total_positivos: esto me obtiene una tupla de filas y columnas, por eso lo convierto en un array
total_positivos = list(casos_positivos.shape)[0]
#!total_positivos_hombres
total_positivos_hombres = list(casos_positivos[casos_positivos['SEXO'] == "MASCULINO"].shape)[0]

#!total_positivos_mujeres
total_positivos_mujeres = list(casos_positivos[casos_positivos['SEXO'] == "FEMENINO"].shape)[0]


#!total_fallecidos:
total_fallecidos = list(casos_fallecidos.shape)[0]

#!total_fallecidos_hombre:
total_fallecidos_hombres = list(
    casos_fallecidos[casos_fallecidos['SEXO'] == "MASCULINO"].shape)[0]

#!total_fallecidos_mujeres:
total_fallecidos_mujeres = list(
    casos_fallecidos[casos_fallecidos['SEXO'] == "FEMENINO"].shape)[0]



#!total_poblacion:
# total_poblacion = poblacion_total[poblacion_total['Unnamed: 1'] == "PERU"].iloc[0,2]
total_poblacion = poblacion_total
#!positivos departamento loreto
positivos_loreto = list(casos_positivos[casos_positivos['DEPARTAMENTO'] == "LORETO"].shape)[0]

#!positivos departamento amazonas
positivos_amazonas = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "AMAZONAS"].shape)[0]


#!positivos departamento tumbes
positivos_tumbes = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "TUMBES"].shape)[0]


#!positivos departamento piura
positivos_piura = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "PIURA"].shape)[0]


#!positivos departamento lambayeque
positivos_lambayeque = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "LAMBAYEQUE"].shape)[0]


#!positivos departamento Cajamarca
positivos_cajamarca = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "CAJAMARCA"].shape)[0]



#!positivos departamento La Libertad
positivos_libertad = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "LA LIBERTAD"].shape)[0]


#!positivos departamento ancash
positivos_ancash = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "ANCASH"].shape)[0]

#!positivos departamento san martin
positivos_sanmartin = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "SAN MARTIN"].shape)[0]



#!positivos departamento huanuco
positivos_huanuco = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "HUANUCO"].shape)[0]



#!positivos departamento ucayali
positivos_ucayali = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "UCAYALI"].shape)[0]



#!positivos departamento pasco
positivos_pasco = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "PASCO"].shape)[0]



#!positivos departamento lima
positivos_lima = list(
    casos_positivos[(casos_positivos['DEPARTAMENTO'] == "LIMA") | (casos_positivos['DEPARTAMENTO'] == "LIMA REGION")].shape)[0]


#!positivos departamento junin
positivos_junin = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "JUNIN"].shape)[0]



#!positivos departamento huancavelica
positivos_huancavelica = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "HUANCAVELICA"].shape)[0]



#!positivos departamento ica
positivos_ica = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "ICA"].shape)[0]


#!positivos departamento ayacucho
positivos_ayacucho = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "AYACUCHO"].shape)[0]

#!positivos departamento apurimac
positivos_apurimac = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "APURIMAC"].shape)[0]


#!positivos departamento cusco
positivos_cusco = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "CUSCO"].shape)[0]

#!positivos departamento madre de dios
positivos_madrededios = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "MADRE DE DIOS"].shape)[0]


#!positivos departamento puno
positivos_puno = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "PUNO"].shape)[0]

#!positivos departamento arequipa
positivos_arequipa = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "AREQUIPA"].shape)[0]


#!positivos departamento moquegua
positivos_moquegua = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "MOQUEGUA"].shape)[0]


#!positivos departamento tacna
positivos_tacna = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "TACNA"].shape)[0]

#!positivos departamento callao

positivos_callao = list(
    casos_positivos[casos_positivos['DEPARTAMENTO'] == "CALLAO"].shape)[0]

#!Fallecidos por etapa de vida
#!0 a 5 años (Primera infancia o Bebes o Infancia Temprana)
fallecidos_preinfancia = list(casos_fallecidos[(casos_fallecidos['EDAD_DECLARADA'] >= 0) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 5)].shape)[0]

#!6 a 11 años (Infancia o Niños o Niñez)
fallecidos_infancia = list(casos_fallecidos[(casos_fallecidos['EDAD_DECLARADA'] >= 6) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 11)].shape)[0]

#!12 a 18 años (Adolescencia o Adolescentes)
fallecidos_adolescencia = list(casos_fallecidos[(casos_fallecidos['EDAD_DECLARADA'] >= 12) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 18)].shape)[0]

#!19 a 26 años (Juventud o Jóvenes)
fallecidos_juventud = list(casos_fallecidos[(casos_fallecidos['EDAD_DECLARADA'] >= 19) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 26)].shape)[0]

#!27 a 59 años (Adultez o Adultos)
fallecidos_adultez = list(casos_fallecidos[(casos_fallecidos['EDAD_DECLARADA'] >= 27) & (
    casos_fallecidos['EDAD_DECLARADA'] <= 59)].shape)[0]

#!60 a mas (Persona Mayor o Ancianos)
fallecidos_persona_mayor = list(
    casos_fallecidos[(casos_fallecidos['EDAD_DECLARADA'] >= 60)].shape)[0]

casos_generales = {
    "name": "peru",
    "poblacion": total_poblacion,
    "positivos": total_positivos,
    "hombres_infectados": total_positivos_hombres,
    "mujeres_infectados": total_positivos_mujeres,
    "fallecidos": total_fallecidos,
    "hombres_fallecidos": total_fallecidos_hombres,
    "mujeres_fallecidos": total_fallecidos_mujeres,
    "etapa_de_vida_fallecidos": {
        "primera_infancia": fallecidos_preinfancia,
        "infancia": fallecidos_infancia,
        "adolescencia": fallecidos_adolescencia,
        "juventud": fallecidos_juventud,
        "adultez": fallecidos_adultez,
        "persona_mayor": fallecidos_persona_mayor
    },
    "mapa_hijos": [
        positivos_amazonas,
        positivos_ancash,
        positivos_apurimac,
        positivos_arequipa,
        positivos_ayacucho,
        positivos_cajamarca,
        positivos_callao, 
        positivos_cusco,
        positivos_huancavelica,
        positivos_huanuco,
        positivos_ica,
        positivos_junin,
        positivos_libertad,
        positivos_lambayeque,
        positivos_lima,
        positivos_loreto,
        positivos_madrededios,
        positivos_moquegua,
        positivos_pasco,
        positivos_piura,
        positivos_puno,
        positivos_sanmartin,
        positivos_tacna,
        positivos_tumbes,
        positivos_ucayali
    ]
}

print(json.dumps(casos_generales));
sys.stdout.flush();





















