class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        max_i=float('-inf')
        c=0
        for key, value in hashmap.items():
            if max_i<value:
                max_i=value
                c=value
            elif max_i==value:
                c+=value
        return c
