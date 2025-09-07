class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        n = len(queries)
        res = 0

        def operations(x):
            base = 1
            bits = 1
            ops = 0
            while base <= x:
                ops += (min(base * 2 - 1, x) - base + 1) * ((bits + 1) // 2)
                bits += 1
                base *= 2
            return ops

        for (
            l,
            r,
        ) in queries:
            res += (operations(r) - operations(l - 1) + 1) // 2

        return res
