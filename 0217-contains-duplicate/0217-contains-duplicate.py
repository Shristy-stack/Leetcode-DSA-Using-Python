class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for index,value in enumerate(nums):
            if value in hashmap:
                return True
            hashmap[value]=index
        return False