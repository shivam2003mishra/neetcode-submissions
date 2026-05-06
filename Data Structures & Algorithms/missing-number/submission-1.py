class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual=0
        for m in nums:
            actual +=m
        n=len(nums)
        expected=n*(n+1)//2

        return expected-actual