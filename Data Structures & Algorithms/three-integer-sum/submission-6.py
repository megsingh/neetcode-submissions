class Solution:

    def twoSum(self, nums: List[int], start, target, len_nums)->List[List[int]]:
            res = list()
            print(target)
            end = len_nums-1
            while start<end:
                if nums[start] + nums[end] == target:
                    res.append([-1* target, nums[start],nums[end]])
                    start = start+1
                    while start < end and nums[start] == nums[start-1]:
                        start = start+1
                    
                elif nums[start] + nums[end] < target:
                    start = start+1
                else:
                    end = end-1
            print(res)
            return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        ans = list()
        for i in range(len_nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            res = self.twoSum(nums, i+1, target, len_nums)
            if len(res)>0:
                ans.extend(res)
        return ans
                
                    



