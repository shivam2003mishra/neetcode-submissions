class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1

        m=len(nums1)
        n=len(nums2)

        left=0
        right=m

        while left <= right:
            partition1=(left+right)//2
            partition2=(m+n+1)//2 - partition1

            if partition1>0:
                maxLeft1=nums1[partition1-1]
            else:
                maxLeft1=float('-inf')
            
            if partition1<m:
                minRight1=nums1[partition1]
            else:
                minRight1=float('inf')

            if partition2>0:
                maxLeft2=nums2[partition2-1]
            else:
                maxLeft2=float('-inf')
            
            if partition2<n :
                minRight2=nums2[partition2]
            else:
                minRight2=float('inf')

            if maxLeft1<=minRight2 and maxLeft2<= minRight1:
                if (m+n)%2==1:
                    return float(max(maxLeft1,maxLeft2))
                else:
                    return float(max(maxLeft1,maxLeft2)+ min(minRight1, minRight2))/2.0
            elif maxLeft1 > minRight2:
                right=partition1-1
            else:
                left=partition1+1