import math, re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums=list(map(int,re.findall(r'[+-]?\d+', expression)))
        A,B=0,1
        for a,b in zip(nums[::2], nums[1::2]):
            A=A*b+a*B
            B=B*b
            g=math.gcd(A,B)
            A=A//g
            B=B//g
        return f"{A}/{B}"
