class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ind=0
        for i in range(len(nums)):
            if max_ind<i:
                return False
            max_ind=max(max_ind,nums[i]+i)
        return True
            

        