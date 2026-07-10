import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        n = len(points)

        for i in range(n):
            dist = math.sqrt(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(pq, [-1 * dist, points[i][0], points[i][1]])

            if len(pq) == k+1:
                heapq.heappop(pq)

        res = []

        for i in range(len(pq)):
            dist, x, y = heapq.heappop(pq)
            res.append([x,y])
        return res