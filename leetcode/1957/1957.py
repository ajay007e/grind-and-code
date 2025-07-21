class Solution:
    def makeFancyString(self, s: str) -> str:
        prev, cnt, res = "", 0, ""
        for char in s:
            if prev == char:
                cnt += 1
            else:
                cnt = 0
            if cnt < 2:
                res += char
            prev = char
        return res
