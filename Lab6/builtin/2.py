s = str(input())

upper = sum(map(lambda x: x.isupper(), s))
lower = sum(map(lambda x: x.islower(), s))

print(upper, lower)