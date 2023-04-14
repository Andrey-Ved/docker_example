import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from db import DB_PORT, DATA_FILE


class Row(BaseModel):
    data: str


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "It's date base service"}


@app.post("/create/")
async def create_record(row: Row):
    writing_to_file(
        data=row.data,
        file=DATA_FILE,
        new=False
    )
    return row


def writing_to_file(data, file, new=False):
    current_datetime = datetime.now()
    line = f'{current_datetime} - {data}'
    print('db - ', line)
    print(f'db - file = {file}')

    file_opening_mode = 'w' if new else 'a'

    with open(file, file_opening_mode) as f:
        f.write(f'{line} \n')


def main():
    writing_to_file(
        data=f'start file',
        file=DATA_FILE,
        new=True
    )
    uvicorn.run(app, host="0.0.0.0", port=DB_PORT)
    # http://127.0.0.1:8001/docs


if __name__ == "__main__":
    main()
