class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()

        for i in range(9):
            for j in range(9):
                val=board[i][j]

                if val=='.':
                    continue
                if (val,i) in seen:
                    return False
                if (j,val) in seen:
                    return False
                if (i//3,j//3,val) in seen:
                    return False
                
                seen.add((val,i))
                seen.add((j,val))
                seen.add((i//3,j//3,val))

        return True