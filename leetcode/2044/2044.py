class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for x in nums:
            mx |= x

        self.res = 0

        def bf(start, curr):
            if curr == mx:
                self.res += 1
            for i in range(start, len(nums)):
                bf(i + 1, curr | nums[i])

        bf(0, 0)
        return self.res
