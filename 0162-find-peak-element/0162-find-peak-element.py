class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        neg_inf = float('-inf')
        n=len(nums)
        nums = [neg_inf] + nums + [neg_inf]
        i=1
        while n!=0:
            if nums[i]>nums[i-1] and  nums[i]>nums[i+1]:
                return i-1
            i+=1
            n-=1
