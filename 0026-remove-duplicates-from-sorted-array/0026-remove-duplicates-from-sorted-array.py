class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        j=1
        for i in range(len(nums)):
            if nums[j-1]!=nums[i]:
                nums[j]=nums[i]
                j+=1
        return j
                