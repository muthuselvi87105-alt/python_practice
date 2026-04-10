def palindrome(s):
    start=0
    end=len(s)-1
    while start<end:
       if s[start]!=s[end]:
          return "not palindrome"
       start+=1
       end -=1
    return "palindrome"
print(palindrome("amma"))
