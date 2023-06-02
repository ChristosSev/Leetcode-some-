import re

def isPalindrome(s: str) -> bool:
    clean_string = re.sub(r'[\W_]+', '', s)
    lower_s = clean_string.lower()
    l = 0
    r = len(lower_s) - 1

    while l < r:
        if lower_s[l] != lower_s[r]:
            return False

        l += 1
        r -= 1

    return True

string = "A man, a plan, a canal, Panama!"
result = isPalindrome(string)
print(result)  # Output: True

