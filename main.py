import turtle
import time

class Doraemon:
    def _init_(self):
        self.s = turtle.Screen()
        self.s.setup(width=1000, height=800)

    def my_goto(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

    def eyes(self):
        turtle.fillcolor("White")
        turtle.begin_fill()
        turtle.tracer(False)
        a = 2.5
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                turtle.left(3)
                turtle.forward(a)
            else:
                a += 0.05
                turtle.left(3)
                turtle.forward(a)
        turtle.tracer(True)
        turtle.end_fill()

    def beard(self):
        self.my_goto(-32, 135)
        turtle.setheading(165)
        turtle.forward(60)
        self.my_goto(-32, 125)
        turtle.setheading(180)
        turtle.forward(60)
        self.my_goto(-32, 115)
        turtle.setheading(193)
        turtle.forward(60)
        self.my_goto(37, 125)
        turtle.setheading(15)
        turtle.forward(60)
        self.my_goto(37, 125)
        turtle.setheading(0)
        turtle.forward(60)
        self.my_goto(37, 115)
        turtle.setheading(-13)
        turtle.forward(60)

    def mouth(self):
        self.my_goto(5, 148)
        turtle.setheading(270)
        turtle.forward(100)
        turtle.setheading(0)
        turtle.circle(120, 50)
        turtle.setheading(230)
        turtle.circle(-120, 100)

    def scarf(self):
        turtle.fillcolor("Red")
        turtle.begin_fill()
        turtle.setheading(0)
        turtle.forward(200)
        turtle.circle(-5, 90)
        turtle.forward(10)
        turtle.circle(-5, 90)
        turtle.forward(207)
        turtle.circle(-5, 90)
        turtle.forward(10)
        turtle.circle(-5, 90)
        turtle.end_fill()

    def nose(self):
        self.my_goto(-10, 158)
        turtle.setheading(315)
        turtle.fillcolor("Red")
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()

    def pupil(self):
        turtle.setheading(0)
        self.my_goto(-20, 195)
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(13)
        turtle.end_fill()
        turtle.pensize(6)
        self.my_goto(20, 205)
        turtle.setheading(75)
        turtle.circle(-10, 150)
        turtle.pensize(4)
        self.my_goto(-17, 200)
        turtle.setheading(0)
        turtle.fillcolor("White")
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        self.my_goto(0, 0)

    def face(self):
        turtle.forward(183)
        turtle.left(45)
        turtle.fillcolor("White")
        turtle.begin_fill()
        turtle.circle(120, 100)
        turtle.setheading(180)
        turtle.forward(121)
        turtle.pendown()
        turtle.setheading(215)
        turtle.circle(120, 100)
        turtle.end_fill()
        self.my_goto(63.56, 218.24)
        turtle.setheading(90)
        self.eyes()
        turtle.setheading(180)
        turtle.penup()
        turtle.forward(60)
        turtle.pendown()
        turtle.setheading(90)
        self.eyes()
        turtle.penup()
        turtle.setheading(180)
        turtle.forward(64)

    def head(self):
        turtle.penup()
        turtle.circle(150, 40)
        turtle.pendown()
        turtle.fillcolor("Blue")
        turtle.begin_fill()
        turtle.circle(150, 280)
        turtle.end_fill()

    def start(self):
        self.head()
        self.scarf()
        self.face()
        self.pupil()
        self.nose()
        self.mouth()
        self.beard()
        self.my_goto(0, 0)
        turtle.setheading(0)
        turtle.penup()
        turtle.circle(150, 50)
        turtle.pendown()
        turtle.setheading(30)
        turtle.forward(40)
        turtle.setheading(70)
        turtle.circle(-30, 270)
        turtle.fillcolor("Blue")
        turtle.begin_fill()
        turtle.setheading(230)
        turtle.forward(80)
        turtle.setheading(90)
        turtle.circle(1000, 1)
        turtle.setheading(-89)
        turtle.circle(-1000, 10)
        turtle.setheading(180)
        turtle.forward(70)
        turtle.setheading(90)
        turtle.circle(30, 180)
        turtle.setheading(180)
        turtle.forward(70)
        turtle.setheading(100)
        turtle.circle(-1000, 9)
        turtle.setheading(-86)
        turtle.circle(1000, 2)
        turtle.setheading(230)
        turtle.forward(40)
        turtle.circle(-30, 230)
        turtle.setheading(45)
        turtle.forward(81)
        turtle.setheading(0)
        turtle.forward(203)
        turtle.circle(5, 90)
        turtle.forward(10)
        turtle.circle(5, 90)
        turtle.forward(7)
        turtle.setheading(40)
        turtle.circle(150, 10)
        turtle.setheading(30)
        turtle.forward(40)
        turtle.end_fill()
        turtle.setheading(70)
        turtle.fillcolor("White")
        turtle.begin_fill()
        turtle.circle(-30)
        turtle.end_fill()
        self.my_goto(103.74, -182.59)
        turtle.setheading(0)
        turtle.fillcolor("White")
        turtle.begin_fill()
        turtle.forward(15)
        turtle.circle(-15, 180)
        turtle.forward(90)
        turtle.circle(-15, 180)
        turtle.forward(10)
        turtle.end_fill()
        self.my_goto(-96.26, -182.59)
        turtle.setheading(180)
        turtle.fillcolor("White")
        turtle.begin_fill()
        turtle.forward(15)
        turtle.circle(15, 180)
        turtle.forward(90)
        turtle.circle(15, 180)
        turtle.forward(10)
        turtle.end_fill()
        self.my_goto(-133.97, -91.81)
        turtle.setheading(50)
        turtle.fillcolor("White")
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()
        self.my_goto(-103.42, 15.09)
        turtle.setheading(0)
        turtle.forward(38)
        turtle.setheading(230)
        turtle.begin_fill()
        turtle.circle (90, 260)
        turtle.end_fill()
        self.my_goto(5, -40)
        turtle.setheading(0)
        turtle.forward(70)
        turtle.setheading(-90)
        turtle.circle(-70, 180)
        turtle.setheading(0)
        turtle.forward(70)
        self.my_goto(-103.42, 15.09)
        turtle.forward(90)
        turtle.setheading(70)
        turtle.fillcolor("Yellow")
        turtle.begin_fill()
        turtle.circle(-20)
        turtle.end_fill()
        turtle.setheading(170)
        turtle.fillcolor("green")
        turtle.begin_fill()
        turtle.circle(-2, 180)
        turtle.setheading(10)
        turtle.circle(-100, 22)
        turtle.circle(-2, 180)
        turtle.setheading(180 - 10)
        turtle.circle(100, 22)
        turtle.end_fill()
        turtle.goto(-13.42, 15.09)
        turtle.setheading(250)
        turtle.circle(20, 110)
        turtle.setheading(90)
        turtle.forward(15)
        turtle.dot(10)
        self.my_goto(0, -150)

if __name__ == '__main__':
    turtle.speed(9)
    d = Doraemon()
    d.start()
    turtle.mainloop()