class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if nums[index]<0:
                res.append(abs(nums[i]))
            nums[index]=-nums[index]
        return res
       
        