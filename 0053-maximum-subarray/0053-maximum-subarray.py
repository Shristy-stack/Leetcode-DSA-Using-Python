class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sump,max_sump=0,float('-inf')
        for i in range(len(nums)):
            sump=sump+nums[i]
            max_sump=max(max_sump,sump)
            if sump<0:
                sump=0
        return max_sump


