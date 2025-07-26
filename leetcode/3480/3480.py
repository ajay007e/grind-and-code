class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        limits = defaultdict(list)
        for a, b in conflictingPairs:
            limits[max(a, b)].append(min(a, b))

        res, left = 0, [0, 0]
        afterRemoval = [0] * (n + 1)

        for r in range(1, n + 1):
            for l in limits[r]:
                if l > left[0]:
                    left[1] = left[0]
                    left[0] = l
                elif l > left[1]:
                    left[1] = l
            res += r - left[0]
            afterRemoval[left[0]] += left[0] - left[1]
        return res + max(afterRemoval)
