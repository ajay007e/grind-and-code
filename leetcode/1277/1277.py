class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r == R or c == C or not matrix[r][c]:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            cache[(r, c)] = 1 + min(
                helper(r + 1, c), helper(r, c + 1), helper(r + 1, c + 1)
            )
            return cache[(r, c)]

        res = 0
        for r in range(R):
            for c in range(C):
                res += helper(r, c)
        return res
