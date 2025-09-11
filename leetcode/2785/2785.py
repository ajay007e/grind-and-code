class Solution:
    def sortVowels(self, s: str) -> str:
        v = []
        res = ""
        for char in s:
            if char.lower() in ("a", "e", "i", "o", "u"):
                v.append(char)
        v.sort()

        for i in range(len(s)):
            if s[i].lower() in ("a", "e", "i", "o", "u"):
                res += v.pop(0)
            else:
                res += s[i]

        return res
