// Not working for 10000
function isPrime(num) {
	for (let i = 2; i < num; i++) {
		if (num % i == 0) return false;
		return true;
	}
}

function nthPrime(n) {
	if (n == 1) return 2;
	let primeNumbers = 1;
	let count = 3;
	while (primeNumbers !== n) {
		if (isPrime(count)) primeNumbers += 1;
		count += 2;
	}
	return count - 2;
}

console.log(nthPrime(1000));
