# Companies_places

![Image text](https://www.viajarsanfrancisco.com/img/que-visitar-en-san-francisco.jpg)




En este análisis tratamos de buscar la mejor localización para nuestra empresa. Para ello nos bajaremos emplazamientos de una API, y con ella haremos un ranking para encotrar la mejor zona.




## Table of Contents
1. [Información general](#Informacion-general)
2. [Datos](#Datos)
3. [Tecnologías](#Tecnologías)
4. [Librerías](#Librerías)
## Información general
***
Para el dataset hemos utilizado datos de empresas de todo el mundo, las cuales filtraremos según algunos criterios.
Para la API hemos utilizado Foursquare. Nos da lugares cercanos según la localización que le pasemos.
## Datos
***
Los datos que recibimos de la API van a sufrir modificaciones hasta conseguir el formato de dataframe.

Data cleaning:
- Crear dataframes
- Concatenar dataframes
- Unir todos los dataframes de las ciudades

## Tecnologias
***
Una lista de las librerías utilizadas en elproyecto:
* [Jupyter Notebook](https://jupyter.org/) : Version 6.1.4
* [Python](https://www.python.org/): Version 3.8.5
* [Visual Studio Code](https://code.visualstudio.com/)
## Librerías
***
Una pequeña introducción a las librerías usadas: 
```
import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv()
import src.FuncionesAPI as fa
from functools import reduce
import operator
from pandas import json_normalize
import numpy as np
from keplergl import KeplerGl
```

