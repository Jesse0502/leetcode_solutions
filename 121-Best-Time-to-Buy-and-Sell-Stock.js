const maxProfit = function(prices) {
    let max_till_now = prices[0]
    let min_till_now = prices[0]
    result = 0
    for (i in prices){
        if (prices[i] > max_till_now){
            max_till_now = prices[i] 
            result = max_till_now - min_till_now
        }
        if(prices[i] < min_till_now){
            min_till_now = prices[i]
            result = max_till_now - min_till_now
        }

    }
    console.log(max_till_now, min_till_now, result)
};

maxProfit([7,6,4,3,1])