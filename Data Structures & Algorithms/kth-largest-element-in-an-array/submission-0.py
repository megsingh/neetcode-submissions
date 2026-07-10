class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        n = len(nums)

        for i in range(n):
            heapq.heappush(pq, -1 * nums[i])

        for i in range(k-1):
            heapq.heappop(pq)

        return -1 * pq[0]