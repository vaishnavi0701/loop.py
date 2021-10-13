num=int(input("enter number of rows"))
row=0
while row<num:
    space=num-row-1
    while space>0:
        print(" ",end="")
        space=space-1
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()























# num=int(input("enter the number"))
# i=1
# while i<=num:
#     j=1
#     while j<=num-i:
#         print(" ",end="")
#         j=j+1
#     a=1
#     while a<=i:
#         print("*",end=" ")
#         a=a+1
#     i=i+1
#     print()
