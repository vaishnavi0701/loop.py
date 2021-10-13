num=int(input("enter number"))
i=0
while i<=num:
    a=1
    while a<=num-i:
        print(" ",end=" ")
        a=a+1
    b=1
    while b<=i:
        print("",b,end="")
        b=b+1
    c=i+1
    while c>=1:
        print("",c,end="")
        c=c-1
    i=i+1
    print()

