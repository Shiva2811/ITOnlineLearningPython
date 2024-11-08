names = {
    'name':'shiva',
    'age':'20',
    'city':'india'
}

#retreving data with help of keys in dictionaries
result = {key: names.get(key) for key in ['name', 'age', 'city']}
print(result)

#key, values, items
print(names.keys())
print(names.values())
print(names.items())

#loop wiht dictionaries
for key in names:
    print(key, names[key])

print(names)


#coping dictionaries with copy functiona and dict() function 
names2 = names.copy()
print(names2)

names3 = dict(names2)
print(names3)