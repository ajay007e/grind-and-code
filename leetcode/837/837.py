class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # https://www.youtube.com/watch?v=zKi4LzjK27k
        if k == 0:
            return 1.0
        windowSum = 0
        for i in range(k, k + maxPts):
            windowSum += 1 if i <= n else 0

        dp = {}
        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts
            dec = 0
            if i + maxPts <= n:
                dec = dp.get(i + maxPts, 1)
            windowSum += dp[i] - dec
        return dp[0]
