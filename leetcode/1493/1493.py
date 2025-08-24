class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        flag = False
        l, res = 0, 0
        for r in range(len(nums)):
            if not nums[r]:
                while flag:
                    if not nums[l]:
                        flag = False
                    l += 1
                flag = True
            res = max(res, r - l)
        return res
