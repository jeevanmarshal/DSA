# Given nums and k, find the maximum sum of any contiguous subarray of size k.
# Hint: Fixed-size sliding window → remove outgoing + add incoming.

nums = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum_subarray(nums, k):
    window_sum = sum(nums[0:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(window_sum, max_sum)

    return max_sum

print(max_sum_subarray(nums, k))