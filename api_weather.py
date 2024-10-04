import requests
import datetime

api_key = '68b84d513446b2ce68934dc010663614'
lat = '-6.2088' 
lon = '106.8456' 

# API URL
url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'

# Making the request
response = requests.get(url)

if response.status_code == 200:
    forecast_data = response.json()
else:
    print(f"Failed to get weather forecast. Status code: {response.status_code}")

morning_temps = []
for entry in forecast_data['list']:
    if "09:00:00" in entry['dt_txt']:
        morning_temps.append({
            'date': entry['dt_txt'][:10],
            'temp': entry['main']['temp'] - 273.15  # Ubah Kelvin Ke Celcius
        })

forecast_output = "Weather Forecast:\n"
for i in range(5):
    date_obj = datetime.datetime.strptime(morning_temps[i]['date'], "%Y-%m-%d")
    formatted_date = date_obj.strftime("%a, %d %b %Y")
    forecast_output += f"{formatted_date}: {morning_temps[i]['temp']:.2f}°C\n"

print(forecast_output)
