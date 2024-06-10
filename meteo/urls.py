from django.urls import path
from . import views

app_name = 'meteo'
urlpatterns = [
    path('', views.today_weather, name='today_weather'),
    path('five-days/', views.five_days_weather, name='five_days_weather'),
    path('today-forecast/', views.today_forecast, name='today_forecast'),
    path('five-days-forecast/', views.five_days_forecast, name='five_days_forecast'),
    path('cities-list/', views.cities_list, name='cities_list'),
]
