def factorial(num):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    return factorial
num=int(input("enter the number:"))
result=(factorial(num))
print(result)
