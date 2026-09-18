#count subarrays with sum 0 
nums = [1, -1, 2, -2, 3]

def subarray_sum(nums):
    count = 0
    prefix_sum = [0]

    for i in range(len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i])
        if prefix_sum[i] == 0:
            count += 1
    return count

print(subarray_sum(nums))