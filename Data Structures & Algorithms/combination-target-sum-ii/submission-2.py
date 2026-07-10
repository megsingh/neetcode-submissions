class Solution:
    def combinationSumHelper(self, nums, target, pos, res, subset, subset_sum):
        if subset_sum == target:
            res.append(subset.copy())
            return

        if subset_sum > target:
            return

        for i in range(pos, len(nums)):
            # skip duplicates
            if i > pos and nums[i] == nums[i-1]:
                continue

            subset.append(nums[i])
            self.combinationSumHelper(nums, target, i + 1, res, subset, subset_sum + nums[i])
            subset.pop()

    def combinationSum2(self, nums, target):
        nums.sort()
        res = []
        self.combinationSumHelper(nums, target, 0, res, [], 0)
        return res