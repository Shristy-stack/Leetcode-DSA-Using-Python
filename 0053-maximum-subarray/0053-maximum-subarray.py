class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sump,max_sum=0,float('-inf')
        for i in range(len(nums)):
            sump+=nums[i]
            max_sum=max(max_sum,sump)
            if sump<0:
                sump=0
        return max_sum
            