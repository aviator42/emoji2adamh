import turtle
scn = turtle.Screen()
scn.bgcolor("green")


jim = turtle.Turtle()
dwight = turtle.Turtle()
michael = turtle.Turtle()
toby = turtle.Turtle()

jim.shape("turtle")
dwight.shape("turtle")
michael.shape("turtle")
toby.shape("turtle")

jim.penup()
jim.goto(-275, 45)
jim.pendown()

jim.fillcolor("red")
jim.begin_fill()

jim.pendown()
jim.right(100)
jim.circle(250)
jim.end_fill()

dwight.penup()
dwight.goto(-210, 45)
dwight.pendown()

dwight.fillcolor("yellow")
dwight.begin_fill()

dwight.pendown()
dwight.right(100)
dwight.circle(45)
dwight.end_fill()

michael.penup()
michael.goto(0, 45)
michael.pendown()

michael.fillcolor("yellow")
michael.begin_fill()

michael.pendown()
michael.right(100)
michael.circle(45)
michael.end_fill()

toby.penup()
toby.goto(-190, -100)
toby.pendown()

toby.pendown()
toby.color("black")
toby.right(-5)
toby.forward(300)

jim.penup()
jim.goto(-210, 160)
jim.pendown()

jim.fillcolor("red")
jim.begin_fill()

jim.pendown()
jim.right(135)
jim.forward(65)
jim.right(140)
jim.forward(80)
jim.end_fill()

dwight.penup()
dwight.goto(160, 160)
dwight.pendown()

dwight.fillcolor("red")
dwight.begin_fill()

dwight.pendown()
dwight.left(160)
dwight.forward(65)
dwight.left(140)
dwight.forward(80)
dwight.end_fill()
dwight.forward(80)

turtle.exitonclick()
