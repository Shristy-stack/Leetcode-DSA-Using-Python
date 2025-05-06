class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        presum=0
        count=0
        for i in range(0, len(nums)):
            presum=presum+nums[i]
            diff=presum-k
            count+=hashmap.get(diff,0)
            hashmap[presum]=1+hashmap.get(presum,0)
        return count