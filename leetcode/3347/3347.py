class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0

        fm = defaultdict(int)
        l, r = 0, 0
        for x in nums:
            while r < n and nums[r] <= x + k:
                fm[nums[r]] += 1
                r += 1
            while l < n and nums[l] < x - k:
                fm[nums[l]] -= 1
                l += 1

            mx_ops = r - l - fm[x]
            res = max(res, min(mx_ops, numOperations) + fm[x])

        l = 0
        for r in range(n):
            while l < n and nums[l] + (k * 2) < nums[r]:
                l += 1
            mx_ops = r - l + 1
            res = max(res, min(mx_ops, numOperations))

        return res
