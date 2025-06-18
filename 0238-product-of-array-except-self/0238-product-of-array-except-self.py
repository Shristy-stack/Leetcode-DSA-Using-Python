class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        left_prod=[1]*n
        right_prod=[1]*n
        for i in range(len(nums)-1,0,-1):
            right_prod[i-1]=right_prod[i]*nums[i]
        for i in range(1,len(nums)):
            left_prod[i]=left_prod[i-1]*nums[i-1]
        for i in range(len(nums)):
            res[i]=right_prod[i]*left_prod[i]
        return res