def check_palindrome(n):
    original=n
    rev=0
    while n>0:
      digit=n%10
      rev=rev*10+digit
      n=n//10
    if original == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
n=int(input("enter the number:"))
output=(check_palindrome(n))
print(output)

