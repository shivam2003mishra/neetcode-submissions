class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans=1
        up=down=1

        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                up=down +1
                down=1
            elif arr[i]<arr[i-1]:
                down=up+1
                up=1
            else:
                up=down=1
            ans=max(ans,up,down)
        return ans