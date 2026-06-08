class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=nums[0]
        n=len(nums)

        for i in range(n):
            currSum=0
            for j in range(i,n):
                currSum +=nums[j]
                maxSum=max(maxSum,currSum)
        return maxSum