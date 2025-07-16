class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        res = 0
        for num in nums:
            i, j = num - k, num + k
            if i in dic:
                res += dic[i]
            if j in dic:
                res += dic[j]
            dic[num] += 1
        return res
