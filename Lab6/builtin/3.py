s = input()

#1
if s == s[::-1]:
    print("the string is a palindrome")
else:
    print("it isn't")

#2
print("palindrome?", "".join(reversed(s)) == s)