from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # chopped code btw

        # check rows
        for c in range(9):
            s = set()
            for r in range(9):
                item = board[c][r]
                if item in s:
                    return False
                if item == ".":
                    continue
                s.add(item)

        # check cols
        for c in range(9):
            s = set()
            for r in range(9):
                item = board[r][c]
                if item in s:
                    return False
                if item == ".":
                    continue
                s.add(item)
        
        # check squares
        squares = defaultdict(set)
        for c in range(9):
            for r in range(9):
                key = ( c // 3, r // 3)
                item = board[c][r]
                if item in squares[key]:
                    return False
                if item == ".":
                    continue
                squares[key].add(item)

        return True

        