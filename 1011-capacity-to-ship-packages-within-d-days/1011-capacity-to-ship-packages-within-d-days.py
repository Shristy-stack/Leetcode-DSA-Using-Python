class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def canship(mid):
            ship=1
            cap=mid
            for w in weights:
                if cap-w<0:
                    ship+=1
                    cap=mid
                cap=cap-w
            if ship<=days:
                return True
            else:
                return False
        while l<r:
            mid=(l+r)//2
            if canship(mid):
                r=mid
                res=min(res,mid)
            else:
                l=mid+1
        return res