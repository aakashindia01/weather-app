from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    city = request.GET.get('city' , "Mumbai")

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=d2f708fa6fb2caa1420412d6f91d596e'
    data = requests.get(url).json()
    payload ={ 
        'city': data['name'], 
        'weather': data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'], 
        'kelvin_temperature' : data['main']['temp'],
        'Celsius_temperature' : int(data['main']['temp'] - 273),
        'pressure' :data['main']['pressure'],   
        'humidity' :data['main']['humidity'],
        'description' : data['weather'][0]['description']
    }

    context = {'data' :payload }

    return render(request, 'home.html', context)
