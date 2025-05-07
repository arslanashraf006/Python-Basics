text = "ice cream"
print(text)

print(text[0])

#strings are unchangeable (unmutable) means cannot change the string value

print(text[0:3]) # index subrange
print(text[4:9])
print(text[4:])
print(text[:3])

text = "let's learn python"
text = 'hello "world"'

address = '''1 purple street
new york
usa'''

print(address)

#concatinate

s1 = "hello"
s2 = "world"

print(s1+ ' '+s2)

num = 25
s = "total states in usa # "

print(s + str(num))

# Exercise

#1
street = 25
city = "lahore"
country = "Pakistan"

address = str(street) + '\n' + city + '\n' + country
print(address)

# Method 2: Using f-string
address_fstring = f"{street}\n{city}\n{country}"
print("Address using f-string:")
print(address_fstring)

# 2

text = "Earth revolves around the sun"

print(text[7:15])
print(text[-3:])

# 3

x = 'I eat 2 vegitable in day'
y = 'I eat 1 fruit in day'

print(f"{x}\n{y}")

# 4

s = 'maine 200 banana khaye'
print(s.replace("200", "10").replace("banana", "samosa"))
