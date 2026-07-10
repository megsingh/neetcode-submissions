class Solution:

    def permuteHelper(self, nums, pick, perm, res):
        if len(perm) ==len(nums):
            res.append(perm.copy())
            return

        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.permuteHelper(nums, pick, perm, res)
                perm.pop()
                pick[i] = False


    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.permuteHelper(nums, [False]*len(nums), [], res)
        return res