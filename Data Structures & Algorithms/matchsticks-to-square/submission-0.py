class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total=sum(matchsticks)
        if total % 4 !=0:
            return False
        side=total //4

        matchsticks.sort(reverse=True)
        sides=[0]*4

        def dfs(idx):
            if idx==len(matchsticks):
                return True
            curr=matchsticks[idx]

            for c in range(4):
                if sides[c]+ curr > side:
                    continue
                
                sides[c] +=curr

                if dfs(idx +1):
                    return True
                sides[c] -=curr
            return False
        return dfs(0)