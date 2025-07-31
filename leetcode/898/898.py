class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        curr = set()

        for x in arr:
            curr = {x} | {y | x for y in curr}
            ans |= curr

        return len(ans)
