# Got 50 points from hackerrank
import math, time
start = time.time()
def isPrime(num):
    for i in range(3, int(math.floor(math.sqrt(num))) + 1, 2):
        if num % i == 0:
            return False
    return True        

def nthPrime(n):
    if n == 1:
        return 2
    prime_numbers = 1
    count = 3
    while prime_numbers != n:
        if isPrime(count):
            prime_numbers += 1
        count += 2    
    return count - 2

for _ in range(int(input())):
    print(nthPrime(int(input())))
print(' %s seconds ' % (time.time() - start))

# Python Program to find prime numbers in a range using seive of Eratosthenes 
# import time
# t0 = time.time()
# def SieveOfEratosthenes(n):
#     prime = [True for i in range(n + 1)] 
#     p = 2
#     while (p * p <= n):
#         if (prime[p] == True):
#             for i in range(p * 2, n + 1, p): 
#                 prime[i] = False
#         p += 1
#     prime[0]= False
#     prime[1]= False
#     # Print all prime numbers 
#     for p in range(n + 1):
#         if prime[p]: 
#             print p, 
  
# # driver program 
# if __name__=='__main__': 
#     for i in range(int(input())):
#         SieveOfEratosthenes(int(input())) 
# t1 = time.time() 
# print("Time required:", t1 - t0) 
