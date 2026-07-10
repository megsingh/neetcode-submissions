class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(pos, subset):
            if pos == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[pos])
            backtrack(pos+1, subset)

            subset.pop()
            while pos+1 < len(nums) and nums[pos+1]==nums[pos]:
                pos+=1
            backtrack(pos+1, subset)

        
        backtrack(0, [])
        return res
