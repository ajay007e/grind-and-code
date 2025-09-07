class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range(1, n):
            res.append(i)
        _sum = sum(res)
        res.append(_sum * -1)
        return res
