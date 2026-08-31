def is_palindrome(word):
    W = str(word)
    L = 0
    R = len(W)-1

    while L < R:
        if W[L] != W[R]:
            return 'Not a Palindrome'
        else:
            L += 1
            R -= 1

    return 'its an Palindrome'

print(is_palindrome('racecar'))

#Time: O(n)
#Space: O(1) for the pointer-based logic 