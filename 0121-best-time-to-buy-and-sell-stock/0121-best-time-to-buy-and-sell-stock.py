class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_diff=0
        for i in range(1, len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                diff=prices[i]-min_price
                max_diff=max(max_diff,diff)
        return max_diff
        