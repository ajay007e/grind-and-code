class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst = [0] * 32
        res = [0] * n

        for i in range(n - 1, -1, -1):
            for bit in range(32):
                if nums[i] & (1 << bit):
                    lst[bit] = i
            res[i] = max(1, max(lst) - i + 1)
        return res
