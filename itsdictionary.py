dog = {"name": "Barker", "age": "9", "color": "brown", "city": "USA"}
print(dog.get("color")) #To show something in dict
print(dog.pop("name")) #delete item
print(dog)
print(dog.popitem()) #delete the last item in dict
print(dog)
print(dog.keys()) #print the key
print(list(dog.values())) #Print the values
print(list(dog.items())) #Print dict into a list
dog["Food"] = "Meat" #For adding dict
print(dog)
del dog['color'] #delete keys in dict
print(dog)

dog1 = dog.copy()
print(dog1)