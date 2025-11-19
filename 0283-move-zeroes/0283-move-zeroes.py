class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i,j=0,0
        while i<len(nums):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
            i+=1
        return nums




        """
        Do not return anything, modify nums in-place instead.
        """
        