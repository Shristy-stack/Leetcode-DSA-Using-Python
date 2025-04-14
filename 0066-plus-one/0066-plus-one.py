class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        i=0
        nums=0
        while i<n:
            nums=nums+((10**i)*digits[n-i-1])
            i+=1
        nums=nums+1
        a=[]
        while nums:
            a.append(nums%10)
            nums=nums//10
        a=a[::-1]
        return a
            
