class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        res=[]
        for num in nums:
            hashmap[num]=1+hashmap.get(num,0)
        sorted_dict = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        for key,value in sorted_dict.items():
            if k>0:
                res.append(key)
            k-=1
        return res