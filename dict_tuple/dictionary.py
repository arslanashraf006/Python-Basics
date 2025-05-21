# dictonaries
d ={
    "tom": 728479394793,
    "rob": 399748494373,
    "joe": 937493748375,
}
print(d)
print(d['tom'])

d["sam"] = 939249479900
print(d)

del d["sam"]

print(d)

for key in d:
    print("key:", key, "value:",d[key])

for k,v in d.items():
    print("key:", k, "value:", v)

print("samir" in d)

d.clear()

print(d)

# tuple

point = (5,9)
print(point[0])
print(point[1])
# tuples are immutable

point[0] = 50