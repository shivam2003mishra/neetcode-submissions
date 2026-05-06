class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        res=0
        min_length=len(nums)+1
        for right in range(len(nums)):
            res+=nums[right]

            while res >=target:
                window_size=right-left+1
                min_length=min(min_length,window_size)

                res -=nums[left]
                left +=1
        
        if min_length==len(nums)+1:
            return 0
        else:
            return min_length
        return min_length