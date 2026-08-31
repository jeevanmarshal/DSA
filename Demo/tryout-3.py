#  to find the count of the number in the given array

# numbers = [1,2,2,3,3,3,4]
numbers = [1,2,3,2,1,4,5]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    
    else:
         frequency[number] = 1
        
for number in frequency:
    if number <=2:
        print(number)
