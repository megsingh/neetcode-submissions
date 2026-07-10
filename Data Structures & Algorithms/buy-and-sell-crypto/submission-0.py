class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr_len = len(prices)

        left_min, right_max = [-1]*arr_len, [-1]*arr_len
        total_profit = 0
        left_min[0] = prices[0]
        for i in range(1, arr_len):
            left_min[i] = min(left_min[i-1], prices[i])

        for i in range(arr_len-2, -1,-1):
            right_max[i] = max(right_max[i+1], prices[i+1])
            profit = right_max[i] - left_min[i]
            total_profit = max(profit, total_profit)
        return total_profit