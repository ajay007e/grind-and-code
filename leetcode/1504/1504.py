class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        height = [0] * n

        for i in range(m):
            for j in range(n):
                height[j] = height[j] + 1 if mat[i][j] == 1 else 0

            sub_res = [0] * n
            stack = [-1]
            for j in range(n):
                while stack[-1] != -1 and height[stack[-1]] >= height[j]:
                    stack.pop()
                k = stack[-1]
                sub_res[j] = height[j] * (j - k)
                if k != -1:
                    sub_res[j] += sub_res[k]
                stack.append(j)
            res += sum(sub_res)
        return res
