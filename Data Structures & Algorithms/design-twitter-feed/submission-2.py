class Twitter:

    def __init__(self):

        #maps each person to the people they follow
        self.follows = defaultdict(set)

        #maps each person to the people that follow them
        self.followers = defaultdict(set)

        self.time = 0

        #maps each person to their maxheap feed of 10 vlaues (time, tweetid)
        # self.feeds = defaultdict(list)
        self.tweets = []

        

    def postTweet(self, userId: int, tweetId: int) -> None:

        # for follower in self.followers[userId]:

        #     heapq.heappush(self.feeds[follower], (self.time, tweetId))

        # heapq.heappush(self.feeds[userId], (self.time, tweetId))

        heapq.heappush(self.tweets, (self.time, userId, tweetId))
        
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        res= []
        store = []
        while len(res) < 10 and self.tweets:
            top = heapq.heappop(self.tweets)
            store.append(top)
            if top[1] in self.follows[userId] or top[1] == userId:
                res.append(top[2])
        for s in store:
            heapq.heappush(self.tweets, s)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        self.followers[followeeId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        self.followers[followeeId].discard(followerId)
        
