class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minp=float("inf")
        l,r=0,0
        sum=0
        c=0
        while r<len(nums):
            sum=sum+nums[r]
            while sum>=target:
                minp=min(minp,r-l+1)
                sum=sum-nums[l]
                l+=1
                c=1
            r+=1
        if c==1:
            return minp
        else:
            return 0