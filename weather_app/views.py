from django.http import JsonResponse
from django.shortcuts import render
from .models import WeatherData
import json

def receive_weather_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        WeatherData.objects.create(
            temp=data['temp'],
            feels_like=data['feels_like'],
            temp_min=data['temp_min'],
            temp_max=data['temp_max'],
            pressure=data['pressure'],
            humidity=data['humidity'],
            visibility=data['visibility'],
            wind_speed=data['wind']['speed'],
            wind_deg=data['wind']['deg']
        )
        return JsonResponse({'message': 'Data received successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)

def display_weather_data(request):
    weather_data = WeatherData.objects.all()
    
    return render(request, 'weather_display.html', {'weather_data': weather_data})