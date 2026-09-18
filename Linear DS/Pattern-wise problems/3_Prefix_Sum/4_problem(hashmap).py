# Find the Longest Subarray With Sum = K 
# using hashmap - it reduce the time complexity from O(n²)  to O(n)
nums = [1, -1, 5, -2, 3]
k = 3

def longest_subArray(nums, k):
    prefix_sum = [0]
    max_len = 0
    seen = {0: 0}
    for i in range(len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i])
        current_prefix = prefix_sum[i+1]
        needed = current_prefix - k

        if needed in seen:
            curr_len = (i+1) - seen[needed]
            max_len = max(max_len, curr_len) 
        if current_prefix not in seen:
            seen[current_prefix] = i+1

    return max_len

print(longest_subArray(nums,k))
        