class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        low,high=1,n-2
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid
            elif arr[mid]<arr[mid-1]:
                high=mid-1
            elif arr[mid]<arr[mid+1]:
                low=mid+1

        