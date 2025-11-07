class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        diff = [0] * (n + 1)

        for i in range(n):
            diff[max(0, i - r)] += stations[i]
            diff[min(n, i + r + 1)] -= stations[i]

        def check(target):
            dc = diff[:]
            ps, available = 0, k
            for i in range(n):
                ps += dc[i]
                if ps < target:
                    add = target - ps
                    if add > available:
                        return False
                    ps += add
                    dc[min(n, i + r * 2 + 1)] -= add
                    available -= add
            return True

        left, right = min(stations), sum(stations) + k
        while left < right:
            mid = left + (right - left + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left
