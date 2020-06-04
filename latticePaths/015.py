# Read the combinations and NE lattice paths in https://en.wikipedia.org/wiki/Lattice_path
import math

def latticePaths(n):
    return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n))

print(latticePaths(20))