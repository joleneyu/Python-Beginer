my_age = int(input("How old are you?\n"))
decades = int(my_age/10)
years = my_age - decades*10
age = "You are " + str(decades) + " decades and " + str(years) + " year(s) old."
print(age)