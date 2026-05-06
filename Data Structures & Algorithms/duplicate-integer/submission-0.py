class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            temp=nums[i]
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False