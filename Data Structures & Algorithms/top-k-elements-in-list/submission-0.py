from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)

        result=[]
        common=count.most_common(k)

        for word in common:
            result.append(word[0])
        return result