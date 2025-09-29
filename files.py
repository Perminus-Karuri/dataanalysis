import os

# r = Read
# a = Append
# w = Write
# x = Create

# read - error if file does not exist

f = open("names.txt", "r")
# print(f.read())
# print(f.read(4))  # reads the first 4 characters of the line in the file

# print(f.readline())  # reads the first line
# print(f.readline()) # reads the next line

for line in f:
    print(line)

f.close() # closes the file

try:
    f = open("names.txt")
    print(f.read())
except:
    print("\nThe file you want to read does not exist")
finally:
    f.close()

# Append - creates a file if it doesn't exist

f = open("names.txt", "a")
f.write("\nZidane")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)

f = open("context.txt", "w")
f.write("Glory Glory Manchester United GGMU")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# two ways to create a new file

# -opens a file for writing, creates the file if it doesn't exist

f = open("name_list.txt", "w")
f.close()

# creates the speified file but returns an error if the file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file

# avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)