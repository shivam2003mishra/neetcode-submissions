class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum =0
        
        min_sum=nums[0]
        max_sum=nums[0]

        cur_min=0
        cur_max=0

        for n in nums:
            cur_max=max(n,cur_max+n)
            max_sum=max(max_sum,cur_max)

            cur_min=min(n,cur_min +n)
            min_sum=min(min_sum,cur_min)

            total_sum +=n

        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum-min_sum)