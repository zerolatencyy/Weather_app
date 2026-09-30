import requests
print("🌦 Weather App")
city = input("Enter city name: ")
print(f"Fetching weather data for {city}...")
response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1")
data = response.json()
result = data["results"][0]
latitude = result["latitude"]
longitude = result["longitude"]

