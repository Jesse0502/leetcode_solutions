def maxProfit(prices):
    minSoFar = prices[0]
    maxProfit = 0
    for p in prices:
        minSoFar = min(p, minSoFar)
        profit = p - minSoFar
        maxProfit = max(profit, maxProfit)

    return maxProfit
        

print(maxProfit([2,4,3,5,1]))