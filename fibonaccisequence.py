import numpy as np
import time

a = 0
b = 1
print(a)
print(b)

number = input('Enter number of times the sequence to be run: ')
number = int(number)
print(number)

for x in number:
    c = a + b
    print(c)
    a = b
    b = c
    time.sleep(1)
