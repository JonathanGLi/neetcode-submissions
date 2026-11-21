class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -=1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []

        for t in self.tweets[userId][-10:]:
            heapq.heappush(heap, t)

        for f in self.follows[userId]:
            for t in self.tweets[f][-10:]:
                heapq.heappush(heap, t)

        res =[]

        for i in range (10):
            if heap:
                (t, t_id) = heapq.heappop(heap)
                res.append(t_id)

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
