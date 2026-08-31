# def sum(arr):
#     if len(arr) == 0:
#         return 0


#     return  arr[0] + sum(arr[1:])

# print(sum([1,2,3,4]))

# def reverse(n):
#     if n == 0:
#         return 0
    
#     print(n)
#     reverse(n-1)

# reverse(4)

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
    
#     return n*fact(n-1)

# print(fact(5))

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     return fib(n-1) + fib(n-2)

# print(fib(8))


# palindrome

# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
    
#     return is_palindrome(s[1:-1])

# print(is_palindrome("madam"))    


# def sum_of_digits(n):
#     if n == 0:
#         return 0
    
#     return n%10 + sum_of_digits(n//10)

# print(sum_of_digits(123456789))

# def reverse(n):
#     if len(n) <= 1:
#         return n
    
#     return n[-1].lower() + reverse(n[:-1].lower())

# print(reverse("Hello"))

# def gcd(a,b):
#     if b ==0:
#         return a
#     return gcd(b,a%b)

# print(gcd(54, 24))


def toh(n, source, destination, helper):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination} ")
        return
    toh(n-1,source, helper, destination)
    print(f"Move disk {n} from {source} to {destination} ")

    toh(n-1,helper, destination, source)
    
toh(2,'A','C','B')