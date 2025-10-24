class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for n in range(n + 1, 10**7):
            map = Counter(str(n))
            next = False
            for k, v in map.items():
                if k != str(v):
                    next = True
                    break
            if next:
                continue
            return n
