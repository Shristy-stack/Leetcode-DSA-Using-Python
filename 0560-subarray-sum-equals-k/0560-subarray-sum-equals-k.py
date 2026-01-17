class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        count=0
        pre_sum=0
        for i in range(len(nums)):
            pre_sum=pre_sum+nums[i]
            diff=pre_sum-k
            if diff in hashmap:
                count+=hashmap[diff]
            if pre_sum in hashmap:
                hashmap[pre_sum]+=1
            else:
                hashmap[pre_sum]=1
        return count
        

