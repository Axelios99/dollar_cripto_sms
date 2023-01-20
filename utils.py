import json
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from twilio.rest import Client
from scripts_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER_SMS, PHONE_NUMBER_WHATSAPP, EXCHANGE_TOKEN
import pandas as pd
import numpy as np


def get_dollar_today(url_dollar):
    try:
        payload = {}
        headers= {
        "apikey": EXCHANGE_TOKEN
        }
        response = requests.request("GET", url_dollar, headers=headers, data = payload)
        status_code = response.status_code
        result = response.json()
        price_dollar = result['result']
    except Exception as e:
        print(e)    
    return price_dollar



def get_df_criptos(url_criptos):
    try:
        df_criptos = pd.read_json(url_criptos)
        df_criptos = df_criptos[['id', 'symbol', 'name', 'current_price', 'high_24h', 'low_24h', 'price_change_24h', 'price_change_percentage_24h']]
        df_send = df_criptos.rename(columns ={'price_change_percentage_24h':'variation_porcent'})
        df_send = df_send[['name', 'current_price', 'variation_porcent']]
        df_send.set_index('name', inplace= True)
    except Exception as e:
        print(e)
    return df_send


def send_sms(price_dollar, df_criptos):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='\n¡Hola! \n \n El valor del dolar hoy en COP es: '+str(price_dollar)+' \n \n  El precio de la cripto divisa es: \n \n ' + str(df_criptos),
        from_=PHONE_NUMBER_SMS,
        to='+573228784083'
    )
    return (message.sid)



def send_whatsapp(price_dollar, df_criptos):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                body='\n¡Hola! \n \n El valor del dolar hoy en COP es: '+str(price_dollar)+' \n \n  El precio de la cripto divisa es: \n \n ' + str(df_criptos),
                                from_='whatsapp:'+PHONE_NUMBER_WHATSAPP,
                                to='whatsapp:+573228784083'
                            )
    return (message.sid)

    