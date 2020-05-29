# Takes 10.2489750385 seconds
from math import sqrt
import time
start_time = time.time()

def isPrime(num):
    sqrtValue = int(sqrt(num)) 
    # print(sqrtValue, 'num')
    for j in range(3, sqrtValue + 1, 2):
        # print(j, 'j')
        if num % j == 0:
            return False
    return True        

def primeSummation(n):
    if n == 1:
        return 2
    if n == 2:
        return 5
    if n == 3:
        return 10
    if n == 4:
        return 17
    sum = 17
    for i in range(11, n, 2):
        if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            if isPrime(i):
                sum += i    
    return sum

print(primeSummation(2000000))
print("--- %s seconds ---" % (time.time() - start_time))