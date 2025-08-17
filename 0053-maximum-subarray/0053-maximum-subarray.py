class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        sump=0
        for i in range(len(nums)):
            sump=sump+nums[i]
            max_sum=max(max_sum,sump)
            if sump<0:
                sump=0
        return max_sum


