# numbers = [10,20,5,30,25]

# largest = numbers[0]
# second_largest = numbers[0]

# for number in numbers:
#     if number > largest:
#         second_largest = largest
#         largest = number
#     elif number > second_largest and number != largest:
#         second_largest = number

# print(second_largest)

numbers = [4,7,1,9,3]

smaller = numbers[0]

for number in numbers:
    if number < smaller:
        smaller = number
    

print(smaller)