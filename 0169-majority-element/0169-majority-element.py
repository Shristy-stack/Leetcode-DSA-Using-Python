class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele=nums[0]
        count=0
        for i in range(0,len(nums)):
            if ele==nums[i]:
                count+=1
            else:
                count-=1
            if count==0:
                ele=nums[i+1]
        return ele
            
