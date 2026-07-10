class Solution:
    def combinationSumHelper(self, nums: List[int], target: int, pos, res, subset, subset_sum):
        if subset_sum == target:
            res.append(subset.copy())
            return

        if subset_sum > target or pos >=len(nums):
            return

        subset.append(nums[pos])
        self.combinationSumHelper(nums, target, pos, res, subset, subset_sum + nums[pos])
        subset.pop()
        self.combinationSumHelper(nums, target, pos+1, res, subset, subset_sum)

        

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        subset_sum = 0

        pos = 0

        self.combinationSumHelper(nums, target, pos, res, subset, subset_sum)
        return res

