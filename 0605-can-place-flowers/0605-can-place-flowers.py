class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        
        for i in range(length):
            if n == 0:
                return True

            # Check if current spot can hold a flower
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i-1] == 0) and
                (i == length-1 or flowerbed[i+1] == 0)):
                
                flowerbed[i] = 1  # place flower
                n -= 1

        return n == 0