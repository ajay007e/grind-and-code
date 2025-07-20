class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_deleted = False

    def add(self, words):
        curr = self
        for word in words:
            curr = curr.children[word]


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()
        for path in sorted(paths):
            root.add(path)

        def serialize(trie):
            if not trie.children:
                return ""
            string = []
            for folder, child in trie.children.items():
                string.append(folder + "(" + serialize(child) + ")")
            key = "".join(string)
            seen[key].append(trie)
            return key

        seen = defaultdict(list)
        serialize(root)

        for nodes in seen.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True

        def dfs(root, path):
            for folder, child in root.children.items():
                if not child.is_deleted:
                    curr = path + [folder]
                    res.append(curr)
                    dfs(child, curr)

        res = []
        dfs(root, [])
        return res
