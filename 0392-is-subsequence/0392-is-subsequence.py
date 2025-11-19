from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        if len(s)==0:
            return True
        i,j=0,0
        count=0
        while j<len(t):
            if s[i]==t[j] and i==count:
                i+=1
                count+=1
            if i==len(s):
                return True
            j+=1
        return False