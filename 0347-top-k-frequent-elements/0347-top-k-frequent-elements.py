class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        a=[]
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1

        sorted_items=dict(sorted(hashmap.items(),key=lambda x:x[1],reverse= True))
        c=0
        for key, value in sorted_items.items():
            if c<k:
                a.append(key)
                c+=1
        return a
        