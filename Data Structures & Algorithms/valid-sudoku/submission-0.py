class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    cell = int(board[i][j])

                    box_index = (3*int(i/3) + int(j/3))
                    if (cell in row[i]) or (cell in col[j]) or (cell in box[box_index]):
                        return False
                    row[i].add(cell)
                    col[j].add(cell)
                    box[box_index].add(cell)
        return True