class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        p=sorted(nums)
        if len(p)==0:
            return 0
        count=1
        max_count=1
        for i in range(len(p)-1):
            if p[i]==p[i+1]:
                continue
            if p[i]+1==p[i+1]:
                count+=1
            else:
                count=1
            max_count=max(count,max_count)
        return max_count