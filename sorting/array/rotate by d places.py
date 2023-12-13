def rotate_array(arr, n, k):
	# Reduce the number of rotations
	k %= n

	# Reverse the first part of the array
	arr[:n - k] = arr[:n - k][::-1]

	# Reverse the second part of the array
	arr[n - k:] = arr[n - k:][::-1]

	# Reverse the entire array
	arr[:] = arr[::-1]


# Driver code
arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2

rotate_array(arr, n, k)

for i in range(n):
	print(arr[i], end=" ")

print()

# This code is contributed by Dwaipayan Bandyopadhyay
