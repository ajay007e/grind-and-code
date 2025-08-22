class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        mxx, mnx, mxy, mny = 0, 1001, 0, 1001
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    mxx = max(mxx, j)
                    mnx = min(mnx, j)
                    mxy = max(mxy, i)
                    mny = min(mny, i)
        return (mxx - mnx + 1) * (mxy - mny + 1)
