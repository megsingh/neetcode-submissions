class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_elements = set(nums)
        start_indexes = list()
        for i in range(len(nums)):
            if nums[i]-1 not in unique_elements:
                start_indexes.append(nums[i])

        max_count = 0
        for i in range(len(start_indexes)):
            curr_num = start_indexes[i]+1
            curr_count = 1
            while(curr_num in unique_elements):
                curr_count= curr_count+1
                curr_num = curr_num+1
            max_count = max(max_count, curr_count)
        return max_count

        
        