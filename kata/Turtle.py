import turtle
def tur():
    turtle.shape('turtle')
    turtle.width(2)
    turtle.speed(20)
    for i in range(360):
        turtle.forward(3)
        turtle.left(1)

print(tur())
