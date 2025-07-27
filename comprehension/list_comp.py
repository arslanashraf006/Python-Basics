#list comprehension provides a way to transform one list into another
number = [1,2,3,4,5,6,7]
even = []
for i in number:
    if i % 2 == 0:
        even.append(i)

print(even)

#comp
#[output, loop, condition]
even = [i for i in number if i%2==0]
print(even)

sqr_numbers = [i*i for i in number]
print(sqr_numbers)