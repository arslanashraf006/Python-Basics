# write
f = open("C:\\Users\\REGEN\\Documents\\python basics\\files\\funny.txt", "w")
f.write("I Love JavaScript")
# apend
f = open("C:\\Users\\REGEN\\Documents\\python basics\\files\\funny.txt", "a")
f.write("\nI Love c++")
f.close()

# Read
f = open("C:\\Users\\REGEN\\Documents\\python basics\\files\\read.txt", "r")
f_out = open("C:\\Users\\REGEN\\Documents\\python basics\\files\\read_wc.txt", "w")

#print(f.read())

# line by line read
for line in f:
    tokens = line.split(' ')
    print(str(tokens))
    f_out.write("wordcount:"+ str(len(tokens)) + line)
    print(len(tokens))
    print(line)
f.close()
f_out.close()

# read and write
f = open("C:\\Users\\REGEN\\Documents\\python basics\\files\\read.txt", "r+")
f.close()

# read and write and create file if not exist
f = open("C:\\Users\\REGEN\\Documents\\python basics\\files\\read.txt", "w+")
f.close()

# with statement no need to close

with open("C:\\Users\\REGEN\\Documents\\python basics\\files\\funny.txt", "r") as f:
    print(f.read())
print(f.closed)