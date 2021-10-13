x=int(input("enter year"))
y=int(input("enter year"))
i=x
while i<=y:
    if i%4==0 and  i%400==0:
        print(i,"leap year")
    else:
        print(i,"not leap year")
    i=i+1


