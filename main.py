import turtle
import time
import random

wn = turtle.Screen()
wn.title("Змейка")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

snake = []
for i in range(3):
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color("white")
    segment.penup()
    segment.goto(-20 * i, 0)
    snake.append(segment)

bonus = turtle.Turtle()
bonus.shape("circle")
bonus.color("red")
bonus.penup()
bonus.goto(random.randint(-290, 290), random.randint(-290, 290))


def go_up():
    if snake[0].heading() != 270:
        snake[0].setheading(90)


def go_down():
    if snake[0].heading() != 90:
        snake[0].setheading(270)


def go_left():
    if snake[0].heading() != 0:
        snake[0].setheading(180)


def go_right():
    if snake[0].heading() != 180:
        snake[0].setheading(0)


wn.listen()
wn.onkeypress(go_up, "w" or "ц")
wn.onkeypress(go_down, "s" or "ы")
wn.onkeypress(go_left, "a" or "ф")
wn.onkeypress(go_right, "d" or "в")

score = 0
while True:
    wn.update()

    if snake[0].distance(bonus) < 20:
        bonus.goto(random.randint(-290, 290), random.randint(-290, 290))
        score += 1
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        snake.append(segment)

    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)

    snake[0].forward(20)

    if (snake[0].xcor() > 290 or snake[0].xcor() < -290 or
            snake[0].ycor() > 290 or snake[0].ycor() < -290):
        print("Игра окончена! Ваш счёт: {}".format(score))
        break

    time.sleep(0.1)