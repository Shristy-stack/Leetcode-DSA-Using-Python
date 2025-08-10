class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        n=len(s)
        p=0
        for i in range(len(t)):
            if t[i]==s[p]:
                p+=1
            if p==n:
                break
        if p==n:
            return True
        else:
            return False

        