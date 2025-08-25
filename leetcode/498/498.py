class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        d = defaultdict(list)

        for i in range(n):
            for j in range(m):
                d[m - 1 - j - i].append(mat[i][j])

        curr = 1
        res = []
        for k in d:
            if curr:
                res += d[k][::-1]
            else:
                res += d[k]
            curr ^= 1
        return res
