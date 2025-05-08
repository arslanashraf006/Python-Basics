# 1

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter a city name: ")

if city in india:
    print("india")
elif city in pakistan:
    print("pakistan")
elif city in bangladesh:
    print("bangladesh")
else:
    print("based on little knowledge I have, I don't know which country has this", city)


city1 = input("Enter a city1 name: ")
city2 = input("Enter a city2 name: ")

if city1 in india and city2 in india:
    print("india")
elif city1 in pakistan and city2 in pakistan:
    print("pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("bangladesh")
else:
    print("based on little knowledge I have, I don't know which country has these cites belong to named", city1, city2)



# 2

sugar_level = float(input("Enter your fasting sugar level (mg/dL): "))
if sugar_level < 80:
    print("Your sugar level is low.")
elif sugar_level > 100:
    print("Your sugar level is high.")
else:
    print("Your sugar level is normal.")
