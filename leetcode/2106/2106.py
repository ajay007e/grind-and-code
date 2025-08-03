class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        res, curr = 0, 0

        def steps(l, r):
            if startPos >= fruits[r][0]:
                return startPos - fruits[l][0]
            elif startPos <= fruits[l][0]:
                return fruits[r][0] - startPos
            else:
                return (
                    min(startPos - fruits[l][0], fruits[r][0] - startPos)
                    + fruits[r][0]
                    - fruits[l][0]
                )

        l = 0
        for r in range(n):
            curr += fruits[r][1]
            while l <= r and steps(l, r) > k:
                curr -= fruits[l][1]
                l += 1
            res = max(res, curr)
        return res
