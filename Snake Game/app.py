import turtle
import random
import time
from tkinter import PhotoImage

delay = 0.1
points = 0
high_score = 0
snake = []

min_width = 600
min_height = 600

window = turtle.Screen()
window.title("The Legendary Snake Game")
window.bgcolor("black")
window.setup(width=min_width, height=min_height)
window.tracer(0) 

border = turtle.Turtle()
border.penup()
border.goto(-300, 300)
border.pendown()
border.color("white")
border.width(3)
for _ in range(4):
    border.forward(600)
    border.right(90)
border.hideturtle()

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("cyan")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

score_board = turtle.Turtle()
score_board.shape("square")
score_board.penup()
score_board.ht()
score_board.goto(0, 260)
score_board.color("white")
score_board.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "normal"))

game_over = turtle.Turtle()
game_over.shape("square")
game_over.penup()
game_over.ht()
game_over.goto(0, 0)
game_over.color("white")

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_snake():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

window.listen()
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")
icon = PhotoImage(file="Python_Projects\Snake Game\icon.png") 
window._root.iconphoto(True, icon)

while True:
    window.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over.clear()
        game_over.write("Game Over", align="center", font=("Arial", 36, "normal"))
        window.update()
        time.sleep(2)
        game_over.clear()
        head.goto(0, 0)
        head.direction = "stop"
        
        for body in snake:
            body.goto(1000, 1000)  
        snake.clear()

        points = 0
        delay = 0.1
        score_board.clear()
        score_board.write("Score: {}  High Score: {}".format(points, high_score), align="center", font=("Arial", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("cyan")
        body.penup()
        snake.append(body)

        points += 1
        delay -= 0.001

        if points > high_score:
            high_score = points

        score_board.clear()
        score_board.write("Score: {}  High Score: {}".format(points, high_score), align="center", font=("Arial", 24, "normal"))

    for index in range(len(snake) - 1, 0, -1):
        x = snake[index - 1].xcor()
        y = snake[index - 1].ycor()
        snake[index].goto(x, y)

    if len(snake) > 0:
        x = head.xcor()
        y = head.ycor()
        snake[0].goto(x, y)

    move_snake()

    for body in snake:
        if body.distance(head) < 20:
            game_over.clear()
            game_over.write("Game Over", align="center", font=("Arial", 36, "normal"))
            window.update()
            time.sleep(2)
            game_over.clear()
            head.goto(0, 0)
            head.direction = "stop"

            for body in snake:
                body.goto(1000, 1000)
            snake.clear()

            points = 0
            delay = 0.1

            score_board.clear()
            score_board.write("Score: {}  High Score: {}".format(points, high_score), align="center", font=("Arial", 24, "normal"))

    time.sleep(delay)
