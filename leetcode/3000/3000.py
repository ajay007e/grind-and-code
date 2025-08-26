class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        mx, res = 0, 0
        for l, w in dimensions:
            d = sqrt(l**2 + w**2)
            if mx == d:
                res = max(res, l * w)
            elif mx < d:
                mx = d
                res = l * w
        return res
