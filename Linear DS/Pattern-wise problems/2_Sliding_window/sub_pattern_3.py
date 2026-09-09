def max_conscutive_len(char):

    left = 0
    seen = set()
    best = 0

    for right in range(len(char)):

        while char[right] in seen:
            seen.remove(char[left])
            left += 1

        seen.add(char[right])

        current_len = right - left + 1
        best = max(best, current_len)

    return best

char = ['b','c','a','d','e','c','f','g','h']

print(max_conscutive_len(char))

