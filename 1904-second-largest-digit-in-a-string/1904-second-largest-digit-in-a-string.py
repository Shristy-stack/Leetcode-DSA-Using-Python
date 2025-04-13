import re
class Solution:
    def secondHighest(self, s: str) -> int:
        s=re.sub(r'[^0-9]','',s)
        s=sorted(s, reverse= True)
        if len(s):
            p=max(s)
            for i in s:
                if p!=i:
                    return int(i)
        return -1
     
