class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        prev = [0] * n

        for j in range(m):
            mx, t = 0, 0
            for i in range(n):
                mx = max(mx, prev[i] - t)
                t += skill[i] * mana[j]
                prev[i] = t

            for k in range(n):
                prev[k] += mx

        return prev[-1]
