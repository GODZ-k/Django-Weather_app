from django.shortcuts import render, HttpResponse, redirect
import datetime
import requests
import math

# Create your views here.
def home(request):
    city = request.POST.get('city') if 'city' in request.POST else 'Delhi'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5b474101163de7cf4d09da4ac876f9bc'
    params = {"units": "metric"}

    # Fix 1: Use requests.get to make the HTTP GET request
    response = requests.get(url, params=params)



    if response.status_code != 200:
        # Handle the error, for example:
        return HttpResponse(f"I this your are finding your city on moon {city}")
        # context={
        #     'error_message': "Invalid response"
        # }

    data = response.json()
    context={
             "wind":data['wind']['speed'],
             "min_temp":math.floor(data['main']['temp_min']),
             "humidity":data['main']['humidity'],
             "description":data['weather'][0]['description'],
             "icon": data['weather'][0]['icon'],
             "temp": math.floor(data['main']['temp']),
             "day":datetime.date.today(),
             "city": city,

             }

    return render(request, "index.html",context)
