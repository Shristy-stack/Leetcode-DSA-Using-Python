class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof=0
        sump=0
        min_price=float('inf')
        for i in range(len(prices)):
            if prices[i]>min_price:
                diff=prices[i]-min_price
                sump+=diff
                max_prof=max(max_prof,sump)
                min_price=prices[i]
            else:
                min_price=prices[i]

        return max_prof