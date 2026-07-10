class Solution:
    def combinationSumHelper(self, nums: List[int], target: int, pos, res, subset, subset_sum):
        if subset_sum == target:
            res.add(tuple(subset.copy()))
            return

        if subset_sum > target or pos >=len(nums):
            return

        subset.append(nums[pos])
        self.combinationSumHelper(nums, target, pos+1, res, subset, subset_sum + nums[pos])
        subset.pop()

        while pos+1 < len(nums) and nums[pos] == nums[pos+1]:
            pos+=1
        self.combinationSumHelper(nums, target, pos+1, res, subset, subset_sum)
        

    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        subset = []
        subset_sum = 0
        nums.sort()

        pos = 0

        self.combinationSumHelper(nums, target, pos, res, subset, subset_sum)
        return [list(subset) for subset in res]        