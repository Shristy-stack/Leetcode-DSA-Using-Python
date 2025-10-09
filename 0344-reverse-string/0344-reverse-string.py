class Solution:
    def reverseString(self, s: List[str]) -> None:
        p="".join(s)
        p=p[::-1]
        for i in range(len(p)):
            s[i]=p[i]

        return s
        """
        Do not return anything, modify s in-place instead.
        """
        