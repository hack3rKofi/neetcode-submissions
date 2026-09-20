class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        length = 9

        for r in range(length):
            for c in range(length):
                val = board[r][c]

                box = (r//3,c//3)

                if val == ".":
                    continue
                
                if val in rows[r] or val in cols[c] or val in squares[box]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[box].add(val)
            
        
        return True