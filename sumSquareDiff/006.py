def sumSquareDifference(n):
    sumOfSquares = (n * (n + 1) * (2 * n + 1)) / 6
    squaresOfSum = pow((n * (n + 1)) / 2, 2)
    return squaresOfSum - sumOfSquares

print(sumSquareDifference(10))
