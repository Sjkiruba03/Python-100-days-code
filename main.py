
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time
from snake import Snake

my_screen = Screen()
my_screen.setup(width=500, height=500)
my_screen.bgcolor("black")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    snake.move()

    #collisoin with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.calculate_score()
        print("Yummy......!")

    if snake.head.xcor() > 245 or snake.head.xcor() < -245 or snake.head.ycor() > 245 or snake.head.ycor() < -245:
        scoreboard.reset()
        snake.reset()
        # game_is_on = False
        # scoreboard.game_over()

    # detect collision with the tail

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



my_screen.title("Snake Game")
my_screen.exitonclick()