class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        fullBottles, emptyBottles, usedBottles, exchange = numBottles, 0, 0, numExchange
        while fullBottles > 0 or emptyBottles >= exchange:
            if emptyBottles >= exchange:
                emptyBottles -= exchange
                exchange += 1
                fullBottles += 1
            else:
                emptyBottles += fullBottles
                usedBottles += fullBottles
                fullBottles = 0
        return usedBottles
