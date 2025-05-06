class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(0, len(nums)):
            if n==1:
                return i
            if i!=0 and i!=n-1 and  nums[i]>nums[i+1] and nums[i]>nums[i-1] :
                return i
            if i==0 and nums[i]>nums[i+1]:
                return i
            if i==n-1 and nums[i]>nums[i-1]:
                return i