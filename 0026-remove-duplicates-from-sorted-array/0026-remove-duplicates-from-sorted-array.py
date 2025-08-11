class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p=sorted(list(set(nums)))
        n=len(p)
        for i in range(0,n):
            nums[i]=p[i]
        return n
                