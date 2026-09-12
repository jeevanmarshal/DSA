# Given s and k, find the longest substring containing at most k distinct characters.
# Hint: Variable window + frequency dictionary → shrink when distinct count > k.

s = 'aeabcd'
k = 2

def longest_substring(s, k):
    left = 0
    frequency = {}
    max_len = 0

    for right in range(len(s)):
        frequency[s[right]] = frequency.get(s[right],0) + 1

        while len(frequency) > k:
            frequency[s[left]] -= 1
            if frequency[s[left]] == 0:
                del frequency[s[left]]
            left +=1
        current_len = right - left + 1
        max_len = max(max_len, current_len)

    return max_len

print(longest_substring(s,k))
