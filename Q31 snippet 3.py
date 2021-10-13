i=1
num=int(input("enter number"))
while i<num:
    if num%i==0:
        print(num,"not prime number")
        break
    i=i+1
else:
    print(num,"prime number")
