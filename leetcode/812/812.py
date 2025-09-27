class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        res = float("-inf")

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    a = sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
                    b = sqrt(abs(x3 - x2) ** 2 + abs(y3 - y2) ** 2)
                    c = sqrt(abs(x1 - x3) ** 2 + abs(y1 - y3) ** 2)
                    sp = (a + b + c) / 2

                    val = sp * (sp - a) * (sp - b) * (sp - c)
                    res = max(res, sqrt(max(0, val)))
        return res
