import turtle

hibo =turtle.Screen()
hibo.bgcolor("black")
hibo.title("square table")

akcura=turtle.Turtle()
akcura.color("brown")


'''
akcura.circle(50)
akcura.left(90)
akcura.circle(-50)
akcura.left(90)
akcura.circle(50)
akcura.left(90)
akcura.circle(-50)

'''

turtle_colors = ["red", "yellow", "green", "white", "brown", "purple", "orange"]
for i in range(8):
    akcura.color(turtle_colors[i%7])
    akcura.circle(5 * i)
    akcura.left(i)
    akcura.circle(-5 * i)
    akcura.left(i)

#turtle.mainloop() olarak ta kullanılabilir.turtle.done yerine
#turtle.done()
turtle.mainloop()