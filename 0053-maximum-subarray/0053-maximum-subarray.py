class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        sump=0
        for i in range(len(nums)):
            sump=sump+nums[i]
            max_sum=max(sump,max_sum)
            if sump<0:
                sump=0
                
        return max_sum