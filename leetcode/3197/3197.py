class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:

        def area(t, b, l, r):
            top = b + 1
            bottom = -1
            left = r + 1
            right = -1

            for i in range(t, b + 1):
                for j in range(l, r + 1):
                    if grid[i][j] == 1:
                        top = min(top, i)
                        bottom = max(bottom, i)
                        left = min(left, j)
                        right = max(right, j)
            return (bottom - top + 1) * (right - left + 1)

        def solve(tar):
            res = float("inf")
            n = len(grid)
            m = len(grid[0])
            for i in range(n):
                for j in range(m):
                    res = min(
                        res,
                        area(0, i, 0, j)
                        + area(0, i, j + 1, m - 1)
                        + area(i + 1, n - 1, 0, m - 1),
                    )
                    if tar == res:
                        return tar
                    res = min(
                        res,
                        area(0, i, 0, m - 1)
                        + area(i + 1, n - 1, 0, j)
                        + area(i + 1, n - 1, j + 1, m - 1),
                    )
                    if tar == res:
                        return tar
            for i in range(n - 1):
                for j in range(i + 1, n - 1):
                    res = min(
                        res,
                        area(0, i, 0, m - 1)
                        + area(i + 1, j, 0, m - 1)
                        + area(j + 1, n - 1, 0, m - 1),
                    )
                    if tar == res:
                        return tar
            return res

        n = len(grid)
        m = len(grid[0])
        ones = 0

        for i in range(n):
            for j in range(m):
                ones += grid[i][j]

        out = solve(ones)
        if ones == out:
            return ones

        new_grid = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new_grid[j][n - 1 - i] = grid[i][j]
        grid = new_grid

        return min(solve(ones), out)
