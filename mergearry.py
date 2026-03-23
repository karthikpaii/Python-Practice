class Solution(object):
    def merge(self, nums1, m, nums2, n):
       s=m+n
       

       for i in range(n):
          for j in range(m):
            
             if nums1[i]!=nums2[j]:
                 nums1[i]=nums1[i]
             else:
                nums1[i]=nums2[j]

       return nums1


nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
c=Solution()
print(c.merge(nums1,m,nums2,n))



catalan = [0] * (n + 1)  
print(catalan)