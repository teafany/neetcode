from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # chopped code btw

        # check rows
        for r in range(9):
            s = set()
            for c in range(9):
                item = board[r][c]
                if item in s:
                    return False
                if item == ".":
                    continue
                s.add(item)

        # check cols
        for r in range(9):
            s = set()
            for c in range(9):
                item = board[c][r]
                if item in s:
                    return False
                if item == ".":
                    continue
                s.add(item)
        
        # check squares
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                key = ( r // 3, c // 3)
                item = board[r][c]
                if item in squares[key]:
                    return False
                if item == ".":
                    continue
                squares[key].add(item)

        return True

        