def sum_of_digits(n):
    total=0
    while n>0:
     digits=n%10
     total=total+digits
     n=n//10
    return total
num=1234
print("sum of number:",sum_of_digits(num))
