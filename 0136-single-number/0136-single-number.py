class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=sum(set(nums))
        return c-(sum(nums)-c)
        