from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
import requests
from .models import City
from .forms import CityForm
from datetime import datetime


def index(request):
    cities = City.objects.all() #return all the cities in the database    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a67ce542dda0063877352b04f31cf6d3'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()
    weather_data = []
    current_time = datetime.now() # getting the current time
    formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p") # formatting the time using directives, it will take this format Day, Month Date Year, Current Time 
    
    for city in cities:
        try:
            city_weather = requests.get(url.format(city)).json()
            
            # Check if the API returned an error
            if city_weather.get('cod') != 200:
                continue
                
            # Get timestamp, default to current time if 'dt' is missing
            timestamp = city_weather.get('dt', datetime.now().timestamp())
            dt = datetime.fromtimestamp(timestamp)
            dt = dt.strftime("%A, %B %d %Y, %I:%M:%S %p")
            
            weather = {
                'city': city,
                'country_code': city_weather['sys']['country'],
                'temperature': city_weather['main']['temp'],
                'feels_like': city_weather['main']['feels_like'],
                'temp_max': city_weather['main']['temp_max'],
                'temp_min': city_weather['main']['temp_min'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon'],
                'time': dt,
                'wind_speed': city_weather['wind']['speed'],
                'humidity': city_weather['main']['humidity'],
            }
            weather_data.append(weather)
        except Exception as e:
            # Skip this city if there's any error
            print(f"Error fetching data for {city}: {str(e)}")
            continue

    context = {'weather_data' : weather_data, 'form': form}
    return render(request, 'weather/index.html', context) #returns the index.html template

def delete_view(request, city):

    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(City, name = city)
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "weather/delete_view.html", context)