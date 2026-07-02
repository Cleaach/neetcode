class Twitter:

    def __init__(self):
        self.arr = []
        self.count = 0
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.arr.append((userId, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        c = 0
        for i in range(self.count - 1, -1, -1):
            p = self.arr[i]
            if p[0] == userId or p[0] in self.following[userId]:
                res.append(p[1])
                c += 1

            if c == 10:
                break

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
