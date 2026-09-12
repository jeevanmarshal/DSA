# Given a string s and k, find the maximum number of vowels in any substring of size k.
# Hint: Fixed-size window + vowel count.

s = "abciiidef"
k = 3

def max_vowel(s,k):
    vowel_count = 0
    
    for i in range(k):
        if s[i] in 'aeiou':
            vowel_count += 1

    max_vowels = vowel_count
    for i in range(k, len(s)):
        if s[i-k] in 'aeiou':
            vowel_count -=1
        if s[i] in 'aeiou':
            vowel_count +=1

        max_vowels = max(max_vowels, vowel_count)
    return max_vowels

print(max_vowel(s,k))