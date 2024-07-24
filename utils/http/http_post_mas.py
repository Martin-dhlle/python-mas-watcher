import requests

from config.request_config import API, API_MAS_KEY

def http_post_mas(json_str: str, file_path: str):
    '''
    Requête en post afin de créer des affranchissements MAS
    dans la base de données
    '''
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {API_MAS_KEY}'}
    response = requests.post(API, headers=headers, data=json_str)
    
    if response.ok():
        print(f"Les données du fichier d'affranchissements MAS {file_path} ont bien été sauvegardés")
    else:
        print(f"erreur status code : {response.status_code}")