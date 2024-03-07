from functools import reduce

def multiply(a):
    return reduce(lambda x, y: x*y, a)

lst = list(map(int, input().split()))

result = multiply(lst)

print(result)