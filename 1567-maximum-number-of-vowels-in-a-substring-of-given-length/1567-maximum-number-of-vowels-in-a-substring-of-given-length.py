class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=['a', 'e', 'i', 'o','u']
        max_len,count=0,0
        window=s[0:k]
        for i in range(len(window)):
            if window[i] in vowel:
                count+=1
            max_len=count
        for i in range(k,len(s)):
            if s[i] in vowel:
                count+=1
            if s[i-k] in vowel:
                count-=1
            max_len=max(max_len,count)
        return max_len
        