file = open("text.txt", "r")

lines = file.readlines()

print(lines) #show lines in a text file
print(f"The number of lines in text.txt is {len(lines)}") #the number of lines

file.close()