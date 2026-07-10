class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1]*n
        right_prod = [1]*n

   

        left_prod[0] = nums[0]
        right_prod[n-1] = nums[n-1]
        for i in range(1,n):
            left_prod[i] = left_prod[i-1]*nums[i]

        for i in range(n-2,-1,-1):
            right_prod[i] = right_prod[i+1]*nums[i]

        res = []
        for i in range(n):
            left_res = left_prod[i-1] if i>0 else 1
            right_res = right_prod[i+1] if i<n-1 else 1

            res.append(left_res * right_res)
        return res