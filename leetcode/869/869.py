class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        signature = sorted(str(n))
        for i in range(30):
            power_of_two = 1 << i
            p_signature = sorted(str(power_of_two))
            if signature == p_signature:
                return True
        return False
