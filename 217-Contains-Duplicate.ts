function containsDuplicate(nums) {
	let hMap = new Map()
	let output = false
	nums.forEach((num) => {
		if(hMap.has(num)){
			output = true;
			return
		} else {
			hMap.set(num, 1)
		}
	})
	return output
};

console.log(containsDuplicate([1,2,3,4]))