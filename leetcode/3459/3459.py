class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dirs = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

        @cache
        def dfs(i, j, target, turn, dir):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != target:
                return 0

            target = 0 if target == 2 else 2
            ni = i + dirs[dir][0]
            nj = j + dirs[dir][1]
            total = 0

            if turn:
                total = max(total, dfs(ni, nj, target, True, dir) + 1)
            else:
                total = max(total, dfs(ni, nj, target, False, dir) + 1)
                new_dir = (dir + 1) % 4
                ni = i + dirs[new_dir][0]
                nj = j + dirs[new_dir][1]

                total = max(total, dfs(ni, nj, target, True, new_dir) + 1)

            return total

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        res = max(
                            res, dfs(i + dirs[d][0], j + dirs[d][1], 2, False, d) + 1
                        )
        return res
