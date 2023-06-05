def maxProfit(prices):
    l = 0
    r = l +1
    maxprofit = 0

    #print(i)
    while r < len(prices):
          if prices[l]<prices[r]:
              profit = prices[r] - prices[l]
              maxprofit = max(maxprofit,profit)
          else:
              l = r
          r += 1

    return maxprofit
