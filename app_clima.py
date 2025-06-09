import requests
import pandas as pd
from datetime import datetime, timedelta
from time import sleep

API_KEY = "0aa08f9773594e3e805211153240611"

chile_cities = [
    "Punta Arenas", "Puerto Natales", "Antofagasta", "Iquique",
    "Valparaíso", "Los Angeles", "Puerto Montt"
]


start_date = datetime(2025, 5, 26)
end_date = datetime(2025, 6, 4)

delta = timedelta(days=1)
all_hourly_data = []

for city in chile_cities:
    date = start_date
    while date <= end_date:
        date_str = date.strftime("%Y-%m-%d")
        url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={city}&dt={date_str}&lang=es"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Error al consultar {city} en {date_str}: {response.status_code} - {response.text}")
            date += delta
            sleep(1)
            continue
        
        data = response.json()
        hourly = data['forecast']['forecastday'][0]['hour']
        
        for hour_data in hourly:
            record = {
                'date': date_str,
                'time': hour_data['time'],  # Formato: YYYY-MM-DD HH:MM
                'city': city,
                'temp_C': hour_data['temp_c'],
                'condition_text': hour_data['condition']['text'],
                'condition_code': hour_data['condition']['code'],
                'humidity_%': hour_data['humidity'],
                'wind_kph': hour_data['wind_kph'],
                'wind_dir': hour_data['wind_dir'],
                'precip_mm': hour_data['precip_mm'],
                'cloud_%': hour_data['cloud']
            }
            all_hourly_data.append(record)
        
        print(f"Datos horarios obtenidos para {city} en {date_str}")
        date += delta
        sleep(1)  # Para respetar límite de consultas

df = pd.DataFrame(all_hourly_data)
df.to_csv("chile_weather_hourly_may_jun_2025.csv", index=False)
print("CSV generado: chile_weather_hourly_may_jun_2025.csv")
