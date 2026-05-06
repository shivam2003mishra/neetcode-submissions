class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def findPeak():
            left=0
            right=mountainArr.length()-1

            while left < right:
                mid=left+(right-left)//2

                if mountainArr.get(mid)<mountainArr.get(mid+1):
                    left=mid+1
                else:
                    right=mid
            return left
        
        def binarySearchInc(left,right):
            while left <= right:

                mid=left + (right-left)//2
                val=mountainArr.get(mid)

                if val==target:
                    return mid
                elif val < target:
                    left=mid+1
                else:
                    right=mid-1
            return -1
        
        def binarySearchDec(left,right):
            while left<= right:

                mid=left+(right-left)//2
                val=mountainArr.get(mid)

                if val==target:
                    return mid
                elif val <target:
                    right=mid-1
                else:
                    left=mid+1
            return -1
        
        peak=findPeak()
        
        res= binarySearchInc(0,peak)

        if res== -1:
            res=binarySearchDec(peak+1, mountainArr.length()-1)
        
        return res