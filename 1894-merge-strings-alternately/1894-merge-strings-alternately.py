class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word=[]
        list1=list(word1)
        list2=list(word2)
        i,j=0,0
        while i < len(word1) and j<len(word2):
            merged_word.append(word1[i])
            merged_word.append(word2[j])
            i=i+1
            j=j+1
        while i<len(word1):
            merged_word.append(word1[i])
            i=i+1
        while j<len(word2):
            merged_word.append(word2[j])
            j=j+1
        return "".join(merged_word)