import requests


def getData():
    try:
        url = 'http://timportuese.pythonanywhere.com/data'
        x = requests.post(url)
        return x.text
    except Exception as e:
        return None
