class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        m = len(board)
        n = len(board[0])

        def backtrack(row, col, pos):
            if pos == len(word):
                return True

            if row >= m or col >= n or row <0 or col <0 or board[row][col]!= word[pos] or (row,col) in visited:
                return False
            
            visited.add((row,col))
            found = False
            for i in range(len(direction)):
                new_row = row + direction[i][0]
                new_col = col + direction[i][1]
                if backtrack(new_row, new_col, pos+1):
                    found = True
                    break
            visited.remove((row,col))
            return found           

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
        return False