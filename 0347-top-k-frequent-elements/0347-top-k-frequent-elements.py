class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freq=[]
        res=[]
        for i in range(len(nums)+1):
            freq.append([])
        for key, value in count.items():
            freq[value].append(key)
        for i in range(len(freq)-1, -1,-1):
            for j in freq[i]:
                res.append(j)
                if k==len(res):
                    return res

