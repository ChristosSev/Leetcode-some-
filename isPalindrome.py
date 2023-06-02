import re

def isPalindrome (s:str) -> bool:
    str = s.lower()
    str= re.sub(r'[\W_]', '', str)
    #print(str)
    l = 0
    r = len(str) - 1

    while l < r:
          print(r)
          print(l)
          if str[l] != str[r]:
             return False
          l+=1
          r-=1
    return True


str ='Bia_BIA'
print(isPalindrome(str))
