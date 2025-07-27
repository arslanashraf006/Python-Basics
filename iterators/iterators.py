a = ['hey', 'bro', 'you are', 'awesome']
for i in a:
    print(i)
print(dir(a))
itr = iter(a)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
#print(next(itr))
rev = reversed(a)
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))

#list iterate
for element in [1,2,3]:
    print(element)
#tuple iterate
for element in (1,2,3):
    print(element)

#dictionary iterate
for key in {'one': 1, 'two': 2}:
    print(key)

#file
for line in open("C:\\Users\\REGEN\\Documents\\python basics\\book.txt"):
    print(line, end = '')