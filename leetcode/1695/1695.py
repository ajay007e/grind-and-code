class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res, score, l = 0, 0, 0
        map = defaultdict(int)

        for r in range(len(nums)):
            new = nums[r]
            map[new] += 1
            score += new
            while l < r and map[new] == 2:
                old = nums[l]
                map[old] -= 1
                score -= old
                l += 1
            res = max(res, score)
        return res
