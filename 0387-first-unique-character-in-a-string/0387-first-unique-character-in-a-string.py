class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]=-1
            else:
                hashmap[s[i]]=i
        for i in hashmap.values():
            if i!=-1:
                return i
        return -1