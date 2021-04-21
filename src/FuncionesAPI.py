import requests 
import json
import os
import pandas as pd
from dotenv import load_dotenv
from functools import reduce
import operator
import geopandas as gdp
import shapely


from pymongo import MongoClient

def get_data (latitude, longitude, url_query, *args):
    d = {}
    tok1= os.getenv("Client_Id")
    tok2= os.getenv("Client_Secret")
    
    for i in args: 
        parametros = {"client_id" : tok1,
                  "client_secret" : tok2,
                  "v": "20180323",
                  "ll": f"{latitude},{longitude}", 
                  "query":i,
                  "limit": 100}  

        response = requests.get(url= url_query, params=parametros)
        data = json.loads(response.text)        
        d[i] = data
        
    return d

def getFromDict(diccionario,mapa):
    return reduce (operator.getitem,mapa,diccionario)

def crear_dataframe(diccionario):
    mapa_nombre =  ["venue", "name"]
    mapa_latitud = ["venue", "location", "lat"]
    mapa_longitud = ["venue", "location", "lng"]
    lista = []
    for dic in diccionario:
        paralista = {}
        paralista["name"] = getFromDict(dic, mapa_nombre)
        paralista["latitud"]= getFromDict(dic, mapa_latitud)
        paralista["longitud"] = getFromDict(dic,mapa_longitud)
        lista.append(paralista)
        df = pd.DataFrame(lista)
    return df

def clean_dataframes(df_concat,city):
    counter_ = df_concat.groupby("categoria").size()
    df_counter = pd.DataFrame(counter_)
    colname = [city]
    df_counter.columns = colname
    df_counter = df_counter.transpose()
    return df_counter

def puntuacion(df_concat):
    df_concat.loc[df_concat.bar < 45, "bar"]= 2
    df_concat.loc[df_concat.bar > 45, "bar"]= 3
    df_concat.loc[df_concat.Starbucks == 50, "Starbucks"]= 1
    df_concat.loc[df_concat.Starbucks == 51, "Starbucks"]= 2
    df_concat.loc[df_concat.Starbucks > 51, "Starbucks"]= 3
    df_concat.loc[df_concat.basket < 30, "basket"]= 1
    df_concat.loc[df_concat.basket == 36, "basket"]= 2
    df_concat.loc[df_concat.basket >36, "basket"]= 3
    df_concat.loc[df_concat.nursery < 10, "nursery"]= 1
    df_concat.loc[df_concat.nursery == 18, "nursery"]= 3
    df_concat.loc[df_concat.nursery > 10, "nursery"]= 2
    df_concat.loc[df_concat.taxi < 3, "taxi"]= 1
    df_concat.loc[df_concat.taxi == 3, "taxi"]= 2
    df_concat.loc[df_concat.taxi > 3, "taxi"]= 3
    df_concat.loc[df_concat.vegan < 10, "vegan"]= 1
    df_concat.loc[df_concat.vegan > 30, "vegan"]= 3
    df_concat.loc[df_concat.vegan > 10, "vegan"]= 2
    return df_concat