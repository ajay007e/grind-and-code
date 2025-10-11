class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        fm = defaultdict(int)
        for x in power:
            fm[x] += 1
        unique = sorted(list(fm.keys()))
        n, k, mx = len(unique), 0, 0
        dp = [0] * n

        for i in range(n):
            while k < i and unique[k] < unique[i] - 2:
                mx = max(mx, dp[k])
                k += 1
            val = unique[i]
            dp[i] = mx + val * fm[val]

        return max(dp)
