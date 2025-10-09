class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        maxp=float('-inf')
        res=0
        for key,value in hashmap.items():
            if value > maxp:
                maxp=value
                res=key
        return res