class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 2 * k + 1):
            f1, f2 = True, True
            for j in range(i + 1, i + k):
                if nums[j] <= nums[j - 1]:
                    f1 = False
                    break
            for j in range(i + k + 1, i + k + k):
                if nums[j] <= nums[j - 1]:
                    f1 = False
                    break
            if f1 and f2:
                return True
        return False
