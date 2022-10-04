
import turtle
# Assign module and give pen size
olympics = turtle.Pen()
olympics.pensize(10)
# Blue ring
def blue():
    olympics.color("blue")
    olympics.up()
    olympics.goto(-115, -25)
    olympics.down()
    olympics.circle(60)
# Black ring
def black():
    olympics.color("black")
    olympics.up()
    olympics.goto(0, -25)
    olympics.down()
    olympics.circle(60)
# Red ring
def red():
    olympics.color("red")
    olympics.up()
    olympics.goto(115, -25)
    olympics.down()
    olympics.circle(60)
# Yellow ring
def yellow():
    olympics.color("yellow")
    olympics.up()
    olympics.goto(-57.5, -75)
    olympics.down()
    olympics.circle(60)
# Green ring
def green():
    olympics.color("green")
    olympics.up()
    olympics.goto(57.5, -75)
    olympics.down()
    olympics.circle(60)
# Calling functions
def run():
    blue()
    black()
    red()
    yellow()
    green()
#Run the code
run()
