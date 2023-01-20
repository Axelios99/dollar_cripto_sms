"""
*********************************************************************************************************
* Author = @Alexander Ladino                                                                            *
* Date = '19/01/2023'                                                                                   *
* Description = Consulta de dollar en Colombia, consulta de precio de las criptomonedas y envio por SMS *
*********************************************************************************************************
"""

import json
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

url_dollar = 'https://www.datos.gov.co/resource/32sa-8pi3.json'
response = requests.get(url_dollar).json()