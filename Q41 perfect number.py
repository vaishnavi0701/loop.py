num=int(input("enter number"))
i=1
a=0
while i<num:
    if num%i==0:
        a=a+i
    i=i+1
if a==num:
    print(num,"perfect number")
else:
    print(num,"not perfect number")


