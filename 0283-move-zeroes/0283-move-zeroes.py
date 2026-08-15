class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i,j=0,0
        while j<len(nums):
            if nums[j]!=0:
                if nums[i]==0:
                    nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1




        """
        Do not return anything, modify nums in-place instead.
        """
        