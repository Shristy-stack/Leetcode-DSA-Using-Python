class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for num in range(0,n+1):
            count=0
            while num!=0:
                if num%2!=0:
                    count+=1
                num=num//2
            res.append(count)
        return res        