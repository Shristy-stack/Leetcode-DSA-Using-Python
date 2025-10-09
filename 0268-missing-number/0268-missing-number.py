class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sump=0
        n=len(nums)
        for i in range(0,n+1):
            sump=sump+i
        return sump-sum(nums)
        