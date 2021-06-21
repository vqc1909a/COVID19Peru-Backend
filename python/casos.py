import pandas as pd
from urllib.request import Request, urlopen  # Python 3


req1 = Request("https://cloud.minsa.gob.pe/s/Y8w3wHsEdYQSZRp/download");
req1.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
casos_positivos = pd.read_csv(urlopen(req1), sep=";")
 
req2 = Request("https://cloud.minsa.gob.pe/s/Md37cjXmjT9qYSa/download");
req2.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
casos_fallecidos = pd.read_csv(urlopen(req2), encoding = "ISO-8859-1", sep=";")



