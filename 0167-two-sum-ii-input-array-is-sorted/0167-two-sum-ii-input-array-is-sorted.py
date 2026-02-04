class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            sump=numbers[l]+numbers[r]
            if sump==target:
                return [l+1,r+1]
            elif sump>target:
                r-=1
            else:
                l+=1
                
        