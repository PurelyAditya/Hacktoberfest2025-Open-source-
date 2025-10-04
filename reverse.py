def rotate(nums, k):
    n = len(nums)
    k %= n  # In case k > n

    # Helper function to reverse a portion of the list
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse entire array
    reverse(0, n - 1)
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    # Step 3: Reverse remaining elements
    reverse(k, n - 1)

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
rotate(arr, 3)
print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]
