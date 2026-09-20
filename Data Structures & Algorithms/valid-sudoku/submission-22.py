class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9):
            for c in range(9):

                i = board[r][c]
                s = squares[r//3,c//3]

                if i == ".": continue

                if (i in rows[r] or i in cols[c] or i in s):
                    return False
                
                rows[r].add(i)
                cols[c].add(i)
                s.add(i)
        
        return True