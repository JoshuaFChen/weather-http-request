import requests

WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "a50ab14c120677ce84752856d11fef8f"
weather_param = {
    "lat": -33.868820,
    "lon": 151.209290,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(WEATHER_ENDPOINT, params=weather_param)
response.raise_for_status()
weather_data = response.json()
weather_hourly = weather_data["hourly"][0:11]
for _weather in weather_hourly:
    if int(_weather["weather"][0]["id"]) < 700:
        print("Not good weather, take an umbrella")