def remove_element(array,val):
    slow = 0
    for fast in range(len(array)):
        if array[fast] != val:
            array[slow] = array[fast]
            slow += 1 
    return slow


arr = [3,2,2,3]

k = remove_element(arr,3)

print(k)
print(arr[:k])