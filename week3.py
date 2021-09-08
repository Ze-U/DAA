


def mergesort(arr,l,r):
	if r-l>=1:
		m = r-(r-l)//2
		mergesort(arr,l,m-1)
		
		mergesort(arr,m,r)

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
			k+=1
		while i<len(L):
			arr[k] = L[i]
			k+=1
			i+=1
		while j<len(R):
			arr[k] = R[j]
			k+=1
			j+=1
arr = [-13,65,-21,76,46,89,45,12]
def duplicate(arr,target):
	mergesort(arr,0,len(arr)-1)
	c = 0
	for i in arr:
		if i==target:
			c+=1
	return c>1
# print(duplicate(arr,2))

def selection_sort(arr):
	counter = 0
	swaps = 0
	for i in range(len(arr)):
		ind = i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[ind]:
				ind = j
			counter+=1
		swaps+=1
		arr[ind],arr[i] = arr[i],arr[ind]
	print(arr,"Swaps: ",swaps,"Comparisons: ",counter)
	return arr
def insertionSort(arr):
	shift = 0
	comp = 0
	for i in range(1,len(arr)):
		key = arr[i]
		j = i -1
		while j>=0 and key < arr[j]:
			arr[j+1] = arr[j]
			j-=1
			comp+=1
			shift+=1
		shift+=1
		arr[j+1] = key
	print(arr,"Comparisons: ",comp,"Shifts: ",shift)
	return arr

print(insertionSort(arr))
