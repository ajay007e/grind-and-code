class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1

        @cache
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0

            res = 0.25 * dp(a - 100, b)
            res += 0.25 * dp(a - 75, b - 25)
            res += 0.25 * dp(a - 50, b - 50)
            res += 0.25 * dp(a - 25, b - 75)
            return res

        return dp(n, n)
