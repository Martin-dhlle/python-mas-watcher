import os
from dotenv import load_dotenv

load_dotenv('.env.local')

API = os.getenv('API')
MAS_API_KEY = os.getenv('MAS_API_KEY')