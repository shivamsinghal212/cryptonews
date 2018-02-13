from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ico/',views.ico, name="ico"),
    path('upcoming_ico/',views.upcoming_ico, name="upcoming_ico"),
    path('convert/',views.get_rates, name="convert"),
    path('live-trades/', views.get_live_trades, name="trades"),
    path('search/', views.get_news_search, name="search"),
]
