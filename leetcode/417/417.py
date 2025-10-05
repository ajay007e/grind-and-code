class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        pv, av = set(), set()

        def dfs(v, r, c, h):
            if r < 0 or r >= n or c < 0 or c >= m:
                return

            if (r, c) in v:
                return

            curr = heights[r][c]
            if curr < h:
                return

            v.add((r, c))

            for dr, dc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                dfs(v, dr, dc, curr)

        for r in range(n):
            dfs(pv, r, 0, heights[r][0])
            dfs(av, r, m - 1, heights[r][m - 1])
        for c in range(m):
            dfs(pv, 0, c, heights[0][c])
            dfs(av, n - 1, c, heights[n - 1][c])

        res = [list(cell) for cell in pv & av]
        return res
