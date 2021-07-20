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