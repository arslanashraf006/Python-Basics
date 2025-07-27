basket = {"orange", "apple", "mango", "apple", "orange"}
print(type(basket))
print(basket)

a = set()
a.add(1)
a.add(2)
print(a)

numbers = [1,2,3,4,2,3,4]
unique_numbers = set(numbers)
print(unique_numbers)
unique_numbers.add(5)
print(unique_numbers)

x = {"a", "b", "c"}
y = {"a", "g", "h"}

print("a" in x)
print("g" in x)
#union
print(x|y)
#intersection
print(x&y)
#dif
print(x-y)
#subset : second set has all the value of set 1
print(x<y)
a = {"h", "g"}
print(a<y)

for i in x:
    print(i)

# if you don't want to change the content of the set then use frozen sets for it
fs = frozenset(numbers)
print(fs)
fs.add(5)