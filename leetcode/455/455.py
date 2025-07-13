class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res, i = 0, 0
        g.sort()
        s.sort()
        for j in range(len(s)):
            if g[i] <= s[j]:
                res += 1
                i += 1
                if i == len(g):
                    break
        return res
