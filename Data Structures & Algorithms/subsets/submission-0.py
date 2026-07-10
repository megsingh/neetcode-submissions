class Solution:

    def subsetsHelper(self, nums, i , res, subset ):
        if i == len(nums):
            res.append(subset.copy())
            return
        
        self.subsetsHelper(nums, i+1, res, subset)
        subset.append(nums[i])
        self.subsetsHelper(nums, i+1, res, subset)
        subset.pop()
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset =[]
        self.subsetsHelper(nums, 0, res,subset )
        return res