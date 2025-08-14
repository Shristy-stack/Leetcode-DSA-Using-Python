class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1=s.split()[-1]
        return len(s1)