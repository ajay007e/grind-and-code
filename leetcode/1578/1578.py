class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        n, res, i = len(colors), 0, 0

        while i < n:
            j, total, mx = i, 0, 0
            while j < n and colors[i] == colors[j]:
                t = neededTime[j]
                total += t
                mx = max(mx, t)
                j += 1
            res += total - mx
            i = j

        return res
