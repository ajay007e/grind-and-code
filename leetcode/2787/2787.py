class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(acc, i):
            if acc == 0:
                return 1
            if acc < 0:
                return 0

            curr = pow(i, x, MOD)
            if curr > acc:
                return 0
            res = dp(acc - curr, i + 1)
            res += dp(acc, i + 1)
            res %= MOD
            return res

        return dp(n, 1)
