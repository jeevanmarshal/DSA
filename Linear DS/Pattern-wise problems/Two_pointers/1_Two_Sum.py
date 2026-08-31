def two_sum(target, array):
    left = 0
    right = len(array)-1

    while left < right:
        correct_sum = array[left] + array[right]

        if correct_sum == target:
            return [left,right]
        elif correct_sum < target:
            left += 1
        else:
            right -=1
    return[]

array = [1,2,4,6,8,10]
target = 12
print(two_sum(target,array))
