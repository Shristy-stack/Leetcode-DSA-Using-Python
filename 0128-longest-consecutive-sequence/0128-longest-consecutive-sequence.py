class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        num_set=set(nums)
        for i in num_set:
            if i-1 not in num_set:
                current_string=i
                current_streak=1
                while current_string+1 in num_set:
                    current_streak +=1
                    current_string +=1
                longest=max(longest,current_streak)

        return longest
                

