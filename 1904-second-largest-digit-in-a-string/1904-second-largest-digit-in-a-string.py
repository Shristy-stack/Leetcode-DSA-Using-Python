import re
class Solution:
    def secondHighest(self, s: str) -> int:
        s=re.sub(r'[^0-9]','',s)
        s=sorted(set(s),reverse=True)
        if len(s)>=2:
            return int(s[1])
        return -1
     
