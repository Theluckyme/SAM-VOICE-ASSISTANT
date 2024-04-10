from take_command import speak
import requests

def get_weather(city):
    api_key = "b5365733f77540fcb87d76a3e1a371a5"  # Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(base_url)
        weather_data = response.json()

        if response.status_code == 200:
            weather_desc = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]
            return f"The weather in {city} is {weather_desc}. Temperature is {temperature}°C, humidity is {humidity}%, and wind speed is {wind_speed} m/s."
        else:
            return "Sorry, there was an error fetching the weather information. Please try again later."
    except Exception as e:
        return f"Sorry, an error occurred: {e}"