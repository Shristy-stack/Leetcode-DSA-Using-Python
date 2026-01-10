class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]+=1
            else:
                hashmap[s[i]]=1
        c=0
        for key, value in hashmap.items():
            if value==1:
                c=key
                break
        for i in range(len(s)):
            if s[i]==c:
                return i
        return -1
            
