class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0

        for i in range(n):
            ax, ay = points[i]
            for j in range(n):
                if i == j:
                    continue
                bx, by = points[j]
                if not (ax <= bx and ay >= by):
                    continue

                skip = False
                for k in range(n):
                    if k == i or k == j:
                        continue
                    cx, cy = points[k]
                    if (cx >= ax and cx <= bx) and (cy <= ay and cy >= by):
                        skip = True
                        break
                if not skip:
                    res += 1
        return res
