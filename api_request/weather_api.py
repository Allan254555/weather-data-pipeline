import requests

ACCES_KEY = "b7c0fc7826d0488d2685a46913857a13"
url = f"http://api.weatherstack.com/current?access_key={ACCES_KEY}&query=New York"

def fetch_data():
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("API response recieved sucessfully!")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong: {e}")
        raise

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-05-25 22:53', 'localtime_epoch': 1779749580, 'utc_offset': '-4.0'}, 'current': {'observation_time': '02:53 AM', 'temperature': 19, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '05:31 AM', 'sunset': '08:15 PM', 'moonrise': '02:58 PM', 'moonset': '02:25 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 66}, 'air_quality': {'co': '236.85', 'no2': '39.65', 'o3': '23', 'so2': '1.85', 'pm2_5': '10.35', 'pm10': '10.45', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 8, 'wind_degree': 235, 'wind_dir': 'SW', 'pressure': 1019, 'precip': 0, 'humidity': 90, 'cloudcover': 0, 'feelslike': 19, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}