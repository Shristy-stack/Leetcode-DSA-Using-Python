class Solution:
    def reverseString(self, s: List[str]) -> None:
        n=len(s)//2
        p=len(s)-1
        for i in range(n):
            s[i],s[p-i]=s[p-i],s[i]
        """
        Do not return anything, modify s in-place instead.
        """
        