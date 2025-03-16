class Solution:
    def reverseBits(self, n: int) -> int:
        sum=0
        len=32
        i=0
        while len!=0:
            c=n%2
            sum=sum+ (c*(2 ** (len-i-1)))
            n=n//2
            len=len-1
        return sum