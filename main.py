import requests

api_key = "27bef37f32dfd5a6298e9540d63fda01"

weather_url = "http://api.openweathermap.org/data/2.5/weather?"

print("Welcome to my program!")
print("Where would you like to check the weather?")
print("Please enter a zip code or city")

city_zip_code = input(f"Enter here: ")

complete_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_zip_code}&appid={api_key}&units=imperial'

response = requests.get(complete_url)


x = response.json()

if x["cod"] != "404":

    y = x["main"]

    current_temperature = y["temp"]

    current_humidity = y["humidity"]

    z = x["weather"]

    weather_condition = z[0]["description"]

    print(f"\n Temperature (in Fahrenheit) = " +
          str(current_temperature) +
          "\n Humidity (in percentage) = " +
          str(current_humidity) +
          "\n Conditions = " +
          str(weather_condition))

else:
    print(" City Not Found ")