class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in rows[r] or cell in cols[c] or cell in sqrs[(r // 3, c // 3)]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                sqrs[(r // 3, c // 3)].add(cell)
        return True
