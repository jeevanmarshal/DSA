def move_zeros(array):
    slow = 0
    for fast in range(len(array)):
        if array[fast] != 0:
            array[fast], array[slow] = array[slow], array[fast]
            slow += 1
    return array

arr = [0,1,0,3,12]

print(move_zeros(arr))