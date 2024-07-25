import requests

from config.request_config import API, MAS_API_KEY

def http_post_mas(json_str: str, file_path: str):
    '''
    Requête en post afin de créer des affranchissements MAS
    dans la base de données
    '''        
    headers = {'Content-Type': 'application/json', 'mas-api-key': MAS_API_KEY}
    response = requests.post(f'{API}/mas', headers=headers, data=json_str)

    if response.ok:
        print(f"Les données du fichier d'affranchissements MAS {file_path} ont bien été sauvegardés")
    else:
        print(f"erreur status code : {response.status_code}")