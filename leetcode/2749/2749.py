class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 33):
            curr = num1 - k * num2
            if k >= curr.bit_count() and curr >= k:
                return k
        return -1
