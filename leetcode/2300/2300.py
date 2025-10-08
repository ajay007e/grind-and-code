class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        m = len(potions)
        potions.sort()

        @cache
        def bs(s):
            l, r = 0, m - 1
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] * s < success:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        res = []
        for x in spells:
            c = m - bs(x)
            print(c)
            res.append(c)
        return res
