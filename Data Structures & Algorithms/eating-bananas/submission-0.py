class Solution:
    def canFinishBananas(self, piles, h, speed):
        res = 0
        n = len(piles)
        for i in range(n):
            time = piles[i]//speed if piles[i]%speed == 0 else piles[i]//speed + 1
            res += time
        return res <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l<r:
            mid = l + (r-l)//2
            if self.canFinishBananas(piles, h, mid):
                r = mid
            else:
                l = mid+1
        return r

            