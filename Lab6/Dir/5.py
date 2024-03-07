lst = list(map(int, input().split()))

with open("text.txt", "w") as file:
    for i in lst:
        file.write(str(i) + ' ')


file = open("text.txt", "r")

print(file.read())

file.close()


#5A
lst = list(map(int, input().split()))

with open("text.txt", "w") as file:
    for i in lst:
        file.write(str(i) + ' ')


with open("text.txt", "r") as file:
    print(file.read())