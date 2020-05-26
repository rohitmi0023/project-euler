function sumSquareDifference(n) {
	let sumOfSquares = (n * (n + 1) * (2 * n + 1)) / 6;
	let squaresOfSum = Math.pow((n * (n + 1)) / 2, 2);
	return squaresOfSum - sumOfSquares;
}

console.log(sumSquareDifference(10));
