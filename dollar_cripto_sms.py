"""
*********************************************************************************************************
* Author = @Alexander Ladino                                                                            *
* Date = '19/01/2023'                                                                                   *
* Description = Consulta de dollar en Colombia, consulta de precio de las criptomonedas y envio por SMS *
*********************************************************************************************************
"""


from utils import get_dollar_today, get_df_criptos, send_sms, send_whatsapp
import pandas as pd
import numpy as np



url_dollar = "https://api.apilayer.com/exchangerates_data/convert?to=COP&from=USD&amount=1"
url_criptos = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Cethereum%2Cdogecoin%2Ctether%2Ccardano%2Ctron%2Cchainlink%2Ceos%2Cdai%2Cfrax&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=24'



price_dollar = get_dollar_today(url_dollar)
df_criptos = get_df_criptos(url_criptos)

response_sms = send_sms(price_dollar, df_criptos)
response_whatsapp = send_whatsapp(price_dollar, df_criptos)



    

