class Solution:
    def reverseBits(self, n: int) -> int:
        sum=0
        for i in range(31,-1,-1):
            c=n%2
            sum=sum+((2**i)*c)
            n=n//2
        return sum
        