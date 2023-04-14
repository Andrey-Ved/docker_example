import requests
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

from api import API_PORT, DB_PORT


class Row(BaseModel):
    data: str


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "It's api service"}


@app.post("/save/")
async def create_record(row: Row):
    await save_in_db(DB_PORT, row)
    return row


async def save_in_db(db_port, row):
    try:
        r = requests.post(
            url=f'http://DB:{db_port}/create/',
            data=row.json()
        )
        print('api - ', r.json())
    except Exception as e:
        print('api - ', e)


def main():
    uvicorn.run(app, host="0.0.0.0", port=API_PORT)
    # http://127.0.0.1:8000/docs


if __name__ == "__main__":
    main()
