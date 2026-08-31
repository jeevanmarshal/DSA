# List[]

# nums =[1,2,3,4,5]
# nums.append(6)
# nums.remove(2)
# nums[0] = 9
# print(nums)

# print(4 in nums )

# for i in nums:
#     print(i)

# for i in range(len(nums)):
#     print(i,':', nums[i])

# Tuple()

# nums = (10,20,30,40)
# a,b,c,d = nums 

# print(nums)
# print(a,d)


#Set{}

# s ={1,2,2,4}
# r ={3,4,5,5}
# s.add(5)

# s.add(5)
# s.discard(0)
# print(s)

# print(s&r)
# print(s-r)
# print(s|r)



# Dict {key : value}

# marks = {"Arun": 90, "Kumar":87}

# marks["Bala"] = 78
# marks["Arun"] = 65
# print(marks.get("Arun"))
# print(marks)


# easy-1

box = [1,2,3,4,5,6]
print()
for b in box:
    if b%2==0:
        print(b, end=' ')

# easy-2

text  = 'hello'
def count(text):
    dict = {}
    for letter in text:
        dict[letter] = dict.get(letter, 0)+1
    return dict
print(count(text))

# medium-1

a ={1,2,3,4}
b ={3,4,5,6}

print(a&b)