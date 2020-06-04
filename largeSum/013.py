# from functools import reduce
testNums = [
    '37107287533902102798797998220837590246510135740250',
    '46376937677490009712648124896970078050417018260538'
]

# newArr = []

# for k in range(len(testNums[0]) // 10):
#     for i in range(len(testNums)):
#         chunk = testNums[i][k * 10:(k + 1) * 10]
#         newArr.append(chunk)

# # for k in range(len(testNums)):
# #     for i in range(len(testNums[0]) // 10):
# #         chunk = testNums[k][i * 10:(i + 1) * 10]
# #         newArr.append(chunk)

# for i in range(len(newArr)):
#     newArr[i] = int(newArr[i])



# print(newArr)

# newTest = list(map(int, testNums[0].split(',')))
# newTest2 = list(map(int, testNums[1].split(',')))
# print(testNums)
# print(newTest)
# print(newTest2)

newArray = []
for i in testNums:
    newArray.append(int(i))

arraySum = sum(newArray)
print(str(arraySum)[:10])
