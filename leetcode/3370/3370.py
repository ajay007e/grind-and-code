class Solution:
    def smallestNumber(self, n: int) -> int:
        bits = 0
        while n > 0:
            bits += 1
            n //= 2
        return (2**bits) - 1
