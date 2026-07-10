class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        len_stones = len(stones)

        for i in range(len_stones):
            heapq.heappush(pq, -stones[i])

        n= len_stones
        while n>1:
            stone1 = heapq.heappop(pq)
            stone2 = heapq.heappop(pq)
            n-=2

            if stone2 - stone1 > 0:
                heapq.heappush(pq, stone1-stone2)
                n+=1

        if n==0:
            return 0

        return -1 * heapq.heappop(pq)

            
        