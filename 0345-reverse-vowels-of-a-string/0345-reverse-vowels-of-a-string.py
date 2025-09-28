class Solution:
    def reverseVowels(self, s: str) -> str:
        p=list(s)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        i,j=0, len(p)-1
        while i<j:
            if p[i] in vowels and p[j] in vowels:
                p[i],p[j]=p[j],p[i]
                i+=1
                j-=1
            elif p[i] in vowels and p[j] not in vowels:
                j-=1
            elif p[i] not in vowels and p[j] in vowels:
                i+=1
            elif p[i] not in vowels and p[j] not in vowels:
                i+=1
                j-=1
        return ''.join(p)

