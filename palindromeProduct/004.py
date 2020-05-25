def checkPalindrome(number):
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


def largestPalindromeProduct(num):
    lower_limit = pow(10, num - 1)
    upper_limit = pow(10, num) - 1
    highest_palindrome = 0
    for i in range(upper_limit, lower_limit, -1):
        for j in range(upper_limit, lower_limit, -1):
            if checkPalindrome(i * j):
                if i * j > highest_palindrome:
                    highest_palindrome = i * j
    return highest_palindrome

print(largestPalindromeProduct(2))
