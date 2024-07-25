import requests

from config.request_config import API, MAS_API_KEY
from utils.log_entry_generator import generate_log

def http_post_mas(json_str: str, file_path: str):
    '''
    Requête en post afin de créer des affranchissements MAS
    dans la base de données
    '''        
    headers = {'Content-Type': 'application/json', 'mas-api-key': MAS_API_KEY}
    response = requests.post(f'{API}/mas', headers=headers, data=json_str)

    if response.ok:
        generate_log(0, 3, file_path)
    else:
        generate_log(1, 4, response.status_code)