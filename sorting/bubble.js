// Remember, algorithms are the steps to solving a problem. It doesn't matter
// what language they're implemented in.

function bubbleSort(arr) {
	for (let i = 0; i < arr.length - 1; i++) {
		let madeSwap = false;
		for (let j = 0; j < arr.length - 1 - i; j++) {
			if (arr[j] > arr[j + 1]) {
				[arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
				madeSwap = true;
			}
		}
		if (!madeSwap) {
			break;
		}
	}
}
