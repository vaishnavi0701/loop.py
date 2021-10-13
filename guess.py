import random
x=20
y=int(x*random.random())+1
z=0
while z!=y:
    z=int(input("enter number"))
    if z>0:
        if (z>y):
            print("number is too large")
        elif (z<y):
            print("number is too small")
    else:
        print("sorry you are giving up")
else:
    print("congratulayions.you made it!")