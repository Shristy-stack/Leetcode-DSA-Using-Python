class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxp,curr=0,0
        for i in range(0,len(gain)):
            curr=curr+gain[i]
            maxp=max(maxp,curr)
        return maxp
        
