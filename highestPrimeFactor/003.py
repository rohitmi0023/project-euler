# Brute force solution
import time
import math
start = time.time()
def largest_prime_factor(num):
    highest_prime = 2
    for i in range(2, num + 1):
        while num % i == 0:
            # print(num, 'num')
            highest_prime = i
            num /= i
            # print(num, 'num')
    return highest_prime

print(largest_prime_factor(144544))
print(" %s seconds " % (time.time() - start))
# Takes 0.0107049942017 seconds

# 2
# import time
# import math
start = time.time()
def largest_prime_factor(num):
    div = 2
    while div <= math.floor(math.sqrt(num)):
        if div > num:
            return int(num)
        if num % div == 0:
            num /= div
        else:
            div += 1    
    return int(num)
    
print(largest_prime_factor(144544))
print(" %s seconds " % (time.time() - start))
# Takes 2.19345092773e-05 seconds