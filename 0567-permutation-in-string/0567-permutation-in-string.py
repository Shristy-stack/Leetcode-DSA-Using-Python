class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        for i in range(len(s2)-k+1):
            p=s2[i:i+k]
            if sorted(s1)==sorted(p):
                return True

        return False

