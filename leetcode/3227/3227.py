class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for v in "aeiou":
            if v in s:
                return True
        return False
