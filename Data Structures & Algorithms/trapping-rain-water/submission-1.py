class Solution:
    def trap(self, height: List[int]) -> int:
        arr_len = len(height)
        leftMax = [0]*arr_len
        rightMax = [arr_len-1]*arr_len

        for i in range(1, arr_len):
            if height[i-1] > height[leftMax[i-1]]:
                leftMax[i] = i-1
            else:
                leftMax[i] = leftMax[i-1]

        for i in range(arr_len-2, -1, -1):
            if height[i+1] > height[rightMax[i+1]]:
                rightMax[i] = i+1
            else:
                rightMax[i] = rightMax[i+1]
        
        result = 0
        for i in range(arr_len):
            trapped_water= min(height[leftMax[i]], height[rightMax[i]]) - height[i]
            if trapped_water >0:
                result+=trapped_water
        return result
