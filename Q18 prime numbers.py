num=int(input("enter number"))
i=1
a=0
while i<=num:
    if num%i==0:
        a=a+1
    i=i+1
if a==2:
    print(num,"prime number")
else:
    print(num,"not prime number")




# x=int(input("enter number : "))
# if x%2!=0:
#     print(x,"prime no")
# elif x==2:
#     print(x,"also prime no")
# else:
#     print(x,"not prime no")
# if x%2==0:
#     print("even number")
# else:
#     print("odd")


# i=1
# while i<=100:
#     j=2
#     x=0
#     while j<i-1:
#         if i%j==0:
#             x=x+1
#         j=j+1
#     if i!=1 and x==0:
#         print(i,"prime number")
#     else:
#         print(i,"not prime number")
#     i=i+1
