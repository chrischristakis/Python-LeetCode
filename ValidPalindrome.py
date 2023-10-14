def valid_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    return True


print(valid_palindrome('A man, a plan, a canal: Panama'))
print(valid_palindrome('race a car'))
print(valid_palindrome(''))