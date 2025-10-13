class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        fm = [Counter(words[i]) for i in range(n)]

        res = [words[0]]
        for i in range(1, n):
            if fm[i] != fm[i - 1]:
                res.append(words[i])

        return res
