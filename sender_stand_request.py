import configuration
import requests
import data

#Функция для создания заказа
def post_new_order(body):
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    return requests.post(url, json=body, timeout=7)
#Функция получения заказа
def get_track_order(track):
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    return requests.get(url, params={"t": str(track)}, timeout=7)
