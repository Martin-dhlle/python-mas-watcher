from http.client import HTTPSConnection

from config.request import API
from utils.models.affranchissement_mas import AffranchissementMas

def http_post_mas(json_str: str):
    headers = {'Content-Type': 'application/json'}
    connection = HTTPSConnection(API)
    connection.request('POST', url='/mas', headers=headers, body=json_str)
    return