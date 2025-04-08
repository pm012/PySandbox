import requests


def get_provider_info():
    my_provider_info = requests.get("https://ipinfo.io")
    print(my_provider_info.text)


if __name__ == "__main__":
    get_provider_info()
    