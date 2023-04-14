import os
from dotenv import load_dotenv


load_dotenv()


ROWS_NUMBER = int(os.getenv('ROWS_NUMBER'))

API_PORT = int(os.getenv('API_PORT'))
