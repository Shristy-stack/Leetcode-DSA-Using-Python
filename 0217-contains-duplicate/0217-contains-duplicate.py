class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c=len(set(nums))
        p=len(nums)
        if c!=p:
            return True
        return False