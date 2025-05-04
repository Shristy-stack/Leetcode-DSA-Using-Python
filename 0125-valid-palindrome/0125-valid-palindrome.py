import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(" ","")
        s=re.sub(r'[^A-Za-z0-9]', '', s)
        if s==s[::-1]:
            return True
        else:
            return False
