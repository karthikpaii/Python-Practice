class Solution:
	def pythagoreanTriplet(self, arr):
		li=[]
		for num in arr:
			ar=[num**2  for num in arr]
			for i in ar:
				for j in ar:
					for k in ar:
						if ar[i]+ar[j]==ar[k]:
							return num[i],num[j],num[k]

arr=[3,2,4,6,5]
c=Solution()
print(c.pythagoreanTriplet(arr))