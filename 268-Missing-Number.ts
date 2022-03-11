function missingNumber(nums) {
    let output = 0
    nums.forEach((num, i) => {
        if(!nums.includes(i)) {            
            output = i
        }
        if(!nums.includes(nums.length)){
            output = nums.length
        }
    })
    return output
    
};

console.log(missingNumber([9,6,4,2,3,5,7,0,1]))