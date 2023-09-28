import requests



api_url='https://64ba521b5e0670a501d5f92c.mockapi.io/user/'
# def api_fxn():
data=requests.get(api_url).json()
for i in data:
    print(i.name)
