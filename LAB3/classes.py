
# 1st 
print("Exercise #1")
class forString :
    def __init__(mys) :
        mys.str=" "
    def getString(mys):
        mys.str= input()
    def printString (mys):
        print (mys.str.upper())

for_String = forString()
for_String.getString()
for_String.printString()

# 2nd
print("Exercise #2")
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
my_square = Square(5)
print( my_square.area())

# 3rd
print("Exercise #3")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


my_rectangle = Rectangle(4, 6)
print( my_rectangle.area())

# 4th
print("Exercise #4")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f" ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        distance = ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5
        print( distance)


point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()
point2.show()
point1.dist(point2)

# 5th
print("Exercise #5")
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Dep {}. New b {}".format(amount, self.balance))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn {}. New balance: {}".format(amount, self.balance))
        else:
            print("Not enough")


my_account = Account("John Doe", 1000)
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(1000)

# 6th
print("Exercise #6")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print (prime_numbers)









