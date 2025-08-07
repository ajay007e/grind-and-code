class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        res = sum(fruits[i][i] for i in range(n))

        def dp():
            grid = [[0] * n for _ in range(n)]
            grid[0][n - 1] = fruits[0][n - 1]

            for i in range(1, n - 1):
                for j in range(max(i + 1, n - 1 - i), n):
                    best = max(grid[i - 1][j], grid[i - 1][j - 1])
                    if j < n - 1:
                        best = max(best, grid[i - 1][j + 1])
                    grid[i][j] = best + fruits[i][j]

            return grid[n - 2][n - 1]

        res += dp()

        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]

        res += dp()
        return res
