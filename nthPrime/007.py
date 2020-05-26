# Not working for 10000
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True        

def nthPrime(n):
    if n == 1:
        return 2
    primeNumbers = 1
    count = 3
    while primeNumbers != n:
        if isPrime(count):
            primeNumbers += 1
        count += 2    
    return count- 2

print(nthPrime(7))

