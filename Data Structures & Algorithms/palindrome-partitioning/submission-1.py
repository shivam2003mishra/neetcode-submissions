class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def palindrome(start,end):
            while start < end:

                if s[start] != s[end]:
                    return False
                start +=1
                end -=1
            return True

        def dfs(start,curr):
            if start==len(s):
                res.append(curr.copy())
                return
            
            for end in range(start,len(s)):
                if palindrome(start,end):
                    curr.append(s[start:end+1])

                    dfs(end+1,curr)
                    curr.pop()
        dfs(0,[])
        return res