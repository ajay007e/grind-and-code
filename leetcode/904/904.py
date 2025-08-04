class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res, l = 0, 0
        dict = defaultdict(int)
        for r in range(len(fruits)):
            dict[fruits[r]] += 1
            while len(dict) > 2:
                dict[fruits[l]] -= 1
                if dict[fruits[l]] == 0:
                    del dict[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
