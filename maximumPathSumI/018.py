test_triangle = [[1, 0, 0, 0],
                [2, 10, 0, 0],
                [6, 5, 10, 0],
                [50, 5, 6, 10]
]

def maximumPathSumI(test_triangle):
    for i in range(len(test_triangle) - 1, -1, -1):
        for j in range(i):
    		test_triangle[i - 1][j] += max(test_triangle[i][j], test_triangle[i][j+1])
    return test_triangle[0][0]

print(maximumPathSumI(test_triangle))
