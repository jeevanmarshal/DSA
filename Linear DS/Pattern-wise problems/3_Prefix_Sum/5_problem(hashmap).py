#count subarrays with sum 0  , using hashmap
nums = [1, -1, 2, -2, 3]

def subarray_sum(nums):
    count = 0
    prefix_sum = [0]
    seen = {0:1}

    for i in range(len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[i])
        current_prefix = prefix_sum[i+1] 
        needed = current_prefix - 0

        if needed in seen:
            count += seen[needed]
        seen[current_prefix] = seen.get(current_prefix, 0) + 1
    return count


print(subarray_sum(nums))