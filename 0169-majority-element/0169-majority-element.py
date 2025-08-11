class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ele=nums[0]
        count=1
        for i in range(1,len(nums)):
            if count==0:
                maj_ele=nums[i]
            if maj_ele==nums[i]:
                count+=1
            else:
                count-=1
        return maj_ele