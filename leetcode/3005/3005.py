class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        freq = hm.values()
        mx = max(freq)
        res = 0
        for v in freq:
            if v == mx:
                res += mx
        return res
