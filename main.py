import turtle
import threading
from numpy import random

##
drawing_board=turtle.Screen()
drawing_board.bgcolor("light green")
drawing_board.setup(1000,700)

arrow_turtle = turtle.Turtle()
arrow_turtle.shape("turtle")
arrow_turtle.shapesize(2)
arrow_turtle.speed(10)
arrow_turtle.penup()
arrow_turtle.pencolor("red")
##
boards = turtle.Turtle()
boards.hideturtle()
boards.penup()
boards.goto(-300,-300)
boards.pen(pensize=5)
boards.pendown()
for i in range(4):
    boards.forward(600)
    boards.left(90)
##
score = 0
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(360, 290)
score_turtle.write(f"Score: {score:02}", align="center", font=("Arial", 15, "normal"))

def tikla(x,y):
        global score
        score += 1
        print(f"Tıklama yapıldı! Koordinatlar: ({x}, {y}) and score: {score}")
        score_turtle.clear()

        score_turtle.write(f"Score: {score:02}", align="center", font=("Arial", 15, "normal"))
arrow_turtle.onclick(tikla)
##

seconds = 10
def update_timer():
    global seconds
    seconds -= 1
    #Clear the previous timer text
    timer_turtle.clear()
    # Display the updated timer
    timer_turtle.write(f"Time: {seconds:02}", align="center", font=("Arial", 15, "normal"))
    if seconds == 0:
        arrow_turtle.hideturtle()
        arrow_turtle.goto(0,-250)
        arrow_turtle.write(f"Game Over\n  Score: {score} ", align="center", font=("Arial", 25, "normal"))
    # Schedule the function to run again after 1 second
    else :
        timer_thread = threading.Timer(1, update_timer)
        timer_thread.daemon = True
        timer_thread.start()
        arrow_turtle.goto(random.randint(-285, 285), random.randint(-285, 285))

# Create a turtle for the timer display
timer_turtle = turtle.Turtle()
timer_turtle.penup()
timer_turtle.hideturtle()
timer_turtle.goto(360, 250)
update_timer()
turtle.mainloop()