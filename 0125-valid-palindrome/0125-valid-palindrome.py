import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(" ","")
        rs=re.sub(r'[^a-zA-Z0-9]','',s)
        r=[]
        for i in rs:
            r.append(i)
        if r==r[::-1]:
            return True
        else:
            return False
        
        return r