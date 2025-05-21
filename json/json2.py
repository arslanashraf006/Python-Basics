f = open('C:\\Users\\REGEN\\Documents\\python basics\\book.txt', 'r')
s = f.read()
print(s)

import json
book = json.loads(s)
print(book)
print(book['bob'])
print(book['bob']['phone'])

for person in book:
    print(book[person])