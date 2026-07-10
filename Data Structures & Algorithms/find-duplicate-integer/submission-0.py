class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = set()

        for i in range(len(nums)):
            if nums[i] in unique:
                return nums[i]
            unique.add(nums[i])