class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap={}
        res=[]
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1
        for key,value in hashmap.items():
            if value==2:
                res.append(key)
        return res