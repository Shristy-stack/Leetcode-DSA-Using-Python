class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        count=[0]*(n+1)
        for i in range(len(citations)):
            if citations[i]>=n:
                count[n]+=1
            else:
                count[citations[i]]+=1
        sump = 0
        for i in range(n, -1, -1):  # loop from n down to 0
            sump += count[i]
            if i <= sump:
                return i

