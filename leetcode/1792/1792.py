class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calc(p, t):
            curr = p / t
            new = (p + 1) / (t + 1)
            return new - curr

        heap = []
        for p, t in classes:
            heap.append((-calc(p, t), p, t))
        heapq.heapify(heap)

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            heapq.heappush(heap, (-calc(p + 1, t + 1), p + 1, t + 1))

        res = 0
        for _, p, t in heap:
            res += p / t
        return res / len(classes)
