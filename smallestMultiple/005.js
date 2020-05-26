function gcd(a, b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

function lcm(a, b) {
	return Math.floor((a * b) / gcd(a, b));
}

function smallestMult(num) {
	let smallestNum = num;
	for (let i = num - 1; i > 0; i--) smallestNum = lcm(smallestNum, i);
	return smallestNum;
}

console.log(smallestMult(20));
