const testTriangle = [
	[3, 0, 0, 0],
	[7, 4, 0, 0],
	[2, 4, 6, 0],
	[8, 5, 9, 3],
];

function maximumPathSumI(testTriangle) {
	for (let i = testTriangle.length - 1; i >= 0; i--) {
		for (let j = 0; j < i; j++) {
			testTriangle[i - 1][j] += Math.max(testTriangle[i][j], testTriangle[i][j + 1]);
		}
	}
	return testTriangle[0][0];
}

console.log(maximumPathSumI(testTriangle));
