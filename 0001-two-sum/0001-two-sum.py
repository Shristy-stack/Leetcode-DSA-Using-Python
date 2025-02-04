class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            c = target - value
            if c in hashmap:
                return [hashmap[c], index]
            hashmap[value] = index
