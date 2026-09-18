# Find the Longest Subarray With Sum = K
nums = [1, -1, 5, -2, 3]
k = 3

def longest_subArray(nums,k):
    prefix_sum =[0]
    max_len = 0
    for i in range(len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i])

    for R in range(1, len(prefix_sum)):
        for L in range(R):
            if prefix_sum[R]- prefix_sum[L] == k:
                current_len = R - L
                max_len = max(max_len, current_len)

    return max_len


print(longest_subArray(nums,k))
                
