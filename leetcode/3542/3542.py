class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, res, s = len(nums), 0, []

        for num in nums:
            while s and s[-1] > num:
                s.pop()
            if num == 0:
                continue
            if not s or s[-1] < num:
                s.append(num)
                res += 1
        return res
