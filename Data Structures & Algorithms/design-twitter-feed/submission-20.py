class Twitter:

    def __init__(self):
        self.store = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.store[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            ownTweetLen = len(self.store[followeeId])
            if ownTweetLen:
                index = ownTweetLen - 1
                cnt, tweetId = self.store[followeeId][index]
                heapq.heappush(tweets, [cnt, tweetId, followeeId, index - 1])
        
        res = []
        while len(res) < 10 and tweets:
            cnt, tweetId, userId, index = heapq.heappop(tweets)
            res.append(tweetId)
            if index >= 0:
                cnt, tweetId = self.store[userId][index]
                heapq.heappush(tweets, [cnt, tweetId, userId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
