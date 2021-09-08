nums = [1,2,2,3,3,5,5,5,25,75,75,75,97,97,97,97]


def left(nums,target):
	res = None
	l = 0
	r = len(nums)-1
	while l<=r:
		m = r-(r-l)//2
		if nums[m]<target:
			l = m + 1
		else:
			if nums[m]==target:
				res = m
			r = m - 1
	return res
def right(nums,target):
	res = None
	l = 0
	r = len(nums)-1
	while l<=r:
		m = r-(r-l)//2
		if nums[m]>target:
			r = m - 1
		else:
			if nums[m]==target:
				res = m
			l = m + 1

	return res

def count_ele(nums,target):
	l = left(nums,target)
	r = right(nums,target)
	return r-l+1 if l!=None else 0

def sum_target(nums):
	for i in range(len(nums)):
		hash = {}
		for j in range(len(nums)):
			if nums[i]-nums[j] in hash and hash[nums[i]-nums[j]]!=i:
				return (i,j,hash[nums[i]-nums[j]])
			hash[nums[j]] = j
	return None
def diff_target(nums,k):
	hash = {}
	for j in range(len(nums)):
		if nums[j]-k in hash:
			return (j,hash[nums[j]-k])
		hash[nums[j]] = j
	return None
print(sum_target(nums),diff_target(nums,2))
