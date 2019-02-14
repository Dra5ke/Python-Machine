import time
import math

time = int(time.time())

seconds = time % 60

minutes = time // 60

hours = minutes // 60

print(hours)
print(minutes)
print(seconds)

def check_fermat(a, b, c, n):
    left_side = math.pow(a, n) + math.pow(b, n)
    right_side = math.pow(c, n)
    if left_side == right_side :
        print('Ok')
    else:
        print('Not ok')

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
n = int(input('n:'))

check_fermat(a, b, c, n)
