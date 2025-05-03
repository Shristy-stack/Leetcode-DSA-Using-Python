class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        currsum=0
        prefixsum={0:1}
        for i in nums:
            currsum=currsum+i
            diff=currsum-k
            res=res+prefixsum.get(diff,0)
            prefixsum[currsum]=1+prefixsum.get(currsum,0)
        return res
        