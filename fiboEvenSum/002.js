function fiboEvenSum(num) {
	let arr = [];
	let sum = 0;
	let i = 0;
	if (num >= 1) arr.push(1);
	i += 1;
	if (num >= 2) arr.push(2);
	i += 1;
	if (num >= 3)
		while (arr[i - 1] + arr[i - 2] <= num) {
			arr.push(arr[i - 1] + arr[i - 2]);
			i += 1;
		}
	for (let j = 0; j < i; j++) {
		if (arr[j] % 2 == 0) sum += arr[j];
	}
	return sum;
}
console.log(fibo_even_sum(100000));
