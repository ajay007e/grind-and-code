class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        xor = [0] * n

        def xor_dfs(node, parent):
            curr = nums[node]
            for nei in adj[node]:
                if nei != parent:
                    curr ^= xor_dfs(nei, node)
            xor[node] = curr
            return curr

        xor_dfs(0, -1)

        subtree_nodes = [0] * n

        def subtree_nodes_dfs(node, parent):
            curr = set([node])
            for nei in adj[node]:
                if nei != parent:
                    curr |= subtree_nodes_dfs(nei, node)
            subtree_nodes[node] = curr
            return curr

        subtree_nodes_dfs(0, -1)

        res = float("inf")
        for i in range(1, n):
            for j in range(i + 1, n):
                if j in subtree_nodes[i]:
                    a = xor[0] ^ xor[i]
                    b = xor[i] ^ xor[j]
                    c = xor[j]
                elif i in subtree_nodes[j]:
                    a = xor[0] ^ xor[j]
                    b = xor[i] ^ xor[j]
                    c = xor[i]
                else:
                    a = xor[0] ^ xor[i] ^ xor[j]
                    b = xor[i]
                    c = xor[j]
                res = min(res, max(a, b, c) - min(a, b, c))
        return res
