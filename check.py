import requests


def run_me() -> None:
    response = requests.get(url='https://www.google.by/')
    print(response.status_code)
    print('Working')


run_me()
