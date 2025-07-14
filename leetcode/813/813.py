class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        p = [0]
        for x in nums:
            p.append(p[-1] + x)

        def avg(i, j):
            return (p[j] - p[i]) / float(j - i)

        n = len(nums)
        dp = [avg(i, n) for i in range(n)]
        for _ in range(k - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], avg(i, j) + dp[j])
        return dp[0]
