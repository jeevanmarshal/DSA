def remove_duplicates(array):
    slow = 0

    for fast in range(1, len(array)):
        if array[slow] != array[fast]:
            slow += 1
            array[slow] = array[fast]
    return slow + 1

arr = [1,1,2,2,2,3,4,4]
k = remove_duplicates(arr)

print(arr[:k])

