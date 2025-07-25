class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = 0
        for x in set(nums):
            res += x if x > 0 else 0
        return res if max(nums) > 0 else max(nums)
