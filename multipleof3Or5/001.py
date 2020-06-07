import time

# 1
start = time.time()
def multiple_of_3_or_5(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multiple_of_3_or_5(1000000))
end = time.time()
print("%s seconds" % (end - start))
# 0.102800130844 seconds for 1000000

# 2
# https://codereview.stackexchange.com/questions/102673/project-euler-1-multiples-of-3-and-5/102686#102686?newreg=9f8570e999d84ee08c20a37ab99cbe61
# Hackerrank solution
start = time.time()
def multiple_of_3_or_5(number):
    sum_of_3 = int((3 * ((number - 1) // 3) * (((number - 1) // 3) + 1)) >> 1)
    sum_of_5 = int((5 * ((number - 1) // 5) * (((number - 1) // 5) + 1)) >> 1)
    # To remove the duplicants like 15, 30 i.e. divisible by both 15 and 30
    # We found 15 by 3 * 5 / gcd(3, 5) = 15
    sum_of_15 = int((15 * ((number - 1) // 15) * (((number - 1) // 15) + 1)) >> 1)
    return sum_of_3 + sum_of_5 - sum_of_15

print(multiple_of_3_or_5(1000000))
end = time.time()
print("%s seconds" % (end - start))
# 8.10623168945e-06 seconds for 1000000