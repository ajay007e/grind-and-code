class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        curr, res = 0, 0
        for x in nums:
            if x == mx:
                curr += 1
            else:
                curr = 0
            res = max(res, curr)
        return res
