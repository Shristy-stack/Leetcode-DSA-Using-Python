
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]+=1
            else:
                hashmap[s[i]]=1
        for key,value in hashmap.items():
            if value==1:
                for i in range(len(s)):
                    if s[i] == key:
                        return i

        return -1