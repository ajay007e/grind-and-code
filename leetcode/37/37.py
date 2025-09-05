class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        r = defaultdict(set)
        c = defaultdict(set)
        b = defaultdict(set)

        fill = []

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == ".":
                    fill.append((i, j))
                else:
                    r[i].add(x)
                    c[j].add(x)
                    b[(i // 3, j // 3)].add(x)

        def bt(start):
            if start == len(fill):
                return True
            i, j = fill[start]
            for x in range(1, 10):
                x = str(x)
                if x not in r[i] and x not in c[j] and x not in b[(i // 3, j // 3)]:
                    board[i][j] = x
                    r[i].add(x)
                    c[j].add(x)
                    b[(i // 3, j // 3)].add(x)
                    if bt(start + 1):
                        return True
                    board[i][j] = "."
                    r[i].remove(x)
                    c[j].remove(x)
                    b[(i // 3, j // 3)].remove(x)
            return False

        bt(0)
