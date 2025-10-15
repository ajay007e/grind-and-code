class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        end_len = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                end_len[i] = end_len[i - 1] + 1
        start_len = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                start_len[i] = start_len[i + 1] + 1

        res = 1
        for i in range(n - 1):
            res = max(res, min(end_len[i], start_len[i + 1]))
        return res
