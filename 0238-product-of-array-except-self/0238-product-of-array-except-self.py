class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod=[1]*len(nums)
        right_prod=[1]*len(nums)
        for i in range(1,len(nums)):
            left_prod[i]=left_prod[i-1]*nums[i-1]
        nums=nums[::-1]
        for i in range(1,len(nums)):
            right_prod[i]=right_prod[i-1]*nums[i-1]
        right_prod=right_prod[::-1]
        merged=[1]*len(nums)
        for i in range(len(nums)):
            merged[i]=left_prod[i]*right_prod[i]
        return merged