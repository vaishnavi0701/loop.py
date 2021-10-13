# i=1
# x=65
# while i<=5:
#     j=1
#     while j<=5:
#         print(chr(x),end="")
#         j=j+1
#         x=x+1
#     print()
#     i=i+1



for i in range (65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")
        
    print()


