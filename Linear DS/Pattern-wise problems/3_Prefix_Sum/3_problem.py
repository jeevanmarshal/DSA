# Count Subarrays With Target Sum
nums = [1, 2, 1, 2, 1]
k = 3

def targetsum(nums, k):
    prefix_sum = []
    count = 0
    for i in range(len(nums)):
        if prefix_sum == []:
            prefix_sum.append(nums[i])
        else:
            prefix_sum.append(nums[i]+prefix_sum[i-1])

    for R in range(1, len(prefix_sum)):
        for L in range(R):
            if prefix_sum[R]- prefix_sum[L] == k:
                count += 1

    return count

print(targetsum(nums,k))
