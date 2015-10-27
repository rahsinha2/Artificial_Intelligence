import random
a = 1
b = 3
c = 7
d = 9
numbers = range(a,b) + range(c,d)
r = random.choice(numbers)
print "%d" %(r)
