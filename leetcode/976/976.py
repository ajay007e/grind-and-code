class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for k in range(n - 1, 1, -1):
            a, b, c = nums[k - 2], nums[k - 1], nums[k]
            if a + b > c:
                return a + b + c
        return res
