import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minp=sys.maxsize
        low,high=0,len(nums)-1
        while(low<=high):
            mid=int((low+high)/2)
            if nums[low]<=nums[mid]:
                minp=min(minp,nums[low])
                low=mid+1
            elif nums[high]>=nums[mid]:
                minp=min(minp,nums[mid])
                high=mid-1
        return minp
