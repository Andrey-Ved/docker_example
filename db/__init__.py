import os
from dotenv import load_dotenv


load_dotenv()


DATA_FILE = os.path.sep.join(
    __file__.split(os.path.sep)[:-2]
    + [
        os.getenv('DATA_DIR'),
        os.getenv('DATA_FILE')
    ])

DB_PORT = int(os.getenv('DB_PORT'))
