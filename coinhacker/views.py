from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    data = {}
    data["coin_data"] = get_data()
    data["coin_news"] = get_news()['articles']
    data["top_5"] = get_top_5()
    data["bottom_5"] = get_bottom_5()
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

#get top 5 gainers and losers in last 24 hours
def get_price_all():

    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=0"
    name=[]
    price=[]

    try:
        data = requests.get(api_url).json()
        for key in data:
            for k,v in key.items():
                if k=='name':
                    name.append(v)
                elif k=='percent_change_24h' and v==None:
                    price.append(0)
                elif k=='percent_change_24h':
                    price.append(float(v))
        sorted_d = sorted(dict(zip(name,price)).items(), key=lambda x: x[1],reverse=True)
        return sorted_d
    except Exception as e:
        print(e)

def get_top_5():
    top_5=[]
    top_5 = get_price_all()[:6]
    return top_5

def get_bottom_5():
    bottom_5 = []
    bottom_5 = get_price_all()[-6:]
    return bottom_5
