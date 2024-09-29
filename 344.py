def reverseString(self, s):
    n = len(s)
    i = 0
    j = n - 1
    while i <= j:
        char_i = s[i]
        char_j = s[j]

        s[i] = char_j
        s[j] = char_i

        i += 1
        j -= 1
    return s