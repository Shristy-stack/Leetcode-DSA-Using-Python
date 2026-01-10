class Solution:
    def firstUniqChar(self, s: str) -> int:
        res=[0]*26
        for i in range(len(s)):
            res[ord(s[i])-ord('a')]+=1
        for i in range(len(s)):
            if res[ord(s[i])-ord('a')]==1:
                return i
        print(res)
        return -1