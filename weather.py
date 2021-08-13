api_key = "c631ceb140e5de617fa39dc05bffd612"
city = "Sydney"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

import requests
response = requests.get(url)
json = response.json()


description = json.get("weather")[0].get('description')
print("Today's weather is", description)

temp_min = json.get("main").get("temp_min")
print("The minimum temperature is ",temp_min)

temp_max = json.get("main").get("temp_max")
print("The maximum temperature is ",temp_max)
temperature = 70
if temperature < 60:
    print("It's too cold!")
    print("Stay inside!")
else:
    print("Enjoy outside!")

if temperature > 80 or temperature < 60:
    print("Stay inside!")
else:
    print("Go oudside")

temperature = 66
weather = "Sunny"
if temperature > 80 or temperature <60 or weather == "Rain":
    print('stay inside')
else:
    print('go outside')

if temperature < 80 and temperature > 60 and weather != "Rain":
    print("Enjoy outdoor")
else:
    print("Stay inside")

forecast = "Rain"
if not forecast == "Rain":
    print("Go outside")
else:
    print("Stay inside")

raining = True
if raining:
    print("Stay inside")

if not raining:
    print("Go outside")
else:
    print("Stay inside")
