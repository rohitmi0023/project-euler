function longestCollatzSequence(n) {
	if (n === 1) return 1;
	longestCount = longestNum = 1;
	currentNum = 2;
	while (currentNum < 2) {
		let initialValue = currentNum;
		let count = 0;
		while (initialValue !== 1) {
			if (initialValue % 2 === 0) initialValue /= 2;
			else initialValue = 3 * initialValue + 1;
			count += 1;
			if (count > longestNum) {
				longestCount = count;
				longestNum = currentNum;
			}
			currentNum++;
		}
	}
	return longestNum;
}

console.log(longestCollatzSequence(14));
