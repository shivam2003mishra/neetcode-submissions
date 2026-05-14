import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        new_tasks=[]
        n=len(tasks)
        for i,(arrival,burst) in enumerate(tasks):
            new_tasks.append((arrival,burst,i))
        
        new_tasks.sort()
        i=0
        result=[]
        heap=[]
        time=0

        while i<n or heap :
            if not heap and time < new_tasks[i][0]:
                time=new_tasks[i][0]

            while i<n and new_tasks[i][0] <= time:
                arrival,burst,index=new_tasks[i]
                heapq.heappush(heap,(burst,index))

                i +=1
            burst,idx =heapq.heappop(heap)
            time +=burst

            result.append(idx)
        
        return result