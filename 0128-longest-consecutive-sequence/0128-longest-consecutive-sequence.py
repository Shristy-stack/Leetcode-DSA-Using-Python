class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setc=set(nums)
        longest=0
        for num in setc:
            if num-1 not in setc:
                start=num
                leng=0
                while start in setc:
                    leng+=1
                    start+=1
                longest=max(longest, leng)
        return longest
