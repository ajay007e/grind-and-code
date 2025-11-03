class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
    ) -> int:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        obs = set()
        seen = set()

        for r, c in walls:
            seen.add((r, c))
            obs.add((r, c))

        q = deque()
        for r, c in guards:
            seen.add((r, c))
            obs.add((r, c))
            for d in range(4):
                q.append((r, c, d))

        while q:
            r, c, d = q.popleft()
            dr, dc = dirs[d]
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in obs:
                continue
            q.append((nr, nc, d))
            seen.add((nr, nc))

        return (n * m) - len(seen)
