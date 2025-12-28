class Solution:
    def isPalindrome(self, x: int) -> bool:
        p=str(x)
        return p[::-1]==p