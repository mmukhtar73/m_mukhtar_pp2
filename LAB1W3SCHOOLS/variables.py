# variables
x = 3
y = 'hello'
print (x)
print (y)

# var names
m=int(7)
M=str(7)
k=float(7)
print(type(m))
print(type(M))
print(type(k))

myvar="Murat"
my_var="Murat"
MY_var_="Murat"
print (myvar)

# multiple vars
a, s, x = "apple", "samsung", "xiaomi"
cars = ["porshe", "bmw","mercedes"]
p, b, m = cars
print (p)

# output vars
h="Hello"
w="World"
print(h,w)
print (h + w)
print(3+2,"five")

# global vars
t="Hi"
def func():
    print(t+", my friend")
func()
print(t+", how are you?")

t="Hi"
def func():
    global t
    t = "Bye"
    print(t+", my friend")
func()
