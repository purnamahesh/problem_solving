def is_palindrome(s: str) -> bool:
    def solve(s: str, i: int, j: int):
        if i >= j:
            return True 
        return solve(s, i + 1, j - 1) if s[i]==s[j] else False
    return solve(s, 0, len(s)-1)

if __name__ == '__main__':
    input = "racecar"
    # input = 'TENET'
    # input = 'aaba'

    print(
        f"String '{input}' is {'not ' if not is_palindrome(input) else ''}a palindrome!"
    )