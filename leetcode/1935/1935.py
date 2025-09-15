class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        mk = set(list(brokenLetters))
        words = text.split()
        res = 0
        for word in words:
            flag = True
            for char in word:
                if char in mk:
                    flag = False
                    break
            res += 1 if flag else 0
        return res
