class Solution:
    def totalMoney(self, n: int) -> int:
        fm = {}
        fm[0] = 1
        i, res = 1, 1
        while i < n:
            d = i % 7
            if d == 0:
                fm[d] += 1
            else:
                fm[d] = fm[d - 1] + 1
            res += fm[d]
            i += 1
        return res
