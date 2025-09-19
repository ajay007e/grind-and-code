class Spreadsheet:
    def __init__(self, rows: int):
        self.grid = [[0] * 26 for i in range(rows + 1)]

    def setCell(self, cell: str, value: int) -> None:
        self.grid[int(cell[1:])][ord(cell[0]) - ord("A")] = value

    def resetCell(self, cell: str) -> None:
        self.grid[int(cell[1:])][ord(cell[0]) - ord("A")] = 0

    def getValue(self, formula: str) -> int:
        curr = formula[1:].split("+")
        res = 0
        for val in curr:
            if val.isdigit():
                res += int(val)
            else:
                res += self.grid[int(val[1:])][ord(val[0]) - ord("A")]
        return res
