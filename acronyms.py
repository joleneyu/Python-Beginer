acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
print (acronyms[0])

acronyms.append('BFN')
acronyms.append('IMHO')
print(acronyms)

acronyms.remove('BFN')
print(acronyms)

del acronyms[4]
print(acronyms)

if "LOL" in acronyms:
    print('True')
else:
    print('False')

word = 'BFN'
if word in acronyms:
    print(word + ' is in the list.')
else:
    print(word + ' is NOT in the list')

for acronym in acronyms:
    print(acronym)
    