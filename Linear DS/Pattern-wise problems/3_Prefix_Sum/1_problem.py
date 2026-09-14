# Range sum query
nums = [2,4,1,5,3]
L = 1
R = 3

def rangesum(nums, L, R):
    prefix_sum = []

    for i in range(len(nums)):
        if prefix_sum == []:
            prefix_sum.append(nums[i])
        else:
            prefix_sum.append(nums[i] + prefix_sum[i-1])

    if L == 0:
        return prefix_sum[R]
    if L > 0:
        return prefix_sum[R] - prefix_sum[L-1]

print(rangesum(nums, L, R)) 