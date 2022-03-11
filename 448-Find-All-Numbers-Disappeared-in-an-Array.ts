function findDisappearedNumbers(nums) {
    let output = []
    nums.forEach((num, i) => {
        if(!nums.includes(i + 1)){
            output.push(i + 1)
        }
    })
    return output
};

console.log(findDisappearedNumbers([4,3,2,7,8,2,3,1]))