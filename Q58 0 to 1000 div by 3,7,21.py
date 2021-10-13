   

    

# i=1
# while i<=1000:
#     if i%3==0:
#         print(i,"nav")
#     elif i%7==0:
#         print(i,"gurukul")
#     elif i%21==0:
#         print(i,"navgurukul")
#     else:
#         print(i)
#     i=i+1



import turtle
pen=turtle.Turtle()
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(133)
    curve()
    pen .left(120)
    curve()
    pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color("black")
    pen.write("Aai",font=("z003",40,"bold"))             
heart()
pen.resizable("false","false","false","false","false","false","false")
txt()
pen.ht()



import turtle
pen=turtle.Turtle()
def curve():
    for i in range  (200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor("red")
    pen.begin_fill()
    pen.left(140)
    pen.forward(133)
    curve()
    pen .left(120)
    curve()
    pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color("black")
    pen.write("vaishnavi",font=("z003",30,"bold"))
heart()
pen.resizable("false","false","false","false" ,"false")
txt()
pen.ht()
