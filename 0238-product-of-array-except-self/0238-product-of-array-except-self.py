class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        postfix=[1]*n
        prefix=[1]*n
        for i in range(1,n):
            prefix[i]=nums[i-1]*prefix[i-1]
        for j in range(n-2,-1,-1):
            postfix[j]=postfix[j+1]*nums[j+1]
        for k in range(n):
            nums[k]=prefix[k]*postfix[k]
        return nums