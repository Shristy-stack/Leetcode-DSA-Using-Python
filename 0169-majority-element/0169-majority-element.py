class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ele=nums[0]
        count=1
        for i in range(1,len(nums)-1):
            if nums[i]==maj_ele:
                count+=1
                #print(count)
            else:
                count-=1
                #print(count)
            if count==0:
                maj_ele=nums[i+1]
                #print('Hello',maj_ele)
                count=0
        return maj_ele