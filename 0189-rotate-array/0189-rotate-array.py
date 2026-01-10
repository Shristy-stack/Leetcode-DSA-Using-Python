class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        if n==0:
            return nums
        k=k%n
        def rotation(nums,i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        rotation(nums,0,n-1)
        rotation(nums,0,k-1)
        rotation(nums,k,n-1)

        