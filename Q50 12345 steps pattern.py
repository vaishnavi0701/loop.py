# x=int(input("enter number"))
# i=1
# while i<=x:
#     j=1
#     while j<=i:  
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1



# x=int(input("enter number"))
# i=1
# while i<=5:
    
#     while j<=i:  


#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1
# prime_list=[]
# i=1
# while i<=100:
#     j=2
#     x=0
#     while j<i-1:
#         if i%j==0:
#             x=x+1
#         j=j+1
#     if i!=1 and x==0:
#         prime_list.append(i)
#     else:
#         pass
#     i=i+1



# x=int(input("enter number"))
# i=1
# while i<=x:
#     if i==2:
#         for k in range(i-1):
#             print(i)
#     else:
#         j=1
#         while j<=i+1:
#             print(j,end=" ")
#             j=j+2
#     print()
#     i=i+1



x=int(input("enter number"))
i=1
c=0
while i<=x:
    if x%i==0:
        c+=1
if c==2:
    print(x,"prime")
else:
    print('not')
i+=1