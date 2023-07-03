from typing import List


class Solution:
    def exit(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def dfs(x, y, index):
            if board[x][y] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            board[x][y] = '#'
            for choice in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = x + choice[0], y + choice[1]
                if 0 <= nx < row and 0 <= ny < col and dfs(nx, ny, index + 1):
                    return True
            board[x][y] = word[index]

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
dfs1 = Solution()
print(dfs1.exit(board,word))