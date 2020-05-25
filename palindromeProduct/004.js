function checkPalindrome(number) {
	let res = Array.from(String(number), Number);
	let length = res.length;
	let count = 0;
	if (length % 2 !== 0) return false;
	for (let i = 0; i < length / 2; i++) {
		if (res[i] == res[length - i - 1]) count += 1;
	}
	if (count == length / 2) return true;
	else return false;
}

let highest_palindrome = 0;

function largestPalindromeProduct(num) {
	let lower_limit = Math.pow(10, num - 1);
	let upper_limit = Math.pow(10, num) - 1;
	for (let i = upper_limit; i > lower_limit; i--) {
		for (let j = upper_limit; j > lower_limit; j--) {
			if (checkPalindrome(i * j)) {
				if (i * j > highest_palindrome) {
					highest_palindrome = i * j;
				}
			}
		}
	}
	return highest_palindrome;
}

console.log(largestPalindromeProduct(2));
