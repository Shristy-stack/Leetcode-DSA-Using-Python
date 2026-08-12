class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_prof=0
        for i in range(1,len(prices)):
            if prices[i]>min_price:
                diff=prices[i]-min_price
                max_prof=max(diff,max_prof)
            else:
                min_price=prices[i]

        return max_prof