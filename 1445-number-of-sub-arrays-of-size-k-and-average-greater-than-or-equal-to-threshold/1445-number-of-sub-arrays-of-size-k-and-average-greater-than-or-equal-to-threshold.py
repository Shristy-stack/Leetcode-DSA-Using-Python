class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ws=sum(arr[:k])
        #print(ws//k)
        n=len(arr)
        res=0
        if ws//k >= threshold:
            res=res+1
        for i in range(k,n):
            ws=ws+arr[i]-arr[i-k]
            if ws//k >= threshold:
                print(ws)
                res=res+1
        return res