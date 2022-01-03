# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name) -> None:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def run_me() -> None:
    import requests
    response = requests.get(url='https://www.google.by/')
    print(response.status_code)
    print('Working')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('asd')
    run_me()
    while True:
        pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
