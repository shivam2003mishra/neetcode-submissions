class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total =sum(nums)
        target = total  //k

        if total %k !=0:
            return False
        nums.sort(reverse=True)

        bucket=[0]*k

        def dfs(i):
            if i==len(nums):
                return True
            curr=nums[i]

            for c in range(k):
                if bucket[c] + curr > target:
                    continue
                bucket[c] +=curr

                if dfs(i+1):
                    return True
                bucket[c] -= curr

                if bucket[c]==0:
                    break

            return False
        return dfs(0)