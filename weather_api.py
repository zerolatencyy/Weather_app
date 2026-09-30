import requests

def get_coordinates(city):

    response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1")
    data =  response.json()
    result = data['results'][0]
    latitude = result['latitude']
    longitude = result['longitude']

    return latitude, longitude

def get_weather(city):
    latitude, longitude = get_coordinates(city)
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()
    temperature = data['current']['temperature_2m']
    return temperature