class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dp(i, o, z):
            if i == len(strs):
                return 0
            c = Counter(strs[i])
            no, nz = c["1"], c["0"]

            bst = float("-inf")
            bst = max(bst, dp(i + 1, o, z))
            if o + no <= n and z + nz <= m:
                bst = max(bst, 1 + dp(i + 1, o + no, z + nz))

            return bst

        return dp(0, 0, 0)
