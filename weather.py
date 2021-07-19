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