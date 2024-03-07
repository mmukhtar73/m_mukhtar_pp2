with open("text.txt", "r") as file:
    copy = file.read()

with open("A.txt", "w") as file:
    file.write(copy)

f = open("A.txt", "r")

print(f.read())

f.close()