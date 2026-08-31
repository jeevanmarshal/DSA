# #  print 1 to n 
# def print_1_to_n(n):
#     if n == 0:
#         return
    
#     print_1_to_n(n - 1)
#     print(n, end=' ')


# print_1_to_n(3)


# print('')

# # print n to 1

# def print_n_to_1(n):
#     for i in range(n):
#         print(n, end=' ')
#         n -=1

# print_n_to_1(3)

# print('')

# # factorial

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
    
#     return n*fact(n-1)

# print(fact(3))

# print('')


# GCD

# def gcd(a,b):
#     if b == 0:
#         return a
#     return gcd(b,a%b)

# print(gcd(54,24))

# # even or odd

# def evenOrodd(n):
#     if n%2 == 0:
#         return True
#     else :
#         return False
    
# print(evenOrodd(6))


# #  sum of first n natural number
# # method 1(recursion) - T O(1), S O(1)

# def sum(n):
#     if n == 1:
#         return 1
#     return n + sum(n-1)

# print(sum(5))

# # method 2 - T O(n) , S O(1)

# def sum(n):
#     sum = 0
#     i = 1

#     while i <= n:
#         sum += i
#         i += 1
#     return sum

# print(sum(4))


# closest number





