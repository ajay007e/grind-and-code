class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        frequency = Counter(basket1)
        frequency.subtract(Counter(basket2))

        to_swap = []
        print(frequency)
        for cost, count in frequency.items():
            if count % 2 != 0:
                return -1

            for _ in range(abs(count) // 2):
                to_swap.append(cost)

        to_swap.sort()
        min_overall_cost = min(basket1 + basket2)
        res = 0

        for i in range(len(to_swap) // 2):
            direct_swap = to_swap[i]
            indirect_swap = 2 * min_overall_cost
            res += min(direct_swap, indirect_swap)

        return res
