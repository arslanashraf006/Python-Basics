exp = [2340, 2500, 2100, 3100, 2980]
#total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
total = 0
for item in exp:
    total = total + item
print(total)

for i in range(1, 11):
    print(i * i)


exp = [2340, 2500, 2100, 3100, 2980]
total = 0
for i in range(len(exp)):
    print('Month: ', (i+1), 'Expense: ', exp[i])
    total = total + exp[i]
print("Total expense is: ", total)

key_location = "chair"
locations = ["garage", "living room", "chair", "closet"]
for i in locations:
    if key_location == i:
        print("key is found in", i)
        break
    else:
        print("key is not found in", i)

for i in range(1,6):
    if i%2 == 0:
        continue
    print(i*i)

i = 1
while i <= 5:
    print(i)
    i = i + 1
    