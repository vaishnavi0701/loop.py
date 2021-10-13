n=int(input("enter the number"))
num=n
sum=0
while n>0:
    sum=sum+(n%10)
    n=n//10
print(sum)
if num%sum==0:
    print(sum,"harshad number")
else:
    print(sum,"not harshad number")
    




