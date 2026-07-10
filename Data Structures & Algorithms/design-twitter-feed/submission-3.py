class Twitter:

    def __init__(self):
        self.time =0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [-time, tweetId, followeeId, index ])

        while heap and len(res)<10:
            time, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index-1 >=0:
                time, tweetId = self.tweetMap[followeeId][index-1]
                heapq.heappush(heap, [-time, tweetId, followeeId, index-1 ])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
