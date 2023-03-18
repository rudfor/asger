import turtle as t
import random

canvas_width = 500
canvas_height = 500
canvas_width_range = range(501)

t.setworldcoordinates(0, 0, canvas_width, canvas_height)
t.bgcolor("black")


# Drawing from back to front, I want to place random stars, that are covered up by the buildings, in case they are in the
# same place, therefore I start with the stars.

def stars():
    t.fillcolor("white")
    for x in range(25):
        t.speed(100)
        x_position = random.randint(0, 500)
        y_position = random.randint(150, 500)
        t.penup()
        t.goto(x_position, y_position)
        t.pendown()
        t.begin_fill()
        t.circle(2)
        t.end_fill()


def highrise():
    global high_poly_1, high_poly_2, high_poly_3, high_poly_4, high_poly_5, high_poly_6, total_poly
    high_poly_1 = []            #Trying to create some definitions of where the buildings actually
    high_poly_2 = []            # end up so i maybe can use it later, how i dont know
    high_poly_3 = []            # But my intentions has been stated futher down
    high_poly_4 = []
    high_poly_5 = []
    high_poly_6 = []
    total_poly = [high_poly_1, high_poly_2, high_poly_3, high_poly_4, high_poly_5, high_poly_6]

    last_build_x = -60

    for j in range(6):
        t.fillcolor("grey")
        build_width = random.randint(50, 140)
        build_height = random.randint(180, 485)
        build_x = last_build_x + build_width + random.randint(40, 60)
        build_y = -10
        t.penup()
        t.goto(build_x, build_y)
        t.pendown()
        t.begin_fill()
        t.begin_poly()
        t.setheading(180)
        t.forward(build_width)
        t.right(90)
        t.forward(build_height)
        t.right(90)
        t.forward(build_width)
        t.right(90)
        t.forward(build_height)
        t.end_poly()
        t.end_fill()
        t.penup()

        last_build_x += build_width

        total_poly[j].append(t.get_poly())

def windows():
    t.fillcolor("white")
    # Draw squares randomly
    for i in range(10):                                             #Example window amount
        x = random.randint(total_poly_x_min, total_poly_x_max)      #Example explanitory text
        y = random.randint(total_poly_y_min, total_poly_y_max)      # I know that this is invalid but its to point out where i want my windows to be
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        for j in range(4):
            t.forward(10)
            t.right(90)
        t.end_fill()


stars()
highrise()
windows()

t.mainloop()