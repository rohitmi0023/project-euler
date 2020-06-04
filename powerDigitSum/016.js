function powerDigitSum(exponent) {
	let value = BigInt(Math.pow(2, exponent));
	let arrValue = Array.from(String(value), Number);
	return arrValue.reduce((acc, item) => (acc += parseInt(item)), 0);
}
