class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap={}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]+=1
            else:
                hashmap[s[i]]=1
        for j in range(len(t)):
            if t[j] not in hashmap or hashmap[t[j]]==0:
                return False
            hashmap[t[j]]-=1
        return True