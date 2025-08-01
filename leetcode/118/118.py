class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            new = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    new.append(1)
                else:
                    new.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(new)
        return res
