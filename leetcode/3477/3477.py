class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res, n = 0, len(fruits)
        for fruit in fruits:
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    res += 1
                    break
        return n - res
