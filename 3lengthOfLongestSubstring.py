def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0
    #r = l +1
    for r in range(0, len(s)):
        #print(r)
        #print(s[r])
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        res = max(res, r-l+1) #l-r+1 einai to parathyro
    return res

str = "abcabcbb"



print(lengthOfLongestSubstring(str))
