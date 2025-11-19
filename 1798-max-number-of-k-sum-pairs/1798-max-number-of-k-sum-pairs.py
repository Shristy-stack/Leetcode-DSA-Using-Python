class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        res=0
        while i<j:
            sump=nums[i]+nums[j]
            if sump==k:
                res+=1
                i+=1
                j-=1
            elif sump<k:
                i+=1
            else:
                j-=1

        return res
            
