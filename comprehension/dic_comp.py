#dic comprehension provides a way to transform one list into another
cities = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]

#zip is build-in function in python, zip two list
z = zip(cities, countries)

for a in z:
    print(a)

d = {city:country for city, country in zip(cities, countries)}
print(d)