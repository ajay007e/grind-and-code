class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for x in nums:
            if x == 0:
                count += 1
            elif count != 0:
                res += comb(count + 1, 2)
                count = 0
        if count != 0:
            res += comb(count + 1, 2)
        return res
