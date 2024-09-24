def caesarCipher(s, k):
    # Write your code here
    res = ''
    
    for ch in s:
        if 'a' <= ch <= 'z':
            res += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':
            res += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        else:
            res += ch
    return res


# I knew this one was going to involve converting to ascii and then back to char
# but I wasnt sure how to do that so I had to google the methods