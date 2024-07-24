import os
from dotenv import load_dotenv

load_dotenv('.env.local')

API = os.getenv('API')
API_MAS_KEY = os.getenv('API_MAS_KEY')