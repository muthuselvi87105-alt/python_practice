def check_prime(n):
    for i in range(2,n):
      if n%i==0:
        return "not prime"
    return "prime"
num=int(input("enter the number:"))
print("prime_or_not:",check_prime(num))
