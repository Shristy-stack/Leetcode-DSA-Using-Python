class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        sump=sum(nums)
        for i in range(0,len(nums)):
            right_sum=sump-left_sum-nums[i]
            if left_sum==right_sum:
                return i
            left_sum=left_sum+nums[i]

        return -1