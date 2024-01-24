m = "Hello"
print(m)

b = """Достоинство человека определяется тем, 
каким путем он идет к цели, 
а не тем, достигнет ли он ее
   (с) Абай К.
"""
print(b)

fc="Barcelona"
print(fc[2])

for fc in "Barcelona ":
 print (fc)

print (len(fc))

print ("l" in fc)

if "o" in fc:
    print("Yes")

print ("z" not in fc)

if "z"not in fc:
    print("No")

print(fc[-5:-2])

print(fc[2:])

print(fc[:-2])

print (fc.upper())

print (fc.lower())

print(fc.strip())

print(fc.replace("B","V"))

print(fc.split("o"))

h="hi"

m="Murat"

c=h+m
d=h+" "+m

print(c)
print(d)

# we can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} 

friends=3
weeks=2
time=9
text = "I will be playing tennis after {} weeks at {} am with my {} friends"
print(text.format(weeks,time,friends)) 

k="He is \"DK\", it means drift king"
print (k)

txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

txt = "Hello\nWorld!"
print(txt) 

txt = "Hello\rWorld!"
print(txt) 

txt = "Hello\tWorld!"
print(txt) 

txt = "Hello \bWorld!"
print(txt) 

txt = "\110\145\154\154\157" #octal
print(txt) 

txt = "\x48\x65\x6c\x6c\x6f" #hex
print(txt) 




#just for myself
""""
Method	            Description

capitalize()	    Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

"""








