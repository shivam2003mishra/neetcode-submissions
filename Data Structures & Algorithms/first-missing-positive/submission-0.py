class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=1
        s=set(nums)
        while True:
            if i not in s:
                return i
            i +=1
