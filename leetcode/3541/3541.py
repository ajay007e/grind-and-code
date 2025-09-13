class Solution:
    def maxFreqSum(self, s: str) -> int:
        vhm = defaultdict(int)
        chm = defaultdict(int)
        consonants = 0
        for char in s:
            if char in "aeiou":
                vhm[char] += 1
            else:
                chm[char] += 1
        return (max(vhm.values()) if len(vhm.values()) else 0) + (
            max(chm.values()) if len(chm.values()) else 0
        )
