import os
from dotenv import load_dotenv


load_dotenv()


API_PORT = int(os.getenv('API_PORT'))

DB_PORT = int(os.getenv('DB_PORT'))
