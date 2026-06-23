class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=[["."]*n for _ in range(n)]
        cols=set()
        diag1=set()
        diag2=set()

        def dfs(row):
            if row==n:
                solution=[]

                for r in board:
                    solution.append("".join(r))
                ans.append(solution)
                return 
            
            for col in range(n):
                if col in cols:
                    continue
                if (row-col) in diag1:
                    continue
                if (row+col) in diag2:
                    continue
                
                board[row][col]='Q'
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)

                dfs(row+1)

                board[row][col]="."
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)

        dfs(0)
        return ans
