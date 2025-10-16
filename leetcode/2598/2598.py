class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        fm = defaultdict(int)
        for num in nums:
            mod = num % value
            fm[mod] += 1
        n = 0
        while True:
            if fm[n % value] == 0:
                return n
            fm[n % value] -= 1
            n += 1
