api_key = "your key from openweather"
city = "Sydney"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

def get_weather_description_min_max():
    import requests
    response = requests.get(url)
    json = response.json()

    description = json.get("weather")[0].get('description')
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")
    return {"description": description,
            "temp_min": temp_min,
            "temp_max": temp_max}

def main():
    weahter_dict = get_weather_description_min_max()

    # Print the results
    print("Today's weather is", weahter_dict.get("description"))
    print("The minimum temperature is ", weahter_dict.get("temp_min"))
    print("The maximum temperature is ", weahter_dict.get("temp_max"))

main()