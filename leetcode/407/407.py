class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])

        h = []

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    heapq.heappush(h, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        res = 0
        level = 0

        while h:
            height, i, j = heapq.heappop(h)
            level = max(level, height)
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                curr = heightMap[ni][nj]
                if curr == -1:
                    continue
                if level > curr:
                    res += level - curr
                heapq.heappush(h, (curr, ni, nj))
                heightMap[ni][nj] = -1
        return res
