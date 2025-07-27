class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        for m in range(1, len(nums) - 1):
            if nums[m] == nums[m - 1]:
                continue
            r, l = m + 1, m - 1
            while l > -1 and nums[l] == nums[m]:
                l -= 1
            while r < len(nums) and nums[r] == nums[m]:
                r += 1
            if l == -1 or r == len(nums):
                continue
            if nums[r] < nums[m] > nums[l] or nums[r] > nums[m] < nums[l]:
                res += 1
        return res
