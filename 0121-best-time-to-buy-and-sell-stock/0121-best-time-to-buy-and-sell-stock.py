class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        max_prof,cost=0,0
        for i in range(1, len(prices)):
            cost=prices[i]-mini
            max_prof=max(max_prof,cost)
            mini=min(mini, prices[i])
        return max_prof