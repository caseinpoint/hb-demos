def has_duplicates(nums):
	"""Check if there are any duplicates. O(n^2)"""

	for i in range(len(nums)):
		for j in range(len(nums)):
			# don't check the same index against itself
			if i == j:
				continue

			if nums[i] == nums[j]:
				return True

	return False

def has_duplicates_better(nums):
	"""Save some looping. Still O(n^2)"""

	for i in range(len(nums) - 1):
		# don't re-check indices that have already been checked
		for j in range(i + 1, len(nums)):
			if nums[i] == nums[j]:
				return True

	return False

def has_duplicates_best(nums):
	"""Use set for better runtime. O(n)"""

	nums_set = set(nums)

	return len(nums_set) != len(nums)
