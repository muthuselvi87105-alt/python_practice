def find_largest(arr):
   largest=arr[0]
   for num in arr:
     if num>largest:
        largest=num
   return largest
numbers=list(map(int,input("enter the number:").split()))
print("largest number:",find_largest(numbers))
