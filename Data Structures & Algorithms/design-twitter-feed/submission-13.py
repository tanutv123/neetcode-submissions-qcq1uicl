class Twitter:

    def __init__(self):
        self.time = 0
        self.store = {} #userId: [[time, tweetId]]
        self.following = {} #followerId: [followeeId1, followeeId2]

    def postTweet(self, userId: int, tweetId: int) -> None:
        if (userId not in self.store):
            self.store[userId] = []
        
        self.store[userId].append([-self.time, tweetId])
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.store.get(userId, []).copy()
        if userId in self.following:
            followees = self.following[userId]
            for followeeId in followees:
                tweets = tweets + self.store[followeeId]
        heapq.heapify(tweets)
        res = []
        maxIndex = 10 if len(tweets) > 10 else len(tweets)
        for _ in range(0, maxIndex):
            res.append(heapq.heappop(tweets)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if (followerId not in self.following):
            self.following[followerId] = set()
        
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
