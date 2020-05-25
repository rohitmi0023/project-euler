# Brute force solution 
def largest_prime_factor(num):
    if num < 2:
        print('Number should be greater than or equal to 2')
        return
    highest_prime = 2
    for i in range(2, num + 1):
        while num % i == 0:
            highest_prime = i
            num /= i 
    return highest_prime

print(largest_prime_factor(5))