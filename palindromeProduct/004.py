# 1
def check_palindrome(number):
    res = list(map(int, str(number)))
    length = len(res)
    count = 0
    if length % 2 != 0:
        return False
    for i in range(length / 2):
        if res[i] == res[length - i - 1]:
            count += 1
    if count == length / 2:
        return True
    else:
        return False


def largest_palindrome_product(num):
    lower_limit = pow(10, num - 1)
    upper_limit = pow(10, num) - 1
    highest_palindrome = 0
    for i in range(upper_limit, lower_limit, -1):
        for j in range(upper_limit, lower_limit, -1):
            if check_palindrome(i * j):
                if i * j > highest_palindrome:
                    highest_palindrome = i * j
    return highest_palindrome

print(largest_palindrome_product(2))

# 2 Hackerrank solution
palindromelist = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if str(a) == str(a)[::-1] and a not in palindromelist:
            palindromelist.append(a)
palindromelist.sort()
length = len(palindromelist)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = int(input())
        for i in range(length - 1, -1, -1):
            if palindromelist[i] < a:
                print(palindromelist[i])
                break