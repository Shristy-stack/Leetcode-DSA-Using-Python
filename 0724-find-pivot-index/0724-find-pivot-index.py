class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum,right_sum=0,0
        sump=sum(nums)
        n=len(nums)
        if left_sum==sump-nums[0]:
            return 0
        
        for i in range(1,len(nums)):
            left_sum=nums[i-1]+left_sum
            right_sum=sump-left_sum-nums[i]
            if left_sum==right_sum:
                return i
        if right_sum==sump-nums[n-1]:
            return len(nums)-1

        return -1