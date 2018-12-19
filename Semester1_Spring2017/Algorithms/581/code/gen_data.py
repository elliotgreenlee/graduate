import random

f = open("input_file", 'w')
top = 10000000
for i in range(0, top):
    num = random.randint(0, top)
    f.write(str(num))
    f.write(" ")