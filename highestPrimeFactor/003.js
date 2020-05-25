//  Brute force solution
function largestPrimeFactor(num) {
	if (num < 2) {
		print('Number should be greater than or equal to 2');
		return;
	}
	let highest_prime = 2;
	for (let i = 2; i <= num; i++) {
		while (num % i == 0) {
			highest_prime = i;
			num /= i;
		}
	}
	return highest_prime;
}
console.log(largestPrimeFactor(5));
