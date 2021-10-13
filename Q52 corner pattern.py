x=int(input("enter number"))
i=0
while i<=x:
    j=1
    while j<=x-i:
        print("*",end="")
        j=j+1
    print()
    i=i+1