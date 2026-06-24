import turtle

# 1. Screen Setup
win = turtle.Screen()
win.title("Simple Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score tracking
score = 0

# 2. Paddle (Player)
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# 3. Ball (YAHAN SPEED SLOW KI HAI)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1  # Pehle 0.25 tha, ab slow (0.1) kar diya
ball.dy = -0.1 # Pehle -0.25 tha, ab slow (-0.1) kar diya

# 4. Score Display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# 5. Functions to move paddle
def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 30
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 30
    paddle.setx(x)

# Keyboard controls
win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")

# 6. Main Game Loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall collisions (Left and Right)
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    # Wall collision (Top)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Game Over (Yahan bhi reset speed slow rakhi hai)
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy = -0.1  # Reset speed slow rahegi
        score = 0        
        pen.clear()
        pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    # Paddle and Ball collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
        