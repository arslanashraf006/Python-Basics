items = ["bread", "pasta", "fruits", "veggies"]
print(items)
print(items[0])
print(items[2])

items[0] = "chips"
print(items)
print(items[0:2])
print(items[-1])

items.append("butter")
print(items)

items.insert(0, "bread")
print(items)

food = ["bread", "pasta", "fruits"]
bathroom = ["shampoo", "soap"]
items =  food + bathroom
print(items)
print(len(items))
print("bread" in items)
print("soda" in items)

# Exercise

# 1
expense_list = [2200, 2350, 2600, 2130, 2190]

print("Spend Extra money in feb compare to jan is : ", expense_list[1] - expense_list[0])
print("Total expense in first quarter : ", sum(expense_list[0:3]) )
print("Did I spend exactly 2000? ", 2000 in expense_list)

expense_list.append(1980)
print("Expense after adding june : ",expense_list)

expense_list[3] = expense_list[3] - 200
print("Expense after april refund : ", expense_list)

# 2

heros=['spider man','thor','hulk','iron man','captain america']

print("Length of the list is : ", len(heros))
heros.append('black panther')
print("After adding black panther : ", heros )
heros.remove("black panther")
heros.insert(3, "black panther")
print("Adding black panther after hulk after removing it from end : ", heros)
heros[1:3] = ['doctor strange']
print("replace thor and hulk : ", heros)

print(dir(heros))

heros.sort()
print("After sorting : ", heros)
