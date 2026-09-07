def slidewindow(nums, k):
    window_sum = sum(nums[0:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(window_sum,max_sum)
    return max_sum



nums = [4,2,7,3,1,6]
k = 3
print(slidewindow(nums,k))