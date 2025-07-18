class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        part_one = [0] * (n + 1)
        total = sum(nums[:n])
        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)
        part_one[0] = total

        for i in range(n, n * 2):
            total += nums[i]
            heapq.heappush(max_heap, -nums[i])
            total -= -heapq.heappop(max_heap)
            part_one[i - (n - 1)] = total

        part_two = sum(nums[n * 2 :])
        min_heap = nums[n * 2 :]
        heapq.heapify(min_heap)
        ans = part_one[n] - part_two

        for i in range(n * 2 - 1, n - 1, -1):
            part_two += nums[i]
            heapq.heappush(min_heap, nums[i])
            part_two -= heapq.heappop(min_heap)
            ans = min(ans, part_one[i - n] - part_two)

        return ans
