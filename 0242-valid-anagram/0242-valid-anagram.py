class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        dict2={}
        for i in s:
            dict[i]=1+dict.get(i,0)
        for i in t:
            dict2[i]=1+dict2.get(i,0)
        return dict==dict2