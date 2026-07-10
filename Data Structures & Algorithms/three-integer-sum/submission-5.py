class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            
            left = i+1
            right = n-1
            while left < right:
                # print(left, right, target)
                if nums[left]+nums[right]<target:
                    left = left+1
                elif nums[left]+nums[right]>target:
                    right = right-1
                elif nums[left] + nums[right]==target:
                    ans.append([nums[left], nums[right], -1 *target])
                    left = left+1
                    right = right-1
                    while (left < right and nums[left]==nums[left-1]):
                        left = left+1

        
        return ans

       




