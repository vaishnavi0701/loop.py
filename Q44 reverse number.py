n=int(input("enter number"))
i=0
while n>0:
    i=(i*10)+n%10
    n=n//10
print(i)
i=i+1

