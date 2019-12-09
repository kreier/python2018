import math
import time

last = 1000

start = time.time()
print("Prime numbers to 1000")

print('2, 3, 5, 7',end='')
for number in range(11, last, 2):
    prime = 1
    for divider in range(2, int(math.sqrt(number))+1, 1):
        if number/divider == int(number/divider):
            prime = 0

    if prime == 1:
        print(',', number,end='')
        
end = time.time()
print('\nThis took:', int((end - start) * 1000) , 'ms.')
