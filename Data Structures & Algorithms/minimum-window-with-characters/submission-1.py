from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t)>len(s):
            return ""

        need=Counter(t)
        missing=len(t)
        left=start=0
        min_len=float('inf')

        for right in range(len(s)):
            if need[s[right]]>0:
                missing -=1

            need[s[right]]-=1

            if missing==0:
                while left <right and need[s[left]]<0:
                    need[s[left]]+=1
                    left +=1
                if right-left <min_len:
                    start=left
                    min_len=right-left
                
                need[s[left]]+=1
                missing +=1
                left+=1
        return "" if min_len==float('inf') else s[start:start+min_len+1]