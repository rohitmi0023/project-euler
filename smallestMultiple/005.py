# Brute force method
import time
# start = time.time()
# def smallestMult(num):
#     smallestNum = num
#     count = 0
#     while count != num:
#         count = 0
#         for i in range(num, 0, -1):
#             if smallestNum % i == 0:
#                 count += 1
#             if count != num:    
#                 smallestNum += 1
#     return smallestNum

# print(smallestMult(16))
# print(' %s seconds... ' % (time.time() - start))
# Takes  0.0765368938446 seconds...

# Method 2
# Euclidean algorithm for gcd calculation
start = time.time()
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a*b//gcd(a, b)

def smallest_mult(num):
    smallest_num = num
    for i in range(num - 1, 0, -1):
        smallest_num = lcm(smallest_num, i)
        # Instead of above 3 lines just 
        # reduce(lcm, range(1,num+1))
        # will also work after 
        # from functools import reduce 
    return smallest_num

print(smallest_mult(16))
print(' %s seconds... ' % (time.time() - start))
# 1.19209289551e-05 seconds...
