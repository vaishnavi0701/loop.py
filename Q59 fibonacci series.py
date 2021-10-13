# fibonacii series


num=int(input("enter number:"))

a,b=0,1
count=0
while count<num:
    if count==0:
        print(0)
    print(b)
    a,b=b,a+b
    count=count+1

z=int(input("enter no:"))
j=0
while j<z:
    if j%z==0:
        # print(j)
        j=j+1
    print(j)




# z=int(input("enter no:"))
# y=int(input("enter no:"))