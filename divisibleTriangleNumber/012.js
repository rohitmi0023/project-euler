function divisibleTriangleNumber(n) {
	if (n === 1) return 1;
	let numbers = [1, 1];
	let divisors = 0;
	while (divisors <= n) {
		numbers[1] += 1;
		numbers[0] += numbers[1];
		if (n >= Math.floor(numbers[0] / 2)) continue;
		divisors = 2;
		let count = 2;
		while (count <= Math.sqrt(numbers[0])) {
			if (numbers[0] % count === 0) divisors += 2;
			count += 1;
		}
	}
	return numbers[0];
}

console.log(divisibleTriangleNumber(23));
