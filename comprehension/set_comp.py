#set comprehension provides a way to transform one list into another
# set is unordered collection of unique item
numbers = [1,2,3,4,5,6]
s = set([1, 2,3,4,5,2,3])
print(s)
even = {i for i in numbers if i % 2==0}
print(even)