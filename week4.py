def mergesort(arr,l,r):
	comp = 0
	if r-l>=1:
		m = r-(r-l)//2
		q = mergesort(arr,l,m-1)
		
		w = mergesort(arr,m,r)

		L = arr[l:m]

		R = arr[m:r+1]

		i = j = 0

		k = l

		while i<len(L) and j<len(R):
			if L[i]<R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k] = R[j]
				j+=1
			comp+=1
			k+=1
		while i<len(L):
			arr[k] = L[i]
			k+=1
			i+=1
		while j<len(R):
			arr[k] = R[j]
			k+=1
			j+=1
		comp+=q+w
	return comp
def analyze_merge_sort(arr):
	comp = mergesort(arr,0,len(arr)-1)
	print("Inversion: ",arr,"Comparisons: ",comp)
from random import randint
arr = []
for i in range(10):
	arr.append(randint(0,10))
def quicksort(arr , left = 0 , right = len(arr)-1):
	if left>=right:
		return

	pivot = arr[left]

	index = partition(arr,left,right,pivot)

	quicksort(arr,left,index-1)

	quicksort(arr,index,right)

def partition(arr,l,r,pivot):
	while l<=r:
		while l<r and arr[l]<pivot:
			l+=1
		while r>l and arr[r]>pivot:
			r-=1
		if l<=r:
			arr[l],arr[r] = arr[r],arr[l]
			l+=1
			r-=1
	return l
print(arr)
quicksort(arr)
print(arr)