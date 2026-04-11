def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
x,y=map(int,input("enter the two number:").split())
x,y=swap(x,y)
print("After Swapping:",x,y)
