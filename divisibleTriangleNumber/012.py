import time
from math import sqrt
start_time = time.time()

# First Approach
# def divisibleTriangleNumber(n):
#     if n == 1:
#         return 1
#     numbers = [1]
#     divisors = 0
#     while divisors <= n:
#         numbers.append(numbers[-1] + (len(numbers) + 1))
#         # if len(numbers) == 7:
#         #     print(numbers)
#         if n >= numbers[-1]/2:
#             continue
#         # if numbers[-1] == 28:
#         #     print('Came here')
#         divisors = 2
#         count = 2
#         while count <= numbers[-1]//2:
#             if numbers[-1] % count == 0:
#                 divisors += 1
#             count += 1
#     return numbers[-1]

def divisibleTriangleNumber(n):
    if n == 1:
        return 1
    # Storing the last number at index 0 and position of that number at index 1
    numbers = [1, 1]
    divisors = 0
    # for i in range(6):
    while divisors <= n:
        numbers[1] += 1
        numbers[0] += numbers[1]
        if n >= numbers[0]//2:
            continue
        divisors = 2
        i = 2
        while i <= sqrt(numbers[0]):
            if numbers[0] % i == 0:
                divisors += 2
            i += 1
    return numbers[0]

print(divisibleTriangleNumber(500))
print("--- %s seconds ---" % (time.time() - start_time))
