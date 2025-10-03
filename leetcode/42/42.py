class Solution:
    def trap(self, height: List[int]) -> int:
        n, h = len(height), []

        for i in range(n):
            if i == 0 or i == n - 1:
                heapq.heappush(h, (height[i], i))
                height[i] = -1

        res, level = 0, 0

        while h:
            hei, i = heapq.heappop(h)
            level = max(level, hei)
            for ni in (i + 1, i - 1):
                if ni < 0 or ni >= n:
                    continue
                curr = height[ni]
                if curr == -1:
                    continue
                if level > curr:
                    res += level - curr
                heapq.heappush(h, (curr, ni))
                height[ni] = -1
        return res
