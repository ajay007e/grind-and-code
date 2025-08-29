class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        en = n // 2
        on = n // 2
        if n % 2 != 0:
            on += 1

        em = m // 2
        om = m // 2
        if m % 2 != 0:
            om += 1

        return (en * om) + (em * on)
