class Solution:
    def firstUniqChar(self, s: str) -> int:
        p=Counter(s)
        for index, value in enumerate(s):
            #print(index,value)
            if p[value]==1:
                return index
        return -1
