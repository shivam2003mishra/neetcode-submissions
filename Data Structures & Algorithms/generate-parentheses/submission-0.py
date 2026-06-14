class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def dfs(curr,close_count,open_count):
            if len(curr)==2*n:
                res.append("".join(curr))
                return
            
            if open_count < n:
                curr.append('(')
                dfs(curr,close_count,open_count+1)
                curr.pop()
            
            if close_count < open_count:
                curr.append(')')
                dfs(curr,close_count+1,open_count)
                curr.pop()
        
        dfs([],0,0)
        return res