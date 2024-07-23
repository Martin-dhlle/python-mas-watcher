from http.client import HTTPSConnection

from config.request import API

def http_post_mas():
    connection = HTTPSConnection(API)
    connection.request('POST', '/mas')
    return