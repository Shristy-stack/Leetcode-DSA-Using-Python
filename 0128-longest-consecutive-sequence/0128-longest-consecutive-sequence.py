class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setc=set(nums)
        res=0
        for num in setc:
            if num-1 not in setc:
                length=0
                while num+length in setc:
                    length+=1
                res=max(res,length)
        return res

