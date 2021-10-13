n=int(input("enter number"))
num=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
# print(sum)
if num==sum:
    print(sum,"amstrong number")
else:
    print(sum,"not amstrong number")