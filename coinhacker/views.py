from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    data = {}
    data["coin_data"] = get_data()
    return render(request,"index.html", data)



def get_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"

    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print(e)
        data = dict()

    return data
