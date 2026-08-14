class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        min_length=float('inf')
        sump=0
        while r<len(nums):
            sump+=nums[r]
            while sump>=target:
                min_length=min(min_length,r-l+1)
                sump-=nums[l]
                l+=1
            r+=1
        if min_length !=float('inf'):
            return min_length
        else:
            return 0