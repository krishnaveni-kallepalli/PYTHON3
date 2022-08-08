s=int(input("Enter start:"))
e=int(input("Enter end:"))
def prime(s,n):
    for i in range(s,e+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break;
            else:
               print(i)
prime(s,e)
