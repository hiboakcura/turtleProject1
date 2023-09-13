import turtle

hibo =turtle.Screen()
hibo.bgcolor("light green")
hibo.title("square table")

akcura=turtle.Turtle()
kenar = 300
for i in range(100):
    kenar -=5
    akcura.forward(kenar)
    akcura.left(90)
    if kenar ==0:
        break

turtle.done()