class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        n = len(nums)
        ans = []
        for i in range(n):
            target = -1 * nums[i]
            left = 0
            right = n-1
            while left < right:
                # print(left, right, target)
                if left ==i or nums[left]+nums[right]<target:
                    left = left+1
                elif right ==i or nums[left]+nums[right]>target:
                    right = right-1
                elif nums[left] + nums[right]==target:
                    
                    res = sorted([nums[left], nums[right], -1 *target])
                    ans.append(res)
                    left = left+1
                    right = right-1

        ans.sort()
        final_ans = [ans[0]] if len(ans)>0 else []
        for i in range(1, len(ans)):
            if ans[i][0] == ans[i-1][0] and ans[i][1] == ans[i-1][1] and ans[i][2] == ans[i-1][2]:
                continue
            final_ans.append(ans[i])
        return final_ans


# -4 -1 -1 0 1 2
# l            r t = 0
#     l.   l r

# -1, -1, 2
# -1, 0, 1
# -1, -1, 2
# -1, 0, 1

       




