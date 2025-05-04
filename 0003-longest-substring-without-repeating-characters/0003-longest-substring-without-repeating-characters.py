class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        res=0
        l,r=0,0
        while r<len(s):
            if s[r] in charset:
                charset.discard(s[l])
                l+=1
            else:
                charset.add(s[r])
                res=max(res, r-l+1)
                r=r+1
        return res