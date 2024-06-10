from django.shortcuts import render
import requests
from django.http import JsonResponse

URL_TIPOS_CLIMA_IPMA = 'https://api.ipma.pt/open-data/weather-type-classe.json'

def get_weather_types_json():
    response = requests.get(URL_TIPOS_CLIMA_IPMA)
    return response.json() if response.status_code == 200 else None

def today_weather(request):
    city_id = 1110600
    weather_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    weather_types_response = get_weather_types_json()

    weather_response = requests.get(weather_url).json()

    if not weather_types_response:
        return JsonResponse({'error': 'Não foi possível obter os tipos de clima'}, status=500)

    weather_types = {wt['idWeatherType']: wt['descWeatherTypePT'] for wt in weather_types_response['data']}

    today_forecast = weather_response['data'][0]
    weather_type_id = today_forecast['idWeatherType']

    weather_description = weather_types.get(weather_type_id, 'Descrição indisponível')

    if weather_type_id < 10:
        weather_icon = f"/static/meteo/w_ic_d_0{weather_type_id}anim.svg"
    else:
        weather_icon = f"/static/meteo/w_ic_d_{weather_type_id}anim.svg"

    context = {
        'city_name': 'Lisboa',
        'temp_min': today_forecast['tMin'],
        'temp_max': today_forecast['tMax'],
        'date': today_forecast['forecastDate'],
        'weather_description': weather_description,
        'icon': weather_icon
    }

    return render(request, 'meteo/today_weather.html', context)

def five_days_weather(request):
    city_id = request.GET.get('city_id', 1110600)
    weather_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'

    weather_response = requests.get(weather_url).json()
    cities_response = requests.get(cities_url).json()
    weather_types_response = get_weather_types_json()

    if not weather_types_response:
        return JsonResponse({'error': 'Não foi possível obter os tipos de clima'}, status=500)

    weather_types = {wt['idWeatherType']: wt['descWeatherTypePT'] for wt in weather_types_response['data']}

    forecasts = weather_response['data'][:5]
    for forecast in forecasts:
        weather_type_id = forecast['idWeatherType']
        forecast['weather_description'] = weather_types.get(weather_type_id, 'Descrição indisponível')

        if weather_type_id < 10:
            forecast['icon'] = f"/static/meteo/w_ic_d_0{weather_type_id}anim.svg"
        else:
            forecast['icon'] = f"/static/meteo/w_ic_d_{weather_type_id}anim.svg"

    context = {
        'city_name': next((city['local'] for city in cities_response['data'] if city['globalIdLocal'] == int(city_id)), 'Lisboa'),
        'forecasts': forecasts,
        'cities': cities_response['data']
    }

    return render(request, 'meteo/five_days_weather.html', context)


def cities_list(request):
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cities_url)
    cities_data = response.json()

    cities_dict = {city['globalIdLocal']: city['local'] for city in cities_data['data']}
    return JsonResponse(cities_dict)

def today_forecast(request, city_id):
    city_weather_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(city_weather_url)
    weather_data = response.json()

    today_forecast = weather_data['data'][0]
    weather_description = today_forecast['descIdWeatherTypePT']

    today_forecast_dict = {
        'city_name': today_forecast['local'],
        'min_temperature': today_forecast['tMin'],
        'max_temperature': today_forecast['tMax'],
        'date': today_forecast['forecastDate'],
        'weather_description': weather_description,
        'precipitation': today_forecast['precipitaProb'],
        'weather_icon': f"/static/meteo/w_ic_d_{today_forecast['idWeatherType']}anim.svg"
    }
    return JsonResponse(today_forecast_dict)

def five_days_forecast(request, city_id):
    city_weather_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(city_weather_url)
    weather_data = response.json()

    forecasts = weather_data['data'][:5]
    forecasts_list = []
    for forecast in forecasts:
        weather_description = forecast['descIdWeatherTypePT']
        forecast_dict = {
            'city_name': forecast['local'],
            'min_temperature': forecast['tMin'],
            'max_temperature': forecast['tMax'],
            'date': forecast['forecastDate'],
            'weather_description': weather_description,
            'precipitation': forecast['precipitaProb'],
            'weather_icon': f"/static/meteo/w_ic_d_{forecast['idWeatherType']}anim.svg"
        }
        forecasts_list.append(forecast_dict)
    return JsonResponse(forecasts_list, safe=False)