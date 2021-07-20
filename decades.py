age = int(input("How old are you?\n"))
decades = age // 10
years = age % 10
you_age = "You are " + str(decades) + " decades and " + str(years) + " year(s) old."
print(you_age)