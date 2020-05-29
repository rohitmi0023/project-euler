function isPrime(num) {
	let sqrtValue = Math.floor(Math.sqrt(num))
	for (let j = 3, j <= sqrtValue; j += 2){
		if (num % j == 0) return false
	}
	return true
}
function primeSummation(n) {
	if (n == 1) return 2
	if (n == 2) return 5
	if (n == 3) return 10
	if (n == 4) return 17
	let sum = 17
	for (let i = 11; i < n; i += 2){
		if (i % 3 !== 0 && i % 5 !== 0 && i % 7 !== 0) {
			if(isPrime(i)) sum+= i
		}
	}
	return sum
}

console.log(primeSummation(2000000))