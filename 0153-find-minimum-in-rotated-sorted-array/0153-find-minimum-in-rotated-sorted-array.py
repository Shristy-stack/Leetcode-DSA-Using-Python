import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minp=sys.maxsize
        for i in range(len(nums)):
            minp=min(minp,nums[i])
        return minp