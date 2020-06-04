def longestCollatzSequence(n):
    if n == 1:
        return 1
    longestNum = 1
    longestCount = 1
    currentNum = 2
    while currentNum < n:
        initialValue = currentNum
        count = 0
        while (initialValue != 1):
            if initialValue % 2 == 0:
                initialValue /= 2
            else:
                initialValue = 3 * initialValue + 1
            count += 1
        if count > longestCount:
            longestCount = count
            longestNum = currentNum
        currentNum += 1  

    return longestNum

print(longestCollatzSequence(1000000))