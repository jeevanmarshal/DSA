# Target Subarray Sum
nums = [3, 2, 5, 1, 4]
k = 6

def targetsum(nums, k):
    prefix_sum = []
    
    for i in range(len(nums)):
        if prefix_sum == []:
            prefix_sum.append(nums[i])
        else:
            prefix_sum.append(nums[i]+prefix_sum[i-1])

    for R in range(1, len(prefix_sum)):
        for L in range(R):
            if prefix_sum[R]- prefix_sum[L] == k:
                return True
    return False
print(targetsum(nums,k))
