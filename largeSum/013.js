function largeSum(arr) {
	return +arr
		.reduce((acc, item) => (acc += parseInt(item)), 0)
		.toString()
		.substring(0, 11)
		.replace('.', '');
}

const testNums = [
	'37107287533902102798797998220837590246510135740250',
	'46376937677490009712648124896970078050417018260538',
];

console.log(largeSum(testNums));
