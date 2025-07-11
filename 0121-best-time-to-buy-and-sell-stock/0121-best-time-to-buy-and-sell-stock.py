class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        max_prof=0
        while r<len(prices):
            if prices[l]<prices[r]:
                diff=prices[r]-prices[l]
                max_prof=max(max_prof,diff)
                r+=1
            else:
                l=r
                r+=1
        return max_prof
