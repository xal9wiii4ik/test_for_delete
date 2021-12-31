import requests


def run_me():
    response = requests.get(url='https://www.google.by/')
    print(response.status_code)
    print('Working')


run_me()
