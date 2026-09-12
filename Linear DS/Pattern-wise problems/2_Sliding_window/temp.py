def con_max_vowel(s,k):
    vowel_count = 0
    max_vowels = vowel_count

    for i in range(k):
        if s[i] in 'aeiou':
            vowel_count +=1

    for i in range(k, len(s)):
        if s[i-k] in 'aeiou':
            vowel_count -=1

        if s[i] in 'aeiou':
            vowel_count +=1

        max_vowels = max(max_vowels, vowel_count)
    return max_vowels

s = 'abciiidef'
k = 3

print(con_max_vowel(s,k))