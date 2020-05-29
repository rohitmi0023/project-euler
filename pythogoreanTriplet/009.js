function isTriplet(a, b, c) {
	if (Math.pow(c, 2) === Math.pow(a, 2) + Math.pow(b, 2)) return true;
	return false;
}

function specialPythagoreanTriplet(n) {
	for (let a = 1; a < n; a++) {
		for (let b = a + 1; b < n; b++) {
			let c = n - b - a;
			if (isTriplet(a, b, c)) return a * b * c;
		}
	}
}

console.log(specialPythagoreanTriplet(1000));
