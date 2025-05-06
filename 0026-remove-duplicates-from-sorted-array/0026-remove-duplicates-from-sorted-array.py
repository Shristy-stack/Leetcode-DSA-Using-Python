class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=[]
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
                res.append(num)
        k=0
        for i in range(len(res)):
            nums[i]=res[i]
            k+=1
        return k
