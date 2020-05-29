def isTriplet(a, b, c):
    if pow(c, 2) == pow(a, 2) + pow(b, 2):
        return True
    return False

def specialPythagoreanTriplet(n):
    for a in range(1, n):
        for b in range(a, n):
            c = n - b - a
            if (isTriplet(a, b, c)):
                return a*b*c

print(specialPythagoreanTriplet(1000))