
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
       c=nums1+nums2
       le=len(c)
       c=sorted(c)

       if le%2==0:
         median = (c[le//2 - 1] + c[le//2]) / 2.0
       else:
            median = c[le//2]
          
       return median



nums1=[1,2]
nums2=[3,4]
c=Solution()
c.findMedianSortedArrays(nums1,nums2)
print(c.findMedianSortedArrays(nums1,nums2))

