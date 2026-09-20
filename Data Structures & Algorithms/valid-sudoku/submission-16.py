class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):

                item = board[r][c]

                if item == ".": continue

                if(item in rows[r] or
                    item in cols[c] or
                    item in squares[(r//3, c//3)]):
                    return False
                
                rows[r].add(item)
                cols[c].add(item)
                squares[(r//3,c//3)].add(item)
        
        return True