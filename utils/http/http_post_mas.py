from http.client import HTTPSConnection

from config.request import API
from utils.models.affranchissement_mas import AffranchissementMas

def http_post_mas(affranchissements_mas: list[AffranchissementMas]):
    connection = HTTPSConnection(API)
    connection.request('POST', url='/mas', headers=[""])
    return