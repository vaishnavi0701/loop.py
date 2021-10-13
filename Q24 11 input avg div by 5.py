
n=11
i=1
sum=0
avg=0
while i<=n:
    num=int(input("enter age"))
    sum=sum+num
    avg=sum/n
    i=i+1
print(avg)
if avg%5==0:
    print(avg,"divisible by 5")
else:
    print(avg,"not divisible by 5 ")

                                            
                                            