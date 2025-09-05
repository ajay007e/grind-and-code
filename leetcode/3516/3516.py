class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx = abs(z - x)
        dy = abs(z - y)
        if dx == dy:
            return 0
        return 1 if dx < dy else 2
