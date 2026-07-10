class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sorted_nums = sorted(nums)
        # nums_len = len(nums)
        # for index in range(1, nums_len):
        #     if sorted_nums[index] == sorted_nums[index-1]:
        #         return True
        # return False

        frequency = {}
        nums_len = len(nums)
        for index in range(nums_len):
            if nums[index] in frequency:
                return True
            else:
                frequency[nums[index]]=1
        return False
         