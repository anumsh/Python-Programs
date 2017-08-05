#Generate random float numbers in a specific numerical range


import random
for x in range(6):
    print('{:04.3f}'.format(random.uniform(x, 100)), end = '  ')
