class Solution:
    def trap(self, heights: List[int]) -> int:
        water=0
        left=0
        right=len(heights)-1
        leftMax=0
        rightMax=0
        while left < right:
            if heights[left]< heights[right]:
                if heights[left]>leftMax:
                    leftMax=heights[left]
                else:
                    water +=leftMax-heights[left]
                left +=1
            else:
                if heights[right]>rightMax:
                    rightMax=heights[right]
                else:
                    water +=rightMax-heights[right]
                right -=1
        return water

        # n=len(heights)

        # leftMax=[0]*n
        # rightMax=[0]*n

        # leftMax[0]=heights[0]
        # for i in range(1,n):
        #     leftMax[i]=max(heights[i],leftMax[i-1])
        # rightMax[n-1]=heights[n-1]
        # for i in range(n-2,-1,-1):
        #     rightMax[i]=max(rightMax[i+1],heights[i])
        
        # water=0
        # for i in range(n):
        #     water +=min(leftMax[i],rightMax[i])-heights[i]
        
        # return water