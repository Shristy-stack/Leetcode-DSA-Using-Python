class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        tot_sum=sum(nums)
        for i in range(len(nums)):
            tot_sum-=nums[i]
            if left_sum==tot_sum:
                return i
            left_sum+=nums[i]
        return -1