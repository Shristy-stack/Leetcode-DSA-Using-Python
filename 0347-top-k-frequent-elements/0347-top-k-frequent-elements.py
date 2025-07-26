class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        res=[]
        sorted_dict_desc = dict(sorted(hashmap.items(), key=lambda item: item[1],reverse=True))
        for key, value in sorted_dict_desc.items():
            if k>0:
                res.append(key)
            k-=1
        return res
            