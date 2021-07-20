# Use a list of lists for whole day menu
menus = [["Eggs on totast", "Flat white", "Bagel"],
        ["Pasta", "Coca", "Yang zhou Fried Rice"],
        ["Seafood Salad", "Bread", "Wine"]]
print(menus[0][1])

# Use a dictionary of lists for whole day menu, Key:value is a list
menus = {"Breakfast": ["Eggs on totast", "Flat white", "Bagel"],
         "Lunch":     ["Pasta", "Coca", "Yang zhou Fried Rice"],
         "Dinner":    ["Seafood Salad", "Bread", "Wine"]}
print('Breakfast Menu:\t', menus['Breakfast'])
print('Lunch menu:\t', menus['Lunch'])
print('Dinner menu:\t', menus['Dinner'])

# if the menu is too long, use a dictionary's key and value in a for Loop
x = menus.items()
print(x)

for name, menu in menus.items():
    print(name, ':\n\t', menu)
