class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        p=max(candies)
        for i in range(len(candies)):
            if extraCandies + candies[i] >= p:
                candies[i]=True
            else:
                candies[i]=False
        return candies