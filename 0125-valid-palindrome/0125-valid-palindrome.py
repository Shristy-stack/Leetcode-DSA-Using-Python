import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(" ","")
        cleaned = re.sub(r'[^A-Za-z0-9]', '', s)
        cleanedp=cleaned[::-1]
        return cleaned==cleanedp