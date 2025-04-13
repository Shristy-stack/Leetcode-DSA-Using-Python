class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        c = 0
        for i in hashmap:
            if hashmap[i] == 1:
                c = i
                break

        for i in range(len(s)):
            if s[i] == c:
                return i
        return -1
