class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(id, pg_id):
            seen.add(id)
            pg.append(id)
            id_pg[id] = pg_id
            for nei in adj[id]:
                if nei not in seen:
                    dfs(nei, pg_id)

        seen = set()
        id_pg = {}
        pgs = {}
        pgs_s = {}
        pg_id = 1

        for id in range(1, c + 1):
            if id in seen:
                continue
            pg = []
            dfs(id, pg_id)
            pgs_s[pg_id] = set(pg)
            heapq.heapify(pg)
            pgs[pg_id] = pg
            pg_id += 1

        res = []
        for t, id in queries:
            pgi = id_pg[id]
            pg_set = pgs_s[pgi]
            pg_heap = pgs[pgi]

            if t == 1:
                if id in pg_set:
                    res.append(id)
                else:
                    while pg_heap and pg_heap[0] not in pg_set:
                        heapq.heappop(pg_heap)
                    if pg_heap:
                        res.append(pg_heap[0])
                    else:
                        res.append(-1)
            else:
                if id in pg_set:
                    pg_set.remove(id)

        return res
