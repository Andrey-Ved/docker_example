import requests
import json

from time import sleep

from ui import API_PORT, ROWS_NUMBER


def send_for_processing(row, api_port):
    try:
        r = requests.post(
            url=f'http://API:{api_port}/save/',
            data=json.dumps({"data": row})
        )
        print('ui - ', r.json())
    except Exception as e:
        print('ui - ', e)


def main():

    for i in range(ROWS_NUMBER):
        sleep(2)

        row = f'test {i}'
        print('\n**************\n')

        send_for_processing(row, API_PORT)


if __name__ == '__main__':
    main()
