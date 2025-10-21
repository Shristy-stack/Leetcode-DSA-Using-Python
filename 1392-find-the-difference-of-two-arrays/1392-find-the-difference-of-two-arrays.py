from collections import Counter
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashmap1,hashmap2=Counter(set(nums2)), Counter(set(nums1))
        res1,res2=set(),set()
        for num in nums1:
            if num not in hashmap1 :
                res1.add(num)
        for num in nums2:
            if num not in hashmap2 :
                res2.add(num)
        return [list(res1),list(res2)]


