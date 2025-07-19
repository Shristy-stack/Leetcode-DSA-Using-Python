class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for num in range(1,amount+1):
            for c in coins:
                if num-c>=0:
                    dp[num]=min(dp[num],1+dp[num-c])
        if dp[amount]==amount+1:
            return -1
        else:
            return dp[amount]