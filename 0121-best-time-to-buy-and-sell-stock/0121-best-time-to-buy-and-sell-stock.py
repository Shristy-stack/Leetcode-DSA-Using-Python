class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l,r=0,1
        maxp=0
        while r<n:
            if prices[l]>prices[r]:
                l=r
            else:
                profit=prices[r]-prices[l]
                maxp=max(profit,maxp)
            r=r+1
        return maxp