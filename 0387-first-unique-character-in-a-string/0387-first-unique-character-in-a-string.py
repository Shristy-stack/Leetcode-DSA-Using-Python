class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap=Counter(s)
        for i, ch in enumerate(s):
            if hashmap[ch]==1:
                return i
        return -1