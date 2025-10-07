class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap={}
        res=0
        for i in range(len(nums)):
            diff=k-nums[i]
            if diff in hashmap:
                res+=1
                hashmap[diff]-=1
                if hashmap[diff] == 0:
                    del hashmap[diff]
            else:
                hashmap[nums[i]]=hashmap.get(nums[i],0)+1
        print(hashmap)
        return res