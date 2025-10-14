class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        a,b=0,1
        c=0
        while n>=2:
            c=a+b
            a=b
            b=c
            n-=1
        return c
