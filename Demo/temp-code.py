
# def sum(a,b):
#     if b == 0:
#         return 1
    
#     return a*sum(a,b-1)

# print(sum(2,3))



# def sum(arr):
#     if len(arr) == 0:
#         return 0
#     return arr[0] + sum(arr[1:])
# print(sum([1,2,3,4]))

# def reverse(n):
#     if n == 0:
#         return 
#     print(n)
#     reverse(n-1)

# reverse(3)



# def factorial(n):
#     if n == 0 or  n == 1:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(4))

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    return fib(n-1) + fib(n-2)

print(fib(7))
    