class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        is_inc=True
        is_dec=True
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                is_dec=False
            elif nums[i]>nums[i+1]:
                is_inc=False
        return is_inc or is_dec