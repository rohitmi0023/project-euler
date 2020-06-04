function factorial(num) {
	let value = num;
	for (let i = num - 1; i > 1; i--) {
		value *= i;
	}
	return value;
}

function latticePaths(n) {
	return parseInt(factorial(2 * n) / (factorial(n) * factorial(n)));
}

console.log(latticePaths(6));
