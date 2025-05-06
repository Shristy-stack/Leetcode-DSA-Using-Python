class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            if sum<0:
                max_sum=max(sum,max_sum)
                sum=0
            else:
                max_sum=max(sum, max_sum)
        return max_sum
