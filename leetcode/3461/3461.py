class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        for i in range(n - 2):
            m = len(s)
            res = ""
            for j in range(m - 1):
                res += str((int(s[j]) + int(s[j + 1])) % 10)
            s = res
        return s[0] == s[1]
