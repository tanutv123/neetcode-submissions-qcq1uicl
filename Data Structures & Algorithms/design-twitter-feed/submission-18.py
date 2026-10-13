class Twitter:

    def __init__(self):
        self.time = 0
        self.store = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.store[userId].append([self.time, tweetId])
        if len(self.store[userId]) > 10:
            self.store[userId].pop(0)
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        self.following[userId].add(userId)
        followees = self.following[userId]
        for followeeId in followees:
            if followeeId in self.store:
                index = len(self.store[followeeId]) - 1
                time, tweetId = self.store[followeeId][index]
                heapq.heappush(tweets, [time, tweetId, followeeId, index - 1])
        res = []
        while tweets and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(tweets)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.store[followeeId][index]
                heapq.heappush(tweets, [time, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
