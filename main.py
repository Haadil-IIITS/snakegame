from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake=Snake()
# snake.create_snake()


food=Food()

game_on=True
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)
scoreboard=Scoreboard()
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.xcor()>(290) or snake.head.xcor()<(-290) or snake.head.ycor()>(290) or snake.head.ycor()<(-290):
        scoreboard.reset_scoreboard()


        snake.reset()


    #detect collision from food
    if snake.head.distance(food)< 20:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    for segment in snake.segment:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset_scoreboard()



            snake.reset()



screen.exitonclick()

















