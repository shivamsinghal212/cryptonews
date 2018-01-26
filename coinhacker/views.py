from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    data = {}
    data["coin_data"] = get_data()
    data["coin_news"] = get_news()['articles']
    data["top_5"] = get_top_5()
    data["bottom_5"] = get_bottom_5()
    return render(request,"cointable.html", data)

def ico(request):
    data = {}
    data["live_ico"] = get_live_ico()
    return render(request,"icotable.html",data)

def upcoming_ico(request):
    data = {}
    data["upcoming_ico"] = get_upcoming_ico()
    return render(request,"upcoming_ico.html",data)

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

def get_live_ico():
    data ={}
    api_url = "https://api.icowatchlist.com/public/v1/live"
    try:
        data = requests.get(api_url).json()
        for value in data.values():
            for v in value.values():
                return v
    except Exception as e:
        print(e)

def get_upcoming_ico():
        data ={}
        api_url = "https://api.icowatchlist.com/public/v1/upcoming"
        try:
            data = requests.get(api_url).json()
            for value in data.values():
                for v in value.values():
                    return v
        except Exception as e:
            print(e)

@csrf_exempt
def get_rates(request):
    if request.method=='GET':
        fr = str(request.GET.get('fr'))
        to = str(request.GET.get('to'))
        api_url = "https://api.cryptonator.com/api/full/"+fr+"-"+to
        data = requests.get(api_url).json()
        context={'data':list(data.values())[0]}
        #template = loader.get_template('convert.html')
        return render(request,"convert.html",context)
    else:
                #if post request is not true
                #returing the form template
        template = loader.get_template('convert.html')
        return HttpResponse(template.render())
