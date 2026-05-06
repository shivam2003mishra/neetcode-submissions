class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # n=len(nums)
        # res=[]

        # for i in range(n-k+1):
        #     windowMax=nums[i]

        #     for j in range(i,i+k):
        #         windowMax=max(windowMax,nums[j])
        #     res.append(windowMax)
        # return res

        q=deque()
        l=0
        output=[]

        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if q[0]<l:
                q.popleft()

            if r+1 >=k:
                output.append(nums[q[0]])
                l+=1
            
        return output