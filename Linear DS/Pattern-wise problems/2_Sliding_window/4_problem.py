# Given positive nums and k, find the maximum length of a contiguous subarray with sum <= k.
# Hint: Variable window → shrink while sum > k, then update maximum.

nums = [1, 2, 1, 1, 3]
k = 4

def max_subarray_len(nums, k):
    left = 0
    window_sum = 0
    max_len = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > k:
            window_sum -= nums[left]
            left += 1
        current_len = right - left + 1
        max_len = max(max_len, current_len)

    return max_len

print(max_subarray_len(nums, k))


