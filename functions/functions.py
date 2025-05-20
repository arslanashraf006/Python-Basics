def calculate_total(exp):
    total = 0
    for item in exp:
        total =  total + item
    return total

tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

toms_total = calculate_total(tom_exp_list)
joes_total = calculate_total(joe_exp_list)

print("Tom's total expenses :", toms_total)
print("Joe's total expenses :", joes_total)

total = 0 #global
def sum(a, b = 0):
    """
    This function takes two arguments which are integer numbers and will return
    a sum of them as output
    """
    total = a+b # local
    print("Inside total : ", total)
    return total

n = sum(a=5)
print("Total :", n)
print("Outside total : ", total)