import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(" ","")
        rs=re.sub(r'[^a-zA-Z0-9]','',s)
        if rs==rs[::-1]:
            return True
        else:
            return False
        
        return r