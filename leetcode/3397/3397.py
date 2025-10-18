class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n, mn, res = len(nums), float("-inf"), 0

        for num in nums:
            curr = max(mn + 1, num - k)
            if curr <= num + k:
                res += 1
                mn = curr
        return res
