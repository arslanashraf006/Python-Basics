#1

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
total_heads = 0
for i in result:
    if i == "heads":
        total_heads =  total_heads + 1
print("Total heads are", total_heads)

#2
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Square is", i**2)

#3
# expense_list = [2340, 2500, 2100, 3100, 2980]

# amount = input("Enter Expanse amount: ")

# exp_amount = int(amount)

# for i in range(len(expense_list)):
#     if exp_amount == expense_list[i]:
#         print("expense occured in month ", i+1 )
#         break
#     else:
#         print("Expense is not occured in any month")

# for i in range(1,6):
#     result = input("Are you tired (yes/no) :")
#     if result == 'yes':
#         print("you didn't finish the race")
#         break
#     if i == 5:
#         print("congratulations! you have finish the race")

#4

for i in range(1,6):
        print("*" * i)