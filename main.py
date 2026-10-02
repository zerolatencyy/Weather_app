from weather_api import get_weather
print("🌦 Weather App")
city = input("Enter city name: ")
print(f"Fetching weather data for {city}...")
temperature = get_weather(city)
print(f"Current temperature in {city}: {temperature}°C")