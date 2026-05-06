class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(0,len(nums)):
            ans=1
            for j in range(0,len(nums)):
                if i!=j:
                    ans*=nums[j]
            res.append(ans)
        return res