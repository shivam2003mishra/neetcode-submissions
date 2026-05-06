class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # res=[]
        # i=0
        # for s in nums:
        #     if s != val:
        #         res.append(s)
        #         i+=1
        # nums[:i]=res
        # return i

        i=0
        for j in range(len(nums)):
            if nums[j] !=val:
                nums[i]=nums[j]
                i+=1
        return i