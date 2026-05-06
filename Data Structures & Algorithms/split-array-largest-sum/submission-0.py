class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(maxSum):
            curr=0
            count=1

            for n in nums:
                if curr+n>maxSum:
                    count+=1
                    curr=0
                curr+=n
            
            return count <= k
        
        left=max(nums)
        right=sum(nums)

        while left < right:
            mid=left +(right-left)//2

            if canSplit(mid):
                right=mid
            else:
                left=mid+1
        return left