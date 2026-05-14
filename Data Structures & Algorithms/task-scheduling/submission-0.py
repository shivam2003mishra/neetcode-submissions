from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        maxFreq=max(freq.values())

        maxCount=0
        for f in freq.values():
            if f==maxFreq:
                maxCount +=1

        cycles=(maxFreq-1)*(n+1)+ maxCount

        return max(len(tasks),cycles)