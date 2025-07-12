class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        self.res = set()
        f = firstPlayer - 1
        s = secondPlayer - 1

        @cache
        def dp(mask, round, i, j):
            if i >= j:
                dp(mask, round + 1, 0, n - 1)
            elif (mask & (1 << i)) == 0:
                dp(mask, round, i + 1, j)
            elif (mask & (1 << j)) == 0:
                dp(mask, round, i, j - 1)
            elif i == f and j == s:
                self.res.add(round)
            else:
                if i not in (f, s):
                    dp(mask ^ (1 << i), round, i + 1, j - 1)
                if j not in (f, s):
                    dp(mask ^ (1 << j), round, i + 1, j - 1)

        dp((1 << n) - 1, 1, 0, n - 1)
        dp.cache_clear()
        return [min(self.res), max(self.res)]
