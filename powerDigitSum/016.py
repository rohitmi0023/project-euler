value = pow(2, 1000)
arrValue = map(int, str(value))
result = reduce(lambda x, y: x + y, arrValue)
print(result)