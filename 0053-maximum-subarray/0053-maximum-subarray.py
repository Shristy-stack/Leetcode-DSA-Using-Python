import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sump=0
        maxp=-sys.maxsize-1
        for i in range(len(nums)):
            sump=sump+nums[i]
            maxp=max(maxp,sump)
            if sump<0:
                sump=0
        return maxp