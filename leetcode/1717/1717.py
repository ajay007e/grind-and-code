class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def solve(op, stack):
            tmp, score = [], 0
            for i in range(len(self.stack)):
                if not tmp or tmp[-1] != op[0] or self.stack[i] != op[1]:
                    tmp.append(self.stack[i])
                else:
                    tmp.pop()
                    score += x if op == "ab" else y
            self.stack = tmp
            return score

        res, self.stack = 0, list(s)
        if x > y:
            res += solve("ab", self.stack)
            res += solve("ba", self.stack)
        else:
            res += solve("ba", self.stack)
            res += solve("ab", self.stack)

        return res
