class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position = dict()
        for index in range(0,len(nums)):
            if target - nums[index] in position:
                second_index = position[target-nums[index]]
                return [min(index, second_index), max(index, second_index)]
            position[nums[index]] = index


               