# Revision:
# Given positive nums and target, find the minimum length of a contiguous subarray with sum >= target.
# Hint: Variable window → expand until valid, shrink while valid.

nums = [2,3,1,2,4,3]
target = 7

def min_subarray_len(nums, target):
    left = 0
    window_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            current_len = right - left + 1    
            min_len = min(min_len, current_len)
            window_sum -= nums[left]
            left += 1
    if min_len == float('inf'):
        return 0

    return min_len

print(min_subarray_len(nums,target))