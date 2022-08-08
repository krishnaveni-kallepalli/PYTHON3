a=int(input())
b=int(input())
print("Maximum num is",max(a,b))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("Enter a:"))
b=int(input("Enter b:"))
ch=int(input("Enter choice(1/2/3/4):"))

if ch==1:
    print(add(a,b))
elif ch==2:
    print(sub(a,b))
elif ch==3:
    print(mul(a,b))
elif ch==4:
    print(div (a,b))
else:
    print("None")
