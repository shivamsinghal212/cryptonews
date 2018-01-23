from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    data = {}
    data["coin_data"] = get_data()
    data["coin_news"] = get_news()['articles']
    return render(request,"cointable.html", data)





def get_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=40"

    try:
        data = requests.get(api_url).json()
    except Exception as e:
        print(e)
        data = dict()

    return data


def get_news():
    api_url = "https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&apiKey=99fd007d1e724a5791ae6a018caecbc6"

    try:
        data = requests.get(api_url).json()
        return data
    except Exception as e:
        print(e)
