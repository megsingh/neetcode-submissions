from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        l = 0
        r = len(self.timemap[key])-1
        timestamps = self.timemap[key].keys()
        ans = -1
        while l <= r:
            mid = l + (r-l)//2
            if timestamps[mid] <= timestamp:
                ans = mid
                l = mid+1
            else:
                r = mid-1
        if ans==-1:
            return ""
        else:
            return self.timemap[key][timestamps[ans]]

        

