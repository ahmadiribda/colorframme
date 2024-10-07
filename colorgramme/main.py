import random
import turtle

from turtle import Turtle, Screen

turtle.colormode(255)
#import colorgram
#colors = colorgram.extract("hirst.jpg", 10)
#rgb_colors=[]
#for i in colors:
#    r=i.rgb.r
#    g=i.rgb.g
#    b=i.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#print(rgb_colors)

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5),
              (227, 159, 49)]
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(205)
tim.forward(270)
tim.setheading(0)
tim.speed(10)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
