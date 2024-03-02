def is_palindrome(s, i, j):
    if i >= j:
        return True 
    return is_palindrome(s, i + 1, j - 1) if s[i]==s[j] else False

input = "racecar"
input = 'TENET'
input = 'aaba'

print(
    f"String '{input}' is {'not ' if not is_palindrome(input, 0, len(input)-1) else ''}a palindrome!"
)