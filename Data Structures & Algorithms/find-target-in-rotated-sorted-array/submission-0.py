class Solution:
    def findMinIndex(self, nums: List[int]) -> int:
        l =0
        r= len(nums)-1
        if nums[l]<nums[r]:
            return nums[l]

        while l<r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        return r
    
    def binarySearch(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l, r = 0, n-1

        res = -1
        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return -1    

    def search(self, nums: List[int], target: int) -> int:
        minIndex = self.findMinIndex(nums)
        print(minIndex)
        targetIndex = self.binarySearch(nums[0:minIndex], target)
        print(targetIndex)
        if targetIndex == -1:
            res = self.binarySearch(nums[minIndex:], target)
            print(res)
            return minIndex + res if res!= -1 else -1
        return targetIndex



        
