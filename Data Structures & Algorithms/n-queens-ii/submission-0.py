class Solution:
    def totalNQueens(self, n: int) -> int:
        count=0
        board=[["."]*n for _ in range(n)]
        diagonal1=set()
        diag2=set()
        cols=set()

        def dfs(row):
            nonlocal count

            if row==n:
                count +=1
                return
            for col in range(n):
                if col in cols:
                    continue
                if (row-col) in diagonal1:
                    continue
                if (row+col) in diag2:
                    continue

                cols.add(col)
                diagonal1.add(row-col)
                diag2.add(row+col)
                board[row][col]="Q"

                dfs(row+1)

                board[row][col]="."
                cols.remove(col)
                diagonal1.remove(row-col)
                diag2.remove(row+col)
        dfs(0)
        return count