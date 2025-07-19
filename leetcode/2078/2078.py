class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        r, l, n = len(colors) - 1, 0, len(colors)
        while l <= r:
            if colors[r] != colors[0]:
                return r
            elif colors[l] != colors[n - 1]:
                return n - l - 1
            else:
                r -= 1
                l += 1
        return 0
