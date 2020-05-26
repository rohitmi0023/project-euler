# Brute force method
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
# 
# print(smallestMult(16))

# Method 2
# Euclidean algorithm for gcd calculation
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a*b//gcd(a, b)

def smallestMult(num):
    smallestNum = num
    for i in range(num - 1, 0, -1):
        smallestNum = lcm(smallestNum, i)
        # Instead of above 3 lines just 
        # reduce(lcm, range(1,num+1))
        # will also work after 
        # from functools import reduce 
    return smallestNum

print(smallestMult(20))
