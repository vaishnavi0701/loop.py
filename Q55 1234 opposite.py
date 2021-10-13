x=int(input("enter number"))
i=1
while i<=x:
    a=1
    while a<=x-i:
        print(" ",end=" ")
        a=a+1
    b=1
    while b<=i:
        print(b,end=" ")
        b=b+1
    i=i+1
    print()
