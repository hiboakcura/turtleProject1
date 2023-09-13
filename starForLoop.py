import turtle

hibo =turtle.Screen()
hibo.bgcolor("green")
hibo.title("square table")


akcura=turtle.Turtle()

for i in range(5):
    akcura.forward(100)
    akcura.left(72)
    akcura.forward(100)
    akcura.right(144)
    

'''
akcura.forward(20)
akcura.left(72)
akcura.forward(20)
akcura.right(144)
akcura.forward(20)
akcura.left(72)
akcura.forward(20)
akcura.right(144)
akcura.forward(20)
akcura.left(72)
akcura.forward(20)
akcura.right(144)
akcura.forward(20)
akcura.left(72)
akcura.forward(20)
akcura.right(144)
akcura.forward(20)
akcura.left(72)
akcura.forward(20)

'''


'''

turtle_intence = turtle.Turtle()
num_sides = 5
angle =360/num_sides*2
side_lenght = 100

for i in range(num_sides):
    turtle_intence.forward(side_lenght)
    turtle_intence.left(angle)


'''
turtle.done()