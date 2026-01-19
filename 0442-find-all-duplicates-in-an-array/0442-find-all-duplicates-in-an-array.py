class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        p=set()
        res=[]
        for num in nums:
            if num in p:
                res.append(num)
            else:
                p.add(num)
        return res