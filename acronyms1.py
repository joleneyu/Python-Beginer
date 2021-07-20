acronyms = ['IDK', "LOL", "TBH"]
translations = ["I don't know", "laugh out loud", "to be honest"]

acronyms = {'LDK': 'laugh out loud',
            'IDK': "I don't know",
            'TBH': 'to be honest'}
print(acronyms['LDK'])

# Dictionaries can be anything, key=string, value=number, or vice versa.
menu = {'Soup': 5, 'Salad': 6}
my_dict = {10: 'hello', 2: 6.5}

# Create a Dictionary
acronyms = {}
acronyms['BZD'] = "bu zhi dao"
print(acronyms)

# Delete an item in Dictionary
del acronyms['BZD']
print(acronyms)

# Get an item that might not be there
defination = acronyms.get('BTW')
print(defination)

if defination:
    print(defination)
else:
    print("Key doesn't exist")

# Use a dictionary to translate a sentence
acronyms = {'LDK': 'laugh out loud',
            'IDK': "I don't know",
            'TBH': 'to be honest'}
sentence = 'IDK ' + 'what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')
print('sentence:', sentence)
print('translation:', translation)