class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        orr=0
        for x in nums:
            orr |=x
        return orr * (1 << (len(nums)-1))