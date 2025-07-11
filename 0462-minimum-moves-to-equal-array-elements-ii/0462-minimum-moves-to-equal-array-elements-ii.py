class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        p=sorted(nums)
        median=0+len(p)//2
        res=0
        for i in range(len(p)):
            res=abs(p[i]-p[median])+res
        return res

        