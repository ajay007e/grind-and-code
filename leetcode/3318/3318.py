class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []

        for i in range(k - 1, n):
            map = defaultdict(int)
            for j in range(i - (k - 1), i + 1):
                map[nums[j]] += 1

            curr = 0
            arr = list(map.items())
            arr.sort()
            arr.sort(key=lambda x: x[1])

            for j in range(x):
                if not arr:
                    break
                key, val = arr.pop()
                curr += key * val
            res.append(curr)
        return res
