class Solution:
    def missingRange(self, arr, low, high):
        arry_set=set(arr)
        result = []
       
        for num in range(low, high + 1):  # Step 2
            if num not in arry_set:        # Step 3
                result.append(num)
    
        return result
     
     
ar=[3,6, 13, 19,24,14,7]
l=9
h=18

obj=Solution()
print(obj.missingRange(ar, l, h))


