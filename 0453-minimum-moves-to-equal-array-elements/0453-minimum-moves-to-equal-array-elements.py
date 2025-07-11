class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sump=sum(nums)
        return sum(nums)-(min(nums)*len(nums))