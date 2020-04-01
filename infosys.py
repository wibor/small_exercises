#written for infosys junior program

def factorial(n):
    if n<2:
        return 1
    else:
        return reduce(lambda x,y:x*y, range(2, n+1))
        
def operation(x, y, s):
    if s not in ['+', '-', '%', '*'] or not len(s) == 1:
        return 'Error'
    else:
        return eval(x+s+y)
        
import numpy as np
from matplotlib import pyplot as plt
import random
data = []
floor = 0

def dice():
    dice = random.randint(1, 6)
    if dice<3:
        return -1
    elif dice==6:
        return random.randint(1, 6) + random.randint(1, 6)
    return 1

for i in range(100):
    floor+=dice()
    if floor<0: floor=0
    if floor>100: floor=100
    data.append(floor)

plt.plot(data)
plt.ylabel('floors')
plt.show()

# other: 
how_mach = int(input())
data = [(int(input()))for i in range(how_mach)]

import operator
def operation(data, operator):
    result = data[0]
    for i in data[1:]:
        result = operator(result, i)
    return result

print(operation(data, operator.iadd))
print(operation(data, operator.isub))
print(operation(data, operator.imul))
