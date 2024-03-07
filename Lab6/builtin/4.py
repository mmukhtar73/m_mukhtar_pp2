import time 
import math

n = int(input())
t = int(input())

time.sleep(t/1000)

square = math.sqrt(n)

print(f"Square root of {n} after {t} miliseconds is {square}")