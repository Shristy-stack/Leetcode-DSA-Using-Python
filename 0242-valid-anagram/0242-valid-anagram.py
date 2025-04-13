class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        chashmap={}
        for i in t:
            if i in chashmap:
                chashmap[i]+=1
            else:
                chashmap[i]=1
        if chashmap==hashmap:
            return True
        else:
            return False
        
            
            

        