class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap={}
        for i in range(len(arr)):
            hashmap[arr[i]]=1+hashmap.get(arr[i],0)
        return len(set(hashmap.values()))==len(hashmap.values())