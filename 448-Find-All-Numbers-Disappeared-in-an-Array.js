function findDisappearedNumbers(nums) {
    let hMap = new Set([...nums])
    let output = []
    nums.forEach((num, i) => {
        if(!hMap.has(i + 1)){
            output.push(i + 1)
        }
    })
    return output
};

console.log(findDisappearedNumbers([4,3,2,7,8,2,3,1]))