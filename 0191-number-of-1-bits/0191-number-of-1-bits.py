class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n!=0:
            c=n&1
            if c==1:
                count=count+1
            n=n>>1
        return count
