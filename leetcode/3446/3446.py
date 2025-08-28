class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        d = defaultdict(list)

        for i in range(n):
            for j in range(n):
                d[i - j].append(grid[i][j])

        for k in d:
            if k < 0:
                d[k].sort(reverse=True)
            else:
                d[k].sort()

        for i in range(n):
            for j in range(n):
                grid[i][j] = d[i - j].pop()

        return grid
