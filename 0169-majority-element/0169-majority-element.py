class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele=nums[0]
        count=1
        for i in range(1,len(nums)):
            if ele==nums[i]:
                count+=1
            else:
                count-=1
            if count==0:
                ele=nums[i+1]
        return ele
            
