function singleNumber(nums ) {
    let stack = new Set()
    nums.forEach((num, i) => {
        if(stack.has(num)){
            stack.delete(num)
        } else {
            stack.add(num)
        }
    })

    return [...stack][0]
};
console.log(

    singleNumber([1])
    )