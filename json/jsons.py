book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 838374992,
}

book['bob'] = {
    'name': 'bob',
    'address': '1 red street, NY',
    'phone': 234374992,
}

import json

s = json.dumps(book)
with open('C:\\Users\\REGEN\\Documents\\python basics\\book.txt', 'w') as f:
    f.write(s)