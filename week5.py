arr = ['a','e','d','w','a','d','q','a','f','p']

def max_freq_alpha(arr):
	count = [0 for i in range((26))]
	for i in arr:
		count[ord(i)-ord('a')]+=1
	m = max(count)
	if m<=1:
		print("No Duplicate")
	else:
		for i in range(len(count)):
			if count[i]==m:
				print(chr(i+ord('a')),m)



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
def duplicate(arr,target):
	mergesort(arr,0,len(arr)-1)
	c = 0
	for i in arr:
		if i==target:
			c+=1
	return c>1
def target_sum(arr,target):
	mergesort(arr,0,len(arr)-1)
	i = 0
	j = len(arr)-1
	print(arr)
	F = True
	while i<j:
		if arr[i]+arr[j]==target:
			F = False
			print(arr[i],arr[j])
			i+=1
		if arr[i]+arr[j]<target:
			i+=1
		else:
			j-=1
	if F:
		print("No Such Pairs Exists")
def common_sorted(arr1,arr2):

	i = 0
	j = 0
	inter = []
	while i<len(arr1) and j<len(arr2):
		if arr1[i]==arr2[j]:
			inter.append(arr1[i])
			i+=1
			j+=1
		elif arr1[i]>arr2[j]:
			j+=1
		else:
			i+=1
	print(inter)
